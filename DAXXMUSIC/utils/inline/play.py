import math
from config import SUPPORT_CHAT, OWNER_USERNAME
from pyrogram.types import InlineKeyboardButton
from DAXXMUSIC import app
from DAXXMUSIC.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    elif 2 < umm < 3:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 3 <= umm < 4:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 4 <= umm < 5:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 6 <= umm < 7:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 7 <= umm < 8:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 9 <= umm < 10:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 11 <= umm < 12:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 12 <= umm < 13:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 13 < umm < 14:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 14 <= umm < 15:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 15 <= umm < 16:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 16 <= umm < 17:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 17 <= umm < 18:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 18 <= umm < 19:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 19 <= umm < 20:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 20 <= umm < 21:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 21 <= umm < 22:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 22 <= umm < 23:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 23 <= vip < 24:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 24 <= vip < 25:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 25 <= vip < 26:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 26 <= vip < 27:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 27 <= vip < 28:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 28 <= vip < 29:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 29 <= vip < 30:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 30 <= vip < 31:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 31 <= vip < 32:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 32 <= vip < 33:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 33 <= vip < 34:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 34 <= vip < 35:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 35 <= vip < 36:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 36 <= vip < 37:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 37 <= vip < 38:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 38 <= vip < 39:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 39 <= vip < 40:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 40 <= vip < 41:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 41 <= vip < 42:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 42 <= vip < 43:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 43 <= vip < 44:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 44 < vip < 45:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 45 <= vip < 46:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 46 <= vip < 47:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 47 <= vip < 48:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 48 <= vip < 49:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 49 <= vip < 50:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 50 <= vip < 51:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 51 <= vip < 52:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 52 <= vip < 53:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 53 <= vip < 54:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 54 <= vip < 55:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 55 <= vip < 56:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 56 <= vip < 57:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 57 <= vip < 58:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 58 <= vip < 59:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 59 <= vip < 60:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 60 <= vip < 61:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 61 <= vip < 62:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 62 <= vip < 63:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 63 <= vip < 64:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 64 <= vip < 65:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 65 <= vip < 66:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 66 <= vip < 67:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 67 <= vip < 68:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 68 <= vip < 69:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 69 <= vip < 70:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 70 <= vip < 71:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 71 <= vip < 72:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 72 <= vip < 73:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 73 <= vip < 74:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 74 <= vip < 75:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 75 <= vip < 76:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 76 <= vip < 77:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 77 <= vip < 78:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 78 <= vip < 79:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 79 <= vip < 80:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 80 <= vip < 81:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 81 <= vip < 82:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 82 <= vip < 83:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 83 <= vip < 84:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 84 <= vip < 85:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 85 <= vip < 86:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 86 <= vip < 87:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 87 <= vip < 88:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 88 <= vip < 89:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 89 <= vip < 90:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 90 <= vip < 91:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 91 <= vip < 92:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 92 <= vip < 93:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 93 <= vip < 94:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 94 <= vip < 95:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    elif 95 <= vip < 96:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 96 <= vip < 97:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 97 <= vip < 98:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩ♡ﮩ٨ـ"
    elif 98 <= vip < 99:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ"
    else:
        bar = "ﮩ٨ـﮩ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
        
    buttons = [
                [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
InlineKeyboardButton(text="ᴘᴀᴜꜱᴇ", callback_data=f"ADMIN Pause|{chat_id}"),
InlineKeyboardButton(text="ʀᴇꜱᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"),
InlineKeyboardButton(text="ꜱᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"),
InlineKeyboardButton(text="ꜱᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
                 [
            InlineKeyboardButton(

                text="💕ᴍᴀɪɴᴛᴀɪɴᴇʀ 💕",

                url=f"tg://openmessage?user_id=6910477574",

            ),
            InlineKeyboardButton(

                text="🎏ɢʀᴏᴜᴘ🎏",

                url=f"{SUPPORT_CHAT}",

            ),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
InlineKeyboardButton(text="ᴘᴀᴜꜱᴇ", callback_data=f"ADMIN Pause|{chat_id}"),
InlineKeyboardButton(text="ʀᴇꜱᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"),
InlineKeyboardButton(text="ꜱᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"),
InlineKeyboardButton(text="ꜱᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
                 [
            InlineKeyboardButton(

                text="💕ᴍᴀɪɴᴛᴀɪɴᴇʀ 💕",

                url=f"t.me/{OWNER_USERNAME}",

            ),
            InlineKeyboardButton(

                text="🎏ɢʀᴏᴜᴘ🎏",

                url=f"{SUPPORT_CHAT}",

            ),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"DAXXPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"DAXXPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
