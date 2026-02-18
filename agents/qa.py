import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

class QaAgent:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )
    
    def review_developer_plan(self, goal, developer_output):
        prompt = f"""
            You are a highly critical CTO reviewing a developer's implementation plan.

            Product Goal:
            {goal}

            Developer Plan:
            {developer_output}

            Your job:
            1) Score the plan from 1-10
            2) Identify strengths
            3) Identify weaknesses
            4) Suggest improvements
            5) Decide APPROVE or REVISE

            Be strict. Avoid generic praise.

            Return ONLY JSON:

            {{
            "score": 0,
            "strengths": [],
            "weaknesses": [],
            "suggested_improvements": [],
            "decision": ""
            }}
            
            No explanation.
            No markdown.
            No extra text.
            
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