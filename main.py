from orchestrator import Orchestrator

if __name__ == "__main__":
    
    goal = input("Enter Product Goal: ")
    
    orchestrator = Orchestrator()
    result = orchestrator.run(goal)
    
    print("\nGenerated Tasks:\n")
    print(result)