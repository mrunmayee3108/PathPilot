from agents import (
    skill_gap_agent,
    resource_agent,
    project_agent,
    interview_agent
)

class Supervisor:

    def run(self, state):
        outputs = {}
        if len(state["skills"]) < 5:
            skill_report = skill_gap_agent(state)
            outputs["skills"] = skill_report
        else:
            skill_report = "User already has strong foundational skills."
            outputs["skills"] = skill_report
        resources = resource_agent(state, skill_report)
        outputs["resources"] = resources
        projects = project_agent(state)
        outputs["projects"] = projects
        if "interview" in state["goal"].lower() or "job" in state["goal"].lower():
            interview = interview_agent(state)
            outputs["interview"] = interview
        return outputs