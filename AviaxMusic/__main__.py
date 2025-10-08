import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from NapsterMusic import LOGGER, app, userbot
from NapsterMusic.core.call import Napster
from NapsterMusic.misc import sudo
from NapsterMusic.plugins import ALL_MODULES
from NapsterMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("NapsterMusic.plugins" + all_module)
    LOGGER("NapsterMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Napster.start()
    try:
        await Napster.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("NapsterMusic").error(
            "Please turn on the videochat of your log group/channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Napster.decorators()
    LOGGER("NapsterMusic").info(
        "Napster Music Started Successfully.\n\nDon't forget to visit @NapsterOfficial"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("NapsterMusic").info("Stopping Napster Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
