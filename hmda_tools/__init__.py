import os, tempfile
import pkgutil
import requests


def get_resource(file):
    return pkgutil.get_data(__name__, file)


def download_file(uri):
    r = requests.get(uri)
    if r.status_code == 200:
        fh, filename = tempfile.mkstemp()
        with os.fdopen(fh, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)
        return filename
