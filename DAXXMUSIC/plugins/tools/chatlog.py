import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from DAXXMUSIC import app  

photo = [
    "https://telegra.ph/file/e60ed99da130b0d9bdeb6.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/01165c66137ad2ba1eaf3.jpg",
    "https://telegra.ph/file/5de3dff9397fa19e7b2bb.jpg",
    "https://telegra.ph/file/02adc1d91efa881e2cb95.jpg",
    "https://telegra.ph/file/fd6c30fbd037d330a3f0c.jpg",
    "https://telegra.ph/file/7feaf467e497d1f871f01.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"📝 ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                f"____________________________________\n\n"
                f"📌 ᴄʜᴀᴛ ɴᴀᴍᴇ: {message.chat.title}\n"
                f"🍂 ᴄʜᴀᴛ ɪᴅ: {message.chat.id}\n"
                f"🔐 ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{message.chat.username}\n"
                f"🛰 ᴄʜᴀᴛ ʟɪɴᴋ: [ᴄʟɪᴄᴋ]({link})\n"
                f"📈 ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count}\n"
                f"🤔 ᴀᴅᴅᴇᴅ ʙʏ: {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"sᴇᴇ ɢʀᴏᴜᴘ👀", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>#ʟᴇғᴛ ɢʀᴏᴜᴘ 🥹</u></b> ✫\n\nCʜᴀᴛ Tɪᴛʟᴇ : {title}\n\nCʜᴀᴛ ɪᴅ : {chat_id}\n\nRᴇᴍᴏᴠᴇᴅ ʙʏ: {remove_by}\n\nʙᴏᴛ : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)

#welcome
@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"💓𝗛𝗘𝗟𝗟𝗢 @{member.username} \n\n"
f"🇼 🇪 🇱 🇨 🇴 🇲 🇪 \n"
f"          🇹 🇴               \n"
f"{message.chat.title} 💞\n\n"
f"👀ʏᴏᴜʀ ɴᴀᴍᴇ - {user.mention} \n"
f"😅ʏᴏᴜʀ ɪᴅ -  {member.id}\n\n"
f"ᴀᴘᴋᴇ ᴀɴᴇ sᴇ  {count}  ᴍᴇᴍʙᴇʀs ᴄᴏᴍᴘʟᴇᴛᴇ ʜᴏ ɢᴀʏᴇ ✨\n "
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"💞ᴍᴀɪɴᴛᴀɪɴᴇʀ💞", url=f"tg://openmessage?user_id=6910477574")]
         ]))


