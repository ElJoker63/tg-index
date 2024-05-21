from pathlib import Path
import tempfile
import traceback
import json
import sys
import os


try:
    port = 8000
except Exception as e:
    print(e)
    port = -1
if not 1 <= port <= 65535:
    print(
        "Please make sure the PORT environment variable is an integer between 1 and 65535"
    )
    sys.exit(1)

try:
    api_id = 7684605
    api_hash = "d270d70e8d3c3ad969ea6ecb5857e30b"
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
    index_settings_str = '''{
    "index_all": true,
    "index_private": false,
    "index_group": false,
    "index_channel": true,
    "exclude_chats": [],
    "include_chats": []
}'''
    index_settings = json.loads(index_settings_str)
except Exception:
    traceback.print_exc()
    print("\n\nPlease set the INDEX_SETTINGS environment variable correctly")
    sys.exit(1)

try:
    session_string = os.environ["SESSION_STRING"]
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the SESSION_STRING environment variable correctly")
    sys.exit(1)

host = "0.0.0.0"
debug = False
block_downloads = False
results_per_page = 20
logo_folder = Path(os.path.join(tempfile.gettempdir(), "logo"))
logo_folder.mkdir(parents=True, exist_ok=True)
username = ''
password = ''
SHORT_URL_LEN = int(3)
authenticated = bool(username and password)
SESSION_COOKIE_LIFETIME = int(60)
try:
    SECRET_KEY = ""
    if len(SECRET_KEY) != 32:
        raise ValueError("SECRET_KEY should be exactly 32 charaters long")
except (KeyError, ValueError):
    if authenticated:
        traceback.print_exc()
        print("\n\nPlease set the SECRET_KEY environment variable correctly")
        sys.exit(1)
    else:
        SECRET_KEY = ""
