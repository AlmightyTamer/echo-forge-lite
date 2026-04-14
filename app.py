import streamlit as st
from data import get_issues, get_community_projects
from ai_helper import generate_project_plan
from components import display_project_card, community_project_card
from utils import seed_session_state, export_all_projects

st.set_page_config(page_title="EchoForge Lite", page_icon="🌍", layout="wide")

seed_session_state()

st.sidebar.title("⚡ EchoForge Lite")
st.sidebar.markdown("**Forge real impact, one step at a time.**")
page = st.sidebar.radio("Navigate", ["🏠 Discover Issues", "🤖 AI Forge Studio", "📁 My Projects", "🌍 Community Feed"])

def save_project(project_data):
    new_id = max([p['id'] for p in st.session_state.my_projects] + [-1]) + 1
    project_data['id'] = new_id
    project_data['progress'] = 0
    project_data['notes'] = ""
    st.session_state.my_projects.append(project_data)
    st.success("✅ Project forged! Check it in **My Projects**.")
    st.balloons()

if page == "🏠 Discover Issues":
    st.title("🌍 Discover Real‑World Issues")
    st.markdown("Explore challenges in your community. Click **Forge this issue** to start an AI‑powered action plan.")
    issues = get_issues()
    cols = st.columns(2)
    for idx, issue in enumerate(issues):
        with cols[idx % 2]:
            st.markdown(f"### {issue['emoji']} {issue['title']}")
            st.caption(f"*{issue['category']} · {issue['region']}*")
            st.write(issue['desc'])
            if st.button(f"Forge this issue →", key=f"forge_{idx}"):
                st.session_state.selected_issue = issue['title']
                st.session_state.page_override = "🤖 AI Forge Studio"
                st.rerun()
            st.divider()
    st.info("🗺️ **Impact Map** – Coming soon: see where students are forging change across the USA!")

elif page == "🤖 AI Forge Studio":
    st.title("🤖 AI Forge Studio")
    st.markdown("Describe an issue you care about, and our AI will generate a custom action plan + impact preview.")
    default_issue = st.session_state.get('selected_issue', "")
    issue_text = st.text_area("What issue do you want to tackle?", value=default_issue, height=100)
    if st.button("✨ Generate Action Plan", use_container_width=True):
        if not issue_text.strip():
            st.warning("Please describe an issue first.")
        else:
            with st.spinner("AI is brainstorming your impact project..."):
                plan = generate_project_plan(issue_text)
            st.session_state.generated_plan = plan
            st.session_state.generated_issue = issue_text
            st.rerun()
    if 'generated_plan' in st.session_state:
        plan = st.session_state.generated_plan
        st.success("### ✅ Your AI‑Powered Project Plan")
        st.markdown(f"**📌 Project Name:** {plan['project_name']}")
        st.markdown(f"**📊 Estimated Impact:** {plan['impact_estimate']}")
        st.markdown("**🚀 Action Steps:**")
        for step in plan['action_steps']:
            st.markdown(f"- {step}")
        st.markdown("### 🌐 Project Preview (mini impact site)")
        preview_html = f"""
        <div style="background: #1E293B; padding: 1rem; border-radius: 1rem; border-left: 5px solid #7C3AED;">
            <h3 style="margin:0;">{plan['project_name']}</h3>
            <p><strong>Issue:</strong> {st.session_state.generated_issue}</p>
            <p>{plan['impact_estimate']}</p>
            <p><em>🔥 Action steps ready – start forging today!</em></p>
        </div>
        """
        st.markdown(preview_html, unsafe_allow_html=True)
        if st.button("💾 Save to My Projects", use_container_width=True):
            new_project = {
                "issue": st.session_state.generated_issue,
                "project_name": plan['project_name'],
                "action_steps": plan['action_steps'],
                "impact_estimate": plan['impact_estimate']
            }
            save_project(new_project)
            del st.session_state.generated_plan
            st.rerun()

elif page == "📁 My Projects":
    st.title("📁 My Impact Projects")
    if not st.session_state.my_projects:
        st.info("You haven't forged any projects yet. Go to **AI Forge Studio** to start!")
    else:
        portfolio_md = export_all_projects()
        st.download_button("📦 Export Full Portfolio (Markdown)", portfolio_md, file_name="my_impact_portfolio.md", use_container_width=True)
        st.divider()
        to_delete = None
        for i, project in enumerate(st.session_state.my_projects):
            result = display_project_card(project, i, show_progress=True, show_delete=True)
            if result == "delete":
                to_delete = i
        if to_delete is not None:
            st.session_state.my_projects.pop(to_delete)
            st.rerun()

elif page == "🌍 Community Feed":
    st.title("🌍 Community Feed")
    st.markdown("Browse projects from other students – like them or fork them to your own dashboard!")
    projects = get_community_projects()
    for idx, proj in enumerate(projects):
        action = community_project_card(proj, idx)
        if action == "like":
            st.session_state.community_likes[proj['id']] += 1
            st.rerun()
        elif action == "fork":
            forked = {
                "id": -1,
                "issue": proj['issue'],
                "project_name": proj['name'],
                "action_steps": ["Review the original plan", "Adapt it to your community", "Start small"],
                "impact_estimate": proj['impact'],
                "progress": 0,
                "notes": f"Forked from {proj['author']}'s project."
            }
            save_project(forked)
            st.rerun()
    st.divider()
    st.caption("💡 *Every like and fork helps spread impact ideas. Forge your own project in the AI Studio!*")
