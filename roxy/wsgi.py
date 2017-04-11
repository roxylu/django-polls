#!/bin/env python
import os
import sys

here = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(here)
venv = os.path.join(root, "env")


def setup_env():
    """Setup the environment variables for the WSGI instance"""
    from project.find_settings import find_settings
    os.environ.update({
        "PATH": ":".join([os.environ.get("PATH", ""),
                         os.path.join(venv, "bin")]),
        "PYTHON_EGG_CACHE": os.path.join(root, "run", ".wwweggs"),
        "DJANGO_SETTINGS_MODULE": find_settings(root)
    })


def setup_path():
    """Add the dependencies and project code to the Python path"""
    # Activate the virtualenv...
    activate = os.path.join(venv, "bin", "activate_this.py")
    execfile(activate, dict(__file__=activate))

    # Add working-dir to the path
    sys.path.append(here)


setup_path()
setup_env()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
