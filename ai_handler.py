import google.generativeai as genai
import json
from config import get_gemini_api_key


class GeminiAIHandler:
    def __init__(self):
        api_key = get_gemini_api_key()
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

        self.system_prompt = """
        You are a leave management system assistant. Your task is to analyze user queries and extract relevant information.
        For each query, provide a JSON response with the following structure:
        {
            "intent": "check_balance|request_leave|cancel_leave|view_history",
            "leave_type": "sick_leave|annual_leave|maternity_leave|null",
            "days": null|number,
            "start_date": "YYYY-MM-DD"|null,
            "extracted_info": "any additional relevant information"
        }
        Only provide the JSON response, nothing else.
        """

    async def analyze_query(self, query: str) -> dict:
        """Analyze user query using Gemini AI"""
        try:
            prompt = f"{self.system_prompt}\nUser query: {query}"
            response = self.model.generate_content(prompt)

            return json.loads(response.text)
        except Exception as e:
            print(f"Error in Gemini API call: {e}")
            return {
                "intent": "unknown",
                "leave_type": None,
                "days": None,
                "start_date": None,
                "extracted_info": None
            }
