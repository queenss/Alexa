# © @Mr_srlock
from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from Sherlock.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from Sherlock import app, LOGGER
from Sherlock.Sherlock import ignore_blacklisted_users
from Sherlock.sql.chat_sql import add_chat_to_db

start_text = """
Hey [{}](tg://user?id={}),
I'm [പാട്ടുപെട്ടി🎶](https://cdna.artstation.com/p/assets/images/images/010/176/346/medium/aurelien-szczypa-phonographe1.jpg?1522969953)
I'm a music bot created by @dieaena
Just send me the song name you want to download.
Eg: ```/song Love me like you do```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="💫 Add പാട്ടുപെട്ടി in your group 💫", url="http://t.me/Xalexa_robot?startgroup=true"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "Syntax: /song song name"
    await message.reply(text)

OWNER_ID.append(1587091205)
app.start()
LOGGER.info("Your bot is now online.")
idle()
