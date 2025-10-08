from NapsterMusic.core.bot import Napster
from NapsterMusic.core.dir import dirr
from NapsterMusic.core.git import git
from NapsterMusic.core.userbot import Userbot
from NapsterMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Napster()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

