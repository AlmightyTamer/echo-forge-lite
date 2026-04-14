import streamlit as st
from utils import generate_project_summary_md

def display_project_card(project, idx, show_progress=True, show_delete=True):
    with st.container():
        st.markdown(f"### ✨ {project['project_name']}")
        st.markdown(f"**Issue:** {project['issue']}")
        st.markdown(f"**Impact:** {project['impact_estimate']}")
        if show_progress:
            new_progress = st.slider("Progress %", 0, 100, project['progress'], key=f"progress_{idx}")
            if new_progress != project['progress']:
                project['progress'] = new_progress
        st.markdown("**Action Steps:**")
        for step in project['action_steps']:
            st.markdown(f"- {step}")
        notes = st.text_area("Notes / Updates", project.get('notes', ''), key=f"notes_{idx}")
        project['notes'] = notes
        col1, col2 = st.columns(2)
        with col1:
            if show_delete and st.button("🗑️ Delete", key=f"del_{idx}"):
                return "delete"
        with col2:
            if st.button("📥 Share Summary", key=f"share_{idx}"):
                md = generate_project_summary_md(project)
                st.download_button("Download Markdown", md, file_name=f"{project['project_name']}_summary.md", key=f"dl_{idx}")
        st.divider()
        return None

def community_project_card(proj, idx):
    col1, col2, col3 = st.columns([3,1,1])
    with col1:
        st.markdown(f"**{proj['name']}** by *{proj['author']}*")
        st.caption(f"{proj['issue']} · {proj['impact']}")
    with col2:
        if st.button(f"❤️ {proj['likes']}", key=f"like_{idx}"):
            return "like"
    with col3:
        if st.button("📎 Fork", key=f"fork_{idx}"):
            return "fork"
    return None
