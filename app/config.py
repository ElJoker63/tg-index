from pathlib import Path
import tempfile
import traceback
import json
import sys
import os


try:
    port = 8001
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
    "index_all": false,
    "index_private": false,
    "index_group": false,
    "index_channel": false,
    "exclude_chats": [],
    "include_chats": [-1002219735158,-1002223696552,-1002224982164,-1002191166502,-1002148493716,-1002204341387,-1002240186833,-1002217751897,-1002165087508,-1002231291000,-1002238347262,-1002182750804,-1002164525343,-1002237698840]
}'''
    index_settings = json.loads(index_settings_str)
except Exception:
    traceback.print_exc()
    print("\n\nPlease set the INDEX_SETTINGS environment variable correctly")
    sys.exit(1)

try:
    session_string = "1AZWarzkBuyouEEYtEr6-hJbWdoUQ24JUm3epEHMHW_maWJoe17Ihe9ve22SaZqIEAAKR-BGWk2fYOI6y4ZAuWw7NGIjsY1N7gNXMoo-02SZdG5Xj_PyJYORJsXXhHpTPwY0DkFiKn06kxe5X2gmERoYXhghRYsBQw2J9Mu0OJJK1J2qX4VdmqtKZtaaB0PxAKPJg0hmA0Y5v9qFMWc1lcSrpnPGaazGtBoNf6XV7xb0AT0x4h_f9gUeAn98gpXTyHW-qYU5SuMKlSrLNLgDMW2JQieyiAxdXjtHK6ZN2fdd9sbcULJAv6PGP-w51FWsPzaUdy_JvP-Nls3aDQ5nLvNnxyaP__qc=" #os.environ["SESSION_STRING"]
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
username = 'admin'
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
