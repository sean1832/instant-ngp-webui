import os
import pathlib
import shutil
import zipfile

import requests


def download_file(file_url, output_directory, new_filename=None):
    file_name = pathlib.Path(output_directory, file_url.split("/")[-1])
    try:
        with requests.get(file_url, stream=True) as response:
            response.raise_for_status()  # Check if the request was successful
            with open(file_name, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

        if new_filename is not None:
            file_name.rename(new_filename)
            file_name = new_filename

        print(f"File has been downloaded to {file_name}.")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return 1, None
    return 0, file_name


def extract_zip(file_path, output_directory):
    try:
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(output_directory)
        print(f"Files have been extracted to {output_directory}")
    except zipfile.BadZipFile as e:
        print(f"Error occurred: {e}")
        return 1
    return 0


def move_files_to_dir(src_dir, dst_dir):
    for file in src_dir.iterdir():
        shutil.move(str(file), dst_dir)


def download_and_extract(url: str, directory: str, filename: str):
    print(f"Downloading from {url}...")
    os.makedirs(directory, exist_ok=True)
    _, downloaded_filename = download_file(url, directory, filename)

    if downloaded_filename is None:
        return

    print(f"Extracting {downloaded_filename} to {directory}")
    extract_zip(downloaded_filename, directory)

    # remove zip file
    print(f"Cleanup: removing {downloaded_filename}")
    os.remove(str(downloaded_filename))
