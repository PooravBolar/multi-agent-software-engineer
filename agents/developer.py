import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

class DeveloperAgent:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )
    
    def implement_task(self, goal, refined_tasks):
        #Pick one task at a time
        task = refined_tasks[0]
        
        prompt = f"""
            You are a senior software developer.

            Goal:
            {goal}

            Task assigned:
            {task}

            Your job:
            1) Explain how you would implement this
            2) Suggest tech stack/tools
            3) Break it into step-by-step development steps
            4) Estimate complexity

            Return ONLY JSON:

            {{
            "selected_task": "...",
            "implementation_plan": ["step1", "step2"],
            "tech_stack": ["..."],
            "complexity": "Low/Medium/High"
            }}
            
            No markdown.
            No explanation.
            Only JSON.
            
            """
            
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        text = response.text.strip()
        
        if text.startswith("```"):
            text = text.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(text)
        
        except:
            return {"error": "Parsing failed", "raw_output": text}
        
    
    def revise_plan(self, goal, previous_plan, critic_feedback):
        prompt = f"""
            You are a senior software developer revising your implementation plan.

            Goal:
            {goal}

            Previous Plan:
            {previous_plan}

            Critic Feedback:
            {critic_feedback}

            Revise the implementation plan by addressing all weaknesses and suggested improvements.

            Be concrete. Make firm technical decisions.

            Return ONLY JSON:

            {{
            "selected_task": "...",
            "implementation_plan": [],
            "tech_stack": [],
            "complexity": ""
            }}
            
            No markdown.
            No explanation.
            Only JSON.
            
            """

        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "").replace("```", "").strip()

        try:
            return json.loads(text)
        except:
            return {"error": "Parsing failed", "raw_output": text}