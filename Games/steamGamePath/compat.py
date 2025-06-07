"""
Finds and returns paths to the compatibility folder for each appID
"""

import os


def fetch_compat_dir(app_id, path):
    """Fetches the compatibility directory for a given appID and path"""
    compat_dir = os.path.join(path, "steamapps/compatdata", str(app_id))
    return compat_dir
