import re
from os import environ
from Script import script
# Importation des variables d'environnement
from dotenv import load_dotenv
load_dotenv()

def is_enabled(type, value):
    data = environ.get(type, str(value))
    if data.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif data.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        print(f'Erreur - {type} est invalide, arrêt du programme')
        exit()

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

# Informations du bot
API_ID = environ.get('API_ID', '')
if len(API_ID) == 0:
    print('Erreur - API_ID est manquant, arrêt du programme')
    exit()
else:
    API_ID = int(API_ID)

API_HASH = environ.get('API_HASH', '')
if len(API_HASH) == 0:
    print('Erreur - API_HASH est manquant, arrêt du programme')
    exit()

BOT_TOKEN = environ.get('BOT_TOKEN', '')
if len(BOT_TOKEN) == 0:
    print('Erreur - BOT_TOKEN est manquant, arrêt du programme')
    exit()

PORT = int(environ.get('PORT', '80'))

# Images du bot
PICS = (environ.get('PICS', 'https://telegra.ph/file/58fef5cb458d5b29b0186.jpg https://telegra.ph/file/f0aa4f433132769f8970c.jpg https://telegra.ph/file/f515fbc2084592eca60a5.jpg https://telegra.ph/file/20dbdcffaa89bd3d09a74.jpg https://telegra.ph/file/6045ba953af4def846238.jpg')).split()

# Administrateurs du bot
ADMINS = environ.get('ADMINS', '')
if len(ADMINS) == 0:
    print('Erreur - ADMINS est manquant, arrêt du programme')
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Canaux
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '').split()]
if len(INDEX_CHANNELS) == 0:
    print('Info - INDEX_CHANNELS est vide')

LOG_CHANNEL = environ.get('LOG_CHANNEL', '')
if len(LOG_CHANNEL) == 0:
    print('Erreur - LOG_CHANNEL est manquant, arrêt du programme')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)

# Groupe de support
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '')
if len(SUPPORT_GROUP) == 0:
    print('Erreur - SUPPORT_GROUP est manquant, arrêt du programme')
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)

# Informations MongoDB
DATABASE_URL = environ.get('DATABASE_URL', "")
if len(DATABASE_URL) == 0:
    print('Erreur - DATABASE_URL est manquant, arrêt du programme')
    exit()

DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Liens
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/HA_Bots_Support')
OWNER_USERNAME = environ.get("OWNER_USERNAME", "https://t.me/Hansaka_Anuhas")
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/HA_Bots')
FILMS_LINK = environ.get('FILMS_LINK', 'https://t.me/HA_Films_World')
TUTORIAL = environ.get("TUTORIAL", "https://t.me/HA_Bots")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/HA_Bots")

# Paramètres du bot
DELETE_TIME = int(environ.get('DELETE_TIME', 3600))  # Temps en secondes
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 10))
LANGUAGES = [language.lower() for language in environ.get('LANGUAGES', 'hindi english telugu tamil kannada malayalam marathi punjabi').split()]
QUALITY = [quality.lower() for quality in environ.get('QUALITY', '360p 480p 720p 1080p 2160p').split()]
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "mdiskshortner.link")
SHORTLINK_API = environ.get("SHORTLINK_API", "36f1ae74ba1aa01e5bd73bdd0bc22aa915443501")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 86400))  # Temps en secondes
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]
PM_FILE_DELETE_TIME = int(environ.get('PM_FILE_DELETE_TIME', '3600'))

# Paramètres booléens
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', False)
IS_VERIFY = is_enabled('IS_VERIFY', False)
AUTO_DELETE = is_enabled('AUTO_DELETE', False)
WELCOME = is_enabled('WELCOME', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
LINK_MODE = is_enabled("LINK_MODE", True)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IMDB = is_enabled('IMDB', True)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
SHORTLINK = is_enabled('SHORTLINK', False)

# Informations premium
PAYMENT_QR = environ.get('PAYMENT_QR', 'http://graph.org/file/cacbbea472e5a48ce0d64.jpg')
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'sampleupi@upi')

# Pour le streaming
IS_STREAM = is_enabled('IS_STREAM', True)
BIN_CHANNEL = environ.get("BIN_CHANNEL", "")
if len(BIN_CHANNEL) == 0:
    print('Erreur - BIN_CHANNEL est manquant, arrêt du programme')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)

URL = environ.get("URL", "")
if len(URL) == 0:
    print('Erreur - URL est manquant, arrêt du programme')
    exit()
else:
    if URL.startswith(('https://', 'http://')):
        if not URL.endswith("/"):
            URL += '/'
    elif is_valid_ip(URL):
        URL = f'http://{URL}/'
    else:
        print('Erreur - URL n\'est pas valide, arrêt du programme')
        exit()

# Réactions aux commandes de démarrage
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]  # Ne pas ajouter d'emoji non supporté par Telegram
