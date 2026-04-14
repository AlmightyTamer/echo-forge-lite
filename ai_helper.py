import requests
import json
import streamlit as st

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_project_plan(issue_description):
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except:
        st.error("Missing API key. Please set GROQ_API_KEY in Streamlit secrets.")
        return fallback_plan()

    prompt = f"""
You are an AI assistant that helps high school students create social impact projects.
Given the issue: "{issue_description}"

Generate a JSON response with exactly these fields:
- "project_name": a catchy, teen-friendly name (max 8 words)
- "action_steps": a list of 3-5 concrete, actionable steps (each a short phrase)
- "impact_estimate": a one‑sentence estimate of potential reach/effect (e.g., "Could reach 200 students per month")

Return ONLY valid JSON, no other text.
"""
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "response_format": {"type": "json_object"}
    }
    try:
        response = requests.post(GROQ_URL, json=payload, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        content = data["choices"][0]["message"]["content"]
        plan = json.loads(content)
        return {
            "project_name": plan.get("project_name", "Impact Initiative"),
            "action_steps": plan.get("action_steps", ["Research the issue", "Plan your first action"]),
            "impact_estimate": plan.get("impact_estimate", "This project will create positive change.")
        }
    except Exception as e:
        st.error(f"AI service error: {e}")
        return fallback_plan()

def fallback_plan():
    return {
        "project_name": "Community Action Plan",
        "action_steps": ["Raise awareness on social media", "Host a small event", "Track your results"],
        "impact_estimate": "Your effort will inspire at least 50 people locally."
    }
