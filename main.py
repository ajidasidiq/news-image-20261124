#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261124.

Copies the pre-rendered poster (entry.png, built by build_poster.py in
this repository) to /output/entry.png. Standard library only, no network.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), "/output/entry.png")


if __name__ == "__main__":
    main()
