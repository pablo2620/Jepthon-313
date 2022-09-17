import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/b4cac03a1c92944856184.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@KKJTT"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/بنك"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/KKJTT")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
