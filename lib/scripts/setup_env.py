import matplotlib
import os

from traitlets.config import get_config

# load Jupyter config
c = get_config()

c.NotebookApp.extra_static_paths = [os.getcwd(), '.binder', 'custom']

# Matplotlib setup
matplotlib.use("agg")
