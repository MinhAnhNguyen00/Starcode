import matplotlib
import os

from traitlets.config import get_config

# load Jupyter config file
c = get_config()

# add static path for css
c.NotebookApp.extra_static_paths = [os.path.join(os.getcwd(), '.binder', 'custom')]

# Matplotlib backend setup
matplotlib.use("agg")
