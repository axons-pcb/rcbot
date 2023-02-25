
# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1814992141:AAFxYGNZwYHXzOJbN0mJE76e6zVaKIvhXKQ"
    OWNER_ID = "584261126"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "drpratyash"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mVKLoF7HWPFsoLGzx28q@containers-us-west-104.railway.app:6467/railway'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'sed']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    MAPS_API = ''
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_ANTISPAM = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    STRICT_GBAN = False
    STRICT_GMUTE = False
    ALLOW_EXCL = True  # Allow ! commands as well as /
    API_OPENWEATHER = None # OpenWeather API

    # MEMES
    DEEPFRY_TOKEN = None
    FIREFOX_BIN=/usr/lib/firefox
    GECKODRIVER_PATH=/app/vendor/geckodriver/geckodriver
    LD_LIBRARY_PATH=/usr/local/lib:/usr/lib:/lib:/app/vendor
    MESSAGE_DUMP=-1001554942558
    PORT=8443
    STRICT_GBAN=True
    SUDO_USERS=584261126
    SUPPORT_USERS=584261126
    WHITELIST_USERS=584261126

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
