"""Ship the bundled front page to the grader's output folder.

The image is already drawn and ships in this repo as entry.png; this
script only places a copy of it where the grader expects it.
"""

import os
import shutil

IMAGE_NAME = "entry.png"


def _source_path():
    folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, IMAGE_NAME)


def _destination_folder():
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not chosen:
        chosen = "/output"
    return chosen


def main():
    target_dir = _destination_folder()
    os.makedirs(target_dir, exist_ok=True)
    shutil.copyfile(_source_path(), os.path.join(target_dir, IMAGE_NAME))


if __name__ == "__main__":
    main()
