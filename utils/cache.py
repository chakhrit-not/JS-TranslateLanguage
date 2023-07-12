

def makedirs(path: str, exist_ok=False):

    import os

    dir = os.path.dirname(path)

    if not os.path.exists(dir):

        os.makedirs(dir, exist_ok=exist_ok)