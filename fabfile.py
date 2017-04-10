from fabric.contrib.files import append, exists, sed, put
from fabric.api import env, local, run, sudo

import random
import os
import json

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)


