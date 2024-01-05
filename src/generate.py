from pathlib import Path
from gafferpy.gaffer_connector import GafferConnector
from fishbowl.fishbowl import Fishbowl
import urllib

# Generate the core api using spring-rest as it has access to every store operation
gc = GafferConnector("http://localhost:8080/rest")

generated_dir_path = Path(__file__).parent / "gafferpy/generated_api"

try:
    Fishbowl(gc, generated_directory_path=generated_dir_path)
except urllib.error.URLError:
    print(
        "Unable to connect to running Gaffer API at localhost:8080. Please ensure "
        "this is running before using Fishbowl."
    )
