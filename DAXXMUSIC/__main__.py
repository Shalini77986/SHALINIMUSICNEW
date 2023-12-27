import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from DAXXMUSIC import LOGGER, app, userbot
from DAXXMUSIC.core.call import DAXX
from DAXXMUSIC.misc import sudo
from DAXXMUSIC.plugins import ALL_MODULES
from DAXXMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("ᴘʟᴇᴀsᴇ ғɪʟʟ ʏᴏᴜʀ ᴘʏʀᴏɢʀᴀᴍ ᴠ𝟸 sᴛʀɪɴɢ sᴇssɪᴏɴ ᴄᴏʀʀᴇᴄᴛ.")
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
        importlib.import_module("DAXXMUSIC.plugins" + all_module)
    LOGGER("DAXXMUSIC.plugins").info("ᴍʏ ᴀʟʟ ғᴇᴀᴛᴜʀᴇs ʟᴏᴀᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ🎉.")
    await userbot.start()
    await DAXX.start()
    try:
        await DAXX.stream_call("https://telegra.ph/file/5b39f31926e6791b53572.mp4")
    except NoActiveGroupCall:
        LOGGER("DAXXMUSIC").error(
            "ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ʏᴏᴜʀ ʟᴏɢ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀɴᴅ ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ."
        )
        exit()
    except:
        pass
    await DAXX.decorators()
    LOGGER("DAXXMUSIC").info(
        "Cᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs 🎉 ʏᴏᴜʀ ʙᴏᴛ ʜᴀs ʙᴇᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇᴘʟᴏʏᴇᴅ ✅ \n\n ᴍᴀᴅᴇ ʙʏ sʜᴀʟɪɴɪ."
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("DAXXMUSIC").info("ʙᴏᴛ sᴛᴏᴘᴘᴇᴅ 🤧🥹.")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
