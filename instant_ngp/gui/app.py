import streamlit as st

from instant_ngp.gui import sidebar, states, ui

if __name__ == "__main__":
    st.title("Instant NGP WebUI")
    states.init_states()
    sidebar.sidebar()

    aabb_scale = ui.extract_frames()
    st.markdown("---")
    ui.align_camera(aabb_scale)
    st.markdown("---")
    ui.interative_training()
