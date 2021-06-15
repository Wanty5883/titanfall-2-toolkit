# SPL - Standard Python Libraries
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "backend":
    pass
if __name__ == "__main__":
    from lib.core.argparse import argParser
    argParser()
