def write_video_to_disk(video, path):
    with open(path, "wb") as f:
        f.write(video.getbuffer())


def is_dir_empty(path):
    return not any(path.iterdir())
