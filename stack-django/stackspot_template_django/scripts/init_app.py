import os
from templateframework.metadata import Metadata

import os

def run(metadata: Metadata = None):
    inputs = metadata.inputs
    os.system(f'cd app_django/{inputs["name_project"]} && \
        python3 manage.py startapp {inputs["name_app"]} && \
        touch {inputs["name_app"]}/urls.py')