import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

class TechLeadAgent:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )
        
    def review_tasks(self, goal, tasks):
        prompt = f"""
            You are a senior tech lead.

            A product manager has created the following task list for this goal:

            Goal:
            {goal}

            Tasks:
            {tasks}

            Your job:
            1) Improve the technical clarity of tasks
            2) Add missing important technical steps
            3) Suggest a high-level architecture
            4) Identify risks or missing considerations

            Return ONLY JSON in this format:

            {{
            "refined_tasks": ["..."],
            "architecture_suggestions": "...",
            "missing_considerations": ["..."]
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
            return {
                "error": "Parsing failed",
                "raw_output": text
            }