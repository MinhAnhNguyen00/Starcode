import subprocess
import time

import matplotlib
import os

from traitlets.config import get_config

# load Jupyter config file and setup custom css
c = get_config()

css_path = os.path.join(os.getcwd(), '.binder', 'custom', 'custom.css')
if not os.path.exists(css_path):
    raise FileNotFoundError(f'Custom CSS file not found at {css_path}')

c.NotebookApp.extra_static_paths = [os.path.join(os.getcwd(), '.binder', 'custom')]
c.NotebookApp.custom_display_url = '/static/custom/custom.css'

# Matplotlib backend setup
matplotlib.use('agg')

# restart jupyter lab to reload css
print("checking if jupyterlab is running...")

try:
    # find the process if it exists
    process_output = subprocess.check_output("pgrep -f jupyter-lab", shell=True, text=True)
    pids = process_output.strip().split("\n")

    if pids:
        print(f"jupyterlab is running with pid(s): {pids}, stopping it now...")
        os.system("pkill -f jupyter-lab")  # terminate only relevant processes
        time.sleep(2)  # wait to ensure it is fully stopped
    else:
        print("jupyterlab was not active, no restart needed.")
except subprocess.CalledProcessError:
    print("no running jupyterlab process found.")

# restart jupyterlab
print("starting jupyterlab...")
os.system("nohup jupyter-lab --no-browser --port=8888 > /dev/null 2>&1 &")
