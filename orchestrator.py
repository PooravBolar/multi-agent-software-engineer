from agents.product_manager import ProductManagerAgent
from agents.tech_lead import TechLeadAgent
from agents.developer import DeveloperAgent
from agents.qa import QaAgent
from memory.memory_store import SharedMemory
from uuid import uuid4

memory = SharedMemory()

class Orchestrator:
    def __init__(self):
        self.pm = ProductManagerAgent()
        self.tech_lead = TechLeadAgent()
        self.developer = DeveloperAgent()
        self.critic = QaAgent()
        
    def run(self,goal, max_iterations=6, score_threshold=8, min_delta=0.3):
        
        #Create unique session id
        run_id = str(uuid4())
        memory.update("run_id", run_id)
        
        memory.update("goal", goal)
        
        print("\n[Orchestrator] Asking PM to generate tasks...\n")
        past_feedback = memory.get("qa_feedback")
        pm_output = self.pm.generate_tasks(goal, past_feedback)

        memory.update("pm_output", pm_output)
        tasks = pm_output.get("tasks", [])
        
        
        print("\n[Orchestrator] Passing tasks to Tech Lead...\n")
        tech_output = self.tech_lead.review_tasks(goal, tasks)
        memory.update("tech_output", tech_output)
        refined_tasks = tech_output.get("refined_tasks", [])
        
        memory.update("architecture", tech_output.get("architecture_suggestions"))
        memory.update("risks", tech_output.get("missing_considerations"))

        
        print("\n[Orchestrator] Asking Developer to generate plan...\n")  
        dev_output = self.developer.implement_task(goal, refined_tasks)
        
        # Store first dev version
        memory.append("dev_versions", dev_output)
        
        iteration = 0
        previous_score = 0
        converged = False
        iteration_history = []
    
        while not converged and iteration < max_iterations:
            
            iteration +=1;
            print(f"\n[Orchestrator] Iteration {iteration}: Asking Critic to review...\n")
            critic_output = self.critic.review_developer_plan(goal, dev_output)
            
            if "error" in critic_output:
                print("[Orchestrator] Critic returned malformed JSON. Retrying once...")
                critic_output = self.critic.review_developer_plan(goal, dev_output)
                memory.append("qa_feedback", critic_output)
                memory.add_score(critic_output.get("score", 0))

            
                if "error" in critic_output:
                    print("[Orchestrator] Critic failed twice. Skipping iteration.")
                    continue
            
            # Store critic review
            memory.append("critic_reviews", critic_output)
            
            current_score = critic_output.get("score", 0)
            improvement = current_score - previous_score
            
            print(f"[Orchestrator] Score: {current_score} | Improvement: {improvement}")
            
            iteration_data = {
            "iteration": iteration,
            "score": current_score,
            "improvement": improvement
            }

            iteration_history.append(iteration_data)
            memory.append("iteration_history", iteration_data)
            
            # Convergence rules
            if current_score >= score_threshold:
                converged = True
                reason = "Quality threshold reached"

            elif improvement < min_delta and iteration > 1:
                converged = True
                reason = "Improvement plateau detected"

            else:
                previous_score = current_score

                print("\n[Orchestrator] Asking Developer to revise plan...\n")
                dev_output = self.developer.revise_plan(
                    goal,
                    dev_output,
                    critic_output
                )
                
                # Save new dev version
                memory.append("dev_versions", dev_output)

        if converged:
            print(f"\n[Orchestrator] Converged: {reason}")
        else:
            print("\n[Orchestrator] Max iterations reached without convergence")

        final_state = {
        "final_plan": dev_output,
        "final_score": current_score,
        "iterations": iteration
        }

        memory.update("final_state", final_state)

        return {
            "pm_tasks": tasks,
            "tech_lead_review": tech_output,
            "final_developer_plan": dev_output,
            "iteration_history": iteration_history,
            "final_critic_review": critic_output
        }