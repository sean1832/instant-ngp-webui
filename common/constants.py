import os
import pathlib
import toml

def _read_toml(toml_file):
    with open(toml_file, "r") as f:
        return toml.load(f)

# paths
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORE_ROOT = pathlib.Path(ROOT, "instant_ngp", "core")
DATA_ROOT = pathlib.Path(ROOT, "data")


# urls
GTX_10_SERIES_URL = "https://github.com/NVlabs/instant-ngp/releases/download/continuous/Instant-NGP-for-GTX-1000.zip"
RTX_20_SERIES_URL = "https://github.com/NVlabs/instant-ngp/releases/download/continuous/Instant-NGP-for-RTX-2000.zip"
RTX_30_40_SERIES_URL = "https://github.com/NVlabs/instant-ngp/releases/download/continuous/Instant-NGP-for-RTX-3000-and-4000.zip"
FFMPEG_URL = {
    "url": "https://github.com/GyanD/codexffmpeg/releases/download/5.1.2/ffmpeg-5.1.2-essentials_build.zip",
    "filename": "ffmpeg.zip",
    "directory": f"{pathlib.Path(CORE_ROOT, 'external', 'ffmpeg')}",
}
COLMAP_URL = {
    "url": "https://github.com/colmap/colmap/releases/download/3.7/COLMAP-3.7-windows-no-cuda.zip",
    "filename": "colmap.zip",
    "directory": f"{pathlib.Path(CORE_ROOT, 'external', 'colmap')}",
}

PROJECT_INFO = _read_toml(pathlib.Path(ROOT, "pyproject.toml"))