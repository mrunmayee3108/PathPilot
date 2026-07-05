from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from agents import (
    skill_gap_agent,
    resource_agent,
    project_agent,
    interview_agent
)

class CareerState(TypedDict, total=False):
    goal: str
    skills: list
    timeline: str

    skill_report: str
    resources: str
    projects: str
    interview: str
    next_step: str

def supervisor_node(state: CareerState):

    goal = state["goal"].lower()

    if "interview" in goal or "job" in goal:
        return {"next_step": "interview"}

    return {"next_step": "skill"}

def skill_node(state: CareerState):

    report = skill_gap_agent(state)

    return {
        "skill_report": report
    }

def resource_node(state: CareerState):

    resources = resource_agent(
        state,
        state["skill_report"]
    )

    return {
        "resources": resources
    }


def project_node(state: CareerState):

    projects = project_agent(state)

    return {
        "projects": projects
    }

def interview_node(state: CareerState):

    interview = interview_agent(state)

    return {
        "interview": interview
    }


builder = StateGraph(CareerState)

builder.add_node("supervisor", supervisor_node)
builder.add_node("skill", skill_node)
builder.add_node("resource", resource_node)
builder.add_node("project", project_node)
builder.add_node("interview", interview_node)

builder.add_edge(START, "supervisor")

builder.add_conditional_edges(
    "supervisor",
    lambda state: state["next_step"],
    {
        "skill": "skill",
        "interview": "interview",
    },
)
builder.add_edge("skill", "resource")
builder.add_edge("resource", "project")
builder.add_edge("project", END)
builder.add_edge("interview", END)
graph = builder.compile()