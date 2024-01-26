import streamlit as st


def _info():
    info_panel = st.container()

    info = st.session_state.info

    with info_panel:
        st.markdown(f"# {info['project']['name']}")
        st.markdown(f"Version: {info['project']['version']}")
        st.markdown(f"Author: {info['project']['authors'][0]['name']}")
        st.markdown(f"[Github Repo]({info['project']['urls']['homepage']})")
        st.markdown(f"[Report a bug]({info['project']['urls']['issues']})")
        st.markdown(
            f"[License: {info['project']['license']['text']}]({info['project']['urls']['homepage']}/LICENSE)"
        )


def sidebar():
    # Create a sidebar object
    with st.sidebar:
        # Use methods of the sidebar object
        st.markdown(
            "## ⭐ Get Started\n"
            "1. 📦 Upload your dataset\n"
            "2. 🎞️ Extract frames\n"
            "3. 📐 Align camera\n"
            "4. 🚀 Interactive training\n"
        )
        st.markdown("---")
        _info()
