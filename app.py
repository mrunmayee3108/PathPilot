import streamlit as st
from graph import graph
st.set_page_config(
    page_title="PathPilot AI",
    page_icon="🚀",
    layout="wide"
)

with st.sidebar:
    st.title("🤖 Agent Dashboard")

    st.markdown("""
    ### Active Agents
    > LangGraph Planner 
    > Skill Gap Agent  
    > Resource Agent  
    > Project Agent  
    > Interview Agent  
    """)

    st.markdown("---")
    st.markdown("""
    ### About
    PathPilot AI is a multi-agent career intelligence system that provides:
    - Skill gap analysis
    - Learning resources
    - Project recommendations
    - Interview preparation
    """)

st.title("PathPilot AI")
st.subheader("Multi-Agent Career Intelligence System for Personalized Learning")

st.markdown("""
Enter your career goal and current skills.  
Our AI agents will generate a personalized roadmap for you.
""")

st.markdown("---")

goal = st.text_input(
    "Enter Your Career Goal",
    placeholder="Example: Become a Machine Learning Engineer"
)

skills = st.text_area(
    "Enter Current Skills (comma separated)",
    placeholder="Python, Pandas, SQL"
)

timeline = st.selectbox(
    "Select Timeline",
    ["3 months", "6 months", "1 year"]
)

if st.button("Generate Roadmap"):

    if not goal or not skills:
        st.warning("Please enter both goal and skills.")
    else:
        state = {
            "goal": goal,
            "skills": [skill.strip() for skill in skills.split(",")],
            "timeline": timeline
        }

        st.info("LangGraph Supervisor initialized")
        st.info("Planning execution graph...")
        st.info("Executing AI agents...")

        with st.spinner("Generating personalized roadmap..."):
            outputs = graph.invoke(state)

        st.success("Roadmap Generated Successfully!")

        st.markdown("---")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Skill Gap Analysis")
            st.write(outputs.get("skill_report", "No skill analysis available."))

        with col2:
            st.subheader("📚 Recommended Resources")
            st.write(outputs.get("resources", "No resources available."))

        st.markdown("---")

        col3, col4 = st.columns(2)

        with col3:
            st.subheader("Recommended Projects")
            st.write(outputs.get("projects", "No project suggestions available."))

        with col4:
            if outputs.get("interview"):
                st.subheader("Interview Preparation")
                st.write(outputs["interview"])
            else:
                st.subheader("Interview Preparation")
                st.write("Interview preparation not required for this goal.")

        st.markdown("---")

        st.subheader("Final Learning Path Summary")

        summary = f"""
        Goal: **{goal}**  
        Timeline: **{timeline}**  
        Current Skills: **{', '.join(state['skills'])}**
        """

        st.markdown(summary)

        st.success("""
        PathPilot AI has completed multi-agent planning and generated
        your personalized career roadmap.
        """)