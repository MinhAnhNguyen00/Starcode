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
