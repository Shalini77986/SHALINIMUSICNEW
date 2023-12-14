from pyrogram.types import InlineKeyboardButton

import config
from DAXXMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ➕",
                url=f"https://t.me/Shalinixmusicxbot?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✭ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs✭", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✭ ᴜᴘᴅᴀᴛᴇs ✭", url=f"https://t.me/ShaliniMusicBotSh"
            ),
            InlineKeyboardButton(
                text="✭ sᴜᴘᴘᴏʀᴛ ✭", url=f"https://t.me/music_world_sh"
            )
        ],
        [
            InlineKeyboardButton(
                text="✮💞 ᴍᴀɪɴᴛᴀɪɴᴇʀ 💞✮", url=f"https://t.me/shalini_shalu_69"
            )
        ]
     ]
    return buttons
