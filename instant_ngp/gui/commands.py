import os
import pathlib
import shutil
import subprocess
import sys

import common.constants as const
import instant_ngp.gui.utilities as utilities


def chdir(path: str):
    # change directory
    print(f"Changing directory to {path}")
    os.chdir(path)


def run_cmd(cmd: list):
    # execute command
    print(
        "Command: ",
        " ".join(cmd),
    )
    subprocess.run(cmd)
    print("Done!\n")


def prepare_data(video):
    # remove data directory if not empty
    if not utilities.is_dir_empty(const.DATA_ROOT):
        shutil.rmtree(const.DATA_ROOT)
    os.makedirs(const.DATA_ROOT, exist_ok=True)

    # write video to disk
    video_path = pathlib.Path(const.DATA_ROOT, "video.mp4").resolve().absolute()
    utilities.write_video_to_disk(video, video_path)
    return video_path


def extract_frames(video_path: str | pathlib.Path, fps: int, aabb_scale: int):
    # extract frames
    colmap_script = (
        pathlib.Path(const.CORE_ROOT, "scripts", "colmap2nerf.py").resolve().absolute()
    )
    cmd = [
        sys.executable,
        str(colmap_script),
        "--video_in",
        str(video_path),
        "--video_fps",
        str(fps),
        "--aabb_scale",
        str(aabb_scale),
        "--overwrite",
        "--run_colmap",
    ]

    # change to data directory
    chdir(const.DATA_ROOT)

    # execute command
    run_cmd(cmd)

    # change back to root directory
    chdir(const.ROOT)


def align_camera(matcher: str, aabb_scale: int):
    # align camera
    colmap_script = (
        pathlib.Path(const.CORE_ROOT, "scripts", "colmap2nerf.py").resolve().absolute()
    )
    cmd = [
        sys.executable,
        str(colmap_script),
        "--colmap_matcher",
        str(matcher),
        "--aabb_scale",
        str(aabb_scale),
        "--overwrite",
        "--run_colmap",
    ]

    # change to data directory
    chdir(const.DATA_ROOT)

    # execute command
    run_cmd(cmd)

    # change back to root directory
    chdir(const.ROOT)


def activate_interactive_training():
    # activate interactive training

    cmd = ["instant-ngp.exe", str(const.DATA_ROOT)]

    # change to core directory
    chdir(const.CORE_ROOT)

    # execute command
    run_cmd(cmd)

    # change back to root directory
    chdir(const.ROOT)


def open_directory():
    # open directory
    cmd = ["explorer", str(const.DATA_ROOT)]

    # execute command
    run_cmd(cmd)
