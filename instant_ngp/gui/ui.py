import traceback as tb

import streamlit as st

from instant_ngp.gui import commands


def extract_frames():
    st.markdown("### 1. Extract Frames")
    file = st.file_uploader("Upload your dataset", type=["mp4", "avi", "mov", "mkv"])

    if not file:
        st.info("Please upload a video file.")
        st.session_state.is_data_prepared = False
        return
    else:
        is_data_prepared = st.button("📦 Prepare data")
        if is_data_prepared:
            with st.spinner("Preparing data..."):
                try:
                    st.session_state.video_path = commands.prepare_data(file)
                    st.session_state.is_data_prepared = True
                except Exception as e:
                    st.error(e)
                    tb.print_exc()
                    return

    if not st.session_state.is_data_prepared:
        return
    col1, col2 = st.columns(2)
    with col1:
        fps = st.slider(
            "Frame Per Second",
            0,
            30,
            value=2,
            help="Defines the number of frames per second to extract from the video.",
        )
    with col2:
        aabb_scale = st.select_slider(
            "Scene Extent Scale",
            options=[1, 2, 4, 8, 16, 32, 64, 128],
            help="Defines the bounding box size for the scene. Set higher for larger, \
                natural scenes (max 128) and lower for smaller, synthetic scenes. \
                Adjust for optimal scene coverage \
                and training speed.",
        )

    st.info("It is recommended to remove blurry frames from extraction.")
    col1, col2 = st.columns([1, 2])
    with col1:
        button_extract_frames = st.empty()
        # extract frames
        with st.spinner("Extracting frames..."):
            if button_extract_frames.button("🎞️ Extract frames"):
                try:
                    commands.extract_frames(
                        st.session_state.video_path, fps, aabb_scale
                    )
                    st.toast("Frames extracted.", icon="🎞️")
                except Exception as e:
                    st.error(e)
                    tb.print_exc()
                    return
    with col2:
        open_dir_button = st.empty()
        # open directory
        if open_dir_button.button("📁 Open directory"):
            try:
                commands.open_directory()
            except Exception as e:
                st.error(e)
                tb.print_exc()
                return

    return int(aabb_scale)


def align_camera(aabb_scale: int):
    st.markdown("### 2. Align Cameras")
    colmap_matcher = st.selectbox(
        "Colmap Matcher",
        ["exhaustive", "sequential", "spatial", "transitive", "vocab_tree"],
        help="Select which matcher colmap should use. Sequential for videos, \
            exhaustive for images.",
    )
    align_button = st.empty()
    with st.spinner("Aligning cameras..."):
        if align_button.button("📐 Align cameras"):
            try:
                commands.align_camera(colmap_matcher, aabb_scale)
                st.toast("Cameras aligned.", icon="📐")
            except Exception as e:
                st.error(e)
                tb.print_exc()
                return


def interative_training():
    st.markdown("### 3. Interactive Training")
    train_button = st.empty()
    with st.spinner("Training..."):
        if train_button.button("🚀 Train"):
            try:
                commands.activate_interactive_training()
            except Exception as e:
                st.error(e)
                tb.print_exc()
                return
