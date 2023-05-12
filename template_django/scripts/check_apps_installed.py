import subprocess
from templateframework.metadata import Metadata
import os

MESSAGE = 'echo Installing apps:'

def check_install(app_check, install_app):
    try:
        output = subprocess.Popen(
            app_check, 
            stdout=subprocess.PIPE).communicate()[0]
        print(output.decode('utf-8'))
    except Exception:
        os.system(MESSAGE)
        os.system(install_app)

def check_system(sys_check):
    output = None
    try:
        output = subprocess.Popen(
            sys_check, 
            stdout=subprocess.PIPE).communicate()[0]
        print(output.decode('utf-8'))
    except Exception:
        pass
    finally:
        return output

def install_mac():
    check_install(['python', '--version'], 'brew install python3')
    check_install(['django-admin', '--version'], 'pip3 install Django')

def install_linux():
    check_install(['python', '--version'], 'sudo apt install python3')
    check_install(['django-admin', '--version'], 'pip3 install python3-django')

CHECK_MAC_VERSION = 'sw_vers'
CHECK_LINUX_VERSION = 'hostnamectl'

def run(metadata: Metadata = None):
    if (check_system(CHECK_MAC_VERSION)):
        install_mac()
    elif (check_system(CHECK_LINUX_VERSION)):
        install_linux()
