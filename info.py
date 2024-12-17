import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Set Pics
PICS = (environ.get('PICS', 'https://telegra.ph/file/497f21338351cef6cc1fd.jpg https://telegra.ph/file/60ec3a4a522d06b5e4a2c.jpg https://telegra.ph/file/90345e9255d32f5c8ad75.jpg https://telegra.ph/file/e81e25e0c3ee753530c7f.jpg https://telegra.ph/file/41aaa2bc85bad6986641b.jpg https://telegra.ph/file/78f1bd0309d6607dc44fa.jpg https://telegra.ph/file/4e0bbf59af8c55dfce9ff.jpg https://telegra.ph/file/7ae43915facd8eb0a3d00.jpg https://telegra.ph/file/2e91f2168859795bebec1.jpg https://telegra.ph/file/2c91985dd562ea835ef3b.jpg https://telegra.ph/file/daab7f2becc4ddab45586.jpg https://telegra.ph/file/7beda83fbe243952f6768.jpg https://telegra.ph/file/c3fdb36e73269c2e4d629.jpg https://telegra.ph/file/07af4bdb370593909aa51.jpg')).split()
