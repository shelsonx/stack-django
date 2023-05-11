import os
from templateframework.metadata import Metadata

import os

def run(metadata: Metadata = None):
    inputs = metadata.inputs
    path = f"app_django/{inputs['name_project']}/{inputs['name_project']}/settings.py"
    to_find = "django.contrib.staticfiles"
    new = f"{to_find}', \n    '{inputs['name_app']}.apps.{inputs['name_app'].capitalize()}Config"
    with open(path, 'r') as file:
        replaced = file.read().replace(to_find, new)
    with open(path, 'w') as file:
        file.write(replaced)
