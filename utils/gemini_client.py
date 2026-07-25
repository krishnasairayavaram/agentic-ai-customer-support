import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError, ServerError
import streamlit as st

load_dotenv()

client = genai.Client(
    api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
)

def ask_gemini(prompt: str):
    retries = 3

    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model="models/gemini-3.5-flash",
                contents=prompt
            )
            return response.text

        except ServerError:
            if attempt < retries - 1:
                time.sleep(5)
            else:
                raise Exception("Gemini server is busy. Please try again in a minute.")

        except ClientError as e:
            raise Exception(f"Gemini API Error: {e}")