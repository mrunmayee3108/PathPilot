import os
from urllib import response 
import google.generativeai as genai
from dotenv import load_dotenv
from urllib import response
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

def skill_gap_agent(state):
    prompt = f"""
    User goal: {state['goal']}
    Current skills: {state['skills']}
    Identify missing skills required to achieve the user's goal. Give bullet points.
    """
    response = model.generate_content(prompt)
    return response

# test 
# state = {
#     "goal": "Become Machine Learning Engineer",
#     "skills": ["Python", "Pandas"]
# }
# print(skill_gap_agent(state).text)

def resource_agent(state, skill_report):
    prompt = f"""
    Missing skills: {skill_report}
    Recommended learning resources: 
    - courses
    - documentation
    - practice websites
    - tutorials
    """
    response = model.generate_content(prompt)
    return response.text

def project_agent(state):
    prompt = f"""
    Goal: {state['goal']}
    Suggest 3 impressive portfolio projects. 
    The projects should be relevant to the user's goal and skills. Provide a brief description for each project. 
    The projects should be challenging enough to demonstrate the user's capabilities and help them stand out in the job market. 
    Mention difficulty and tech stack.
    """
    response = model.generate_content(prompt)
    return response.text

def interview_agent(state):
    prompt = f"""
    Goal: {state['goal']}
    Generate interview questions:
    - easy
    - medium
    - hard
    """
    response = model.generate_content(prompt)
    return response.text