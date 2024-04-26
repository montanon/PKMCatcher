import os
from pathlib import Path

from PIL import Image


def rename_samples_files(samples_folder: Path, name_format: str):
    for n, file in enumerate(samples_folder.iterdir()):
        non_num_name = ''.join([c for c in file.name if not c.isdigit()])
        if non_num_name != name_format.replace('{}', ''):
            new_name = name_format.format(n)
            new_path = samples_folder / new_name
            file.rename(new_path)


if __name__ == '__main__':
    samples_folder = Path('./data/samples')
    rename_samples_files(folder=samples_folder, name_format='sample_{}.jpg')
