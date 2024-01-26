import streamlit as st

from common import constants as const


def init_states():
    if "is_data_prepared" not in st.session_state:
        st.session_state.is_data_prepared = False

    if "video_path" not in st.session_state:
        st.session_state.video_path = None

    if "info" not in st.session_state:
        st.session_state.info = const.PROJECT_INFO
