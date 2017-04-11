def find_settings(root):
    """Find the import path to this host's settings module"""
    import os
    fpath = os.path.join(root, ".settings")

    with open(fpath) as f:
        settings = f.read().strip()

    if not settings:
        raise IOError("%s is empty" % fpath)
    return settings
