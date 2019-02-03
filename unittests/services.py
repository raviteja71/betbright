# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests

def get_todos():
    response = requests.get("http://localhost:5000/api/match/1")
    if response.ok:
        return response
    else:
        return None