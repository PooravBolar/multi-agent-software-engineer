import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

class ProductManagerAgent:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def generate_tasks(self, goal, past_feedback=None):
        prompt = f"""
            Previous system feedback (learn from past mistakes):
            {past_feedback if past_feedback else "None"}
            You are a senior product manager.

            Break the following product goal into clear, actionable development tasks.

            Goal:
            {goal}
            
            No explanation.
            No markdown.
            No extra text.
            Return ONLY valid JSON in this format:
            {{
            "tasks": ["task1", "task2", "task3"]
            }}
        """

        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        text = response.text.strip()
        
        if text.startswith('```'):
            text = text.replace("```json","").replace("```","").strip()

        try:
            return json.loads(text)
        
        except Exception as e:
            return {
                "error": "Failed to parse JSON",
                "raw_output": text
            }
