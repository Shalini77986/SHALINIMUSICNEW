from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from DAXXMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from strings import get_command
SHALINI_PICS = [
"https://telegra.ph/file/2e85d11aefdf6cd01301b.jpg",
"https://telegra.ph/file/0a08b180583f13952336a.jpg",
"https://telegra.ph/file/ace92d59d19127d2d4e89.jpg",
"https://telegra.ph/file/bb0a28259990c6a978985.jpg",
"https://telegra.ph/file/ace92d59d19127d2d4e89.jpg",
"https://telegra.ph/file/a0db46dfacd94e489117b.jpg",
"https://telegra.ph/file/cd77be2595cdc2fca60a3.jpg",
"https://telegra.ph/file/632724b3d30c691247c77.jpg",
"https://telegra.ph/file/a2d01afe4f2cb1d4b650c.jpg",
"https://telegra.ph/file/94dc035df11dfb159b999.jpg",
"https://telegra.ph/file/fed9a5b1cbaaefc3a818c.jpg",
"https://telegra.ph/file/66fd03632cbb38bdb4193.jpg"
]


@app.on_message(filters.command(["owner"]) & filters.private & ~BANNED_USERS & ~filters.edited)
@LanguageStart
async def str(client, message: Message, _):
    await message.reply_photo(
        random.choice(SHALINI_PICS),
      caption=f"""꧁💓✨ Cʅιƈƙ Bҽʅσɯ Bυƚƚσɳ Tσ Dɱ Mყ Oɯɳҽɾ ✨💓꧂""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫 ƈʟɨƈӄ ɦɛʀɛ 💫", url=f"https://t.me/shalini_shalu_69")
                ]
            ]
        ),
               )
