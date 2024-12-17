import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Set Pics
PICS = (environ.get('PICS',  '')).split()
# Messages
default_start_msg = """
**Hi, I'm bot """
START_MSG = environ.get('START_MSG', default_start_msg)

