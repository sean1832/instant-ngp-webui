import os
import pathlib
import shutil
import subprocess

from common import constants as const
from scripts import utilities


def download_latest():
    print("Select type of Nvidia graphics card you have:")
    print("[1] RTX 40 or 30 Series")
    print("[2] RTX 20 Series")
    print("[3] GTX 10 Series")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print(f"Downloading {const.RTX_30_40_SERIES_URL} to {const.CORE_ROOT}")
                _, filename = utilities.download_file(
                    const.RTX_30_40_SERIES_URL, const.CORE_ROOT
                )
                break
            elif choice == 2:
                print(f"Downloading {const.RTX_20_SERIES_URL} to {const.CORE_ROOT}")
                _, filename = utilities.download_file(
                    const.RTX_20_SERIES_URL, const.CORE_ROOT
                )
                break
            elif choice == 3:
                print(f"Downloading {const.GTX_10_SERIES_URL} to {const.CORE_ROOT}")
                _, filename = utilities.download_file(
                    const.GTX_10_SERIES_URL, const.CORE_ROOT
                )
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice. Please try again.")
    print("Done!\n")

    if filename is None:
        return

    print(f"Extracting {filename} to {const.CORE_ROOT}")
    utilities.extract_zip(filename, const.CORE_ROOT)
    # remove zip file
    os.remove(str(filename))

    dirname = filename.stem

    # move files to core directory
    print("Moving files to core directory...")
    utilities.move_files_to_dir(
        pathlib.Path(const.CORE_ROOT, str(dirname)), const.CORE_ROOT
    )
    # remove directory
    shutil.rmtree(pathlib.Path(const.CORE_ROOT, str(dirname)))

    print("Done!\n")


if __name__ == "__main__":
    # check if core directory is empty
    if not const.CORE_ROOT.exists() or not any(const.CORE_ROOT.iterdir()):
        print("Core directory is empty. Downloading latest version of Instant NGP...")
        os.makedirs(const.CORE_ROOT, exist_ok=True)
        download_latest()
    else:
        answer = input(
            "Core directory is not empty. Do you want to overwrite it? [y/n]"
        )
        if answer.lower() == "y":
            print("Downloading latest version of Instant NGP...")
            # remove all files in core directory
            shutil.rmtree(const.CORE_ROOT)
            os.makedirs(const.CORE_ROOT, exist_ok=True)
            download_latest()
        else:
            print("Abort.")

    # install dependencies for Instant NGP
    print("Installing dependencies...")
    subprocess.run(["pip", "install", "-r", f"{const.CORE_ROOT}/requirements.txt"])

    # install ffmpeg
    print("Installing ffmpeg...")
    utilities.download_and_extract(
        const.FFMPEG_URL["url"],
        const.FFMPEG_URL["directory"],
        const.FFMPEG_URL["filename"],
    )
    print("Done!\n")

    # install colmap
    print("Installing colmap...")
    utilities.download_and_extract(
        const.COLMAP_URL["url"],
        const.COLMAP_URL["directory"],
        const.COLMAP_URL["filename"],
    )
    print("Done!\n")
