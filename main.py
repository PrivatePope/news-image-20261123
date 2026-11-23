import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
IMAGE = os.path.join(BASE, "entry.png")
TARGET = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

if not os.path.isfile(IMAGE):
    raise SystemExit("entry.png missing next to main.py")

os.makedirs(TARGET, exist_ok=True)
shutil.copyfile(IMAGE, os.path.join(TARGET, "entry.png"))
