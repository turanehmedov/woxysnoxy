from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am **{bn}** !!
I let you play music in your group's voice chat ð
The commands I currently support are:
âï¸ /play - __Plays the replied audio file or YouTube video through link.__
âï¸ /pause - __Pause Voice Chat Music.__
âï¸ /resume - __Resume Voice Chat Music.__
âï¸ /skip - __Skips the current Music Playing In Voice Chat.__
âï¸ /stop - __Clears The Queue as well as ends Voice Chat Music.__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sahib ð¬", url="https://t.me/snoxy"
                    ),
                    InlineKeyboardButton(
                        "Ceoð£", url="https://t.me/snoxy"
                    )
                ]
            ]
        )
    )
