import time
import inspect
import copy
from collections import deque

def merge_config(new_config, old_config):
    """Merge the user-defined config with default config"""
    config = copy.deepcopy(old_config)
    if new_config is not None:
        config.update(new_config)
    return config

def wait(sleep=0.2):
    time.sleep(sleep)