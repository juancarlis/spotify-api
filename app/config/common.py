"""To load config into __config variable.

This is used to avoid loading several times the file.
"""
import yaml

__config = None


def config():

    global __config

    if not __config:
        with open('config/config.yaml', mode='r') as f:
            __config = yaml.safe_load(f)

    return __config
