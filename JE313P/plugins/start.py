from JE313P import JE313P, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = "https://telegra.ph/file/e5c94b6151f1c00d2f630.jpg""
اهلا بك ! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘انا بوت بسيط لحماية مجموعتك وتشغيل المقاطع الصوتية في المكالمه**.
‣ **استطيع تشغيل المقاطع الصوتية في المكالمة**.
‣ **استطيع حظر و كتم اي مستخدم**.
‣ **افضل بوت من ناحية المميزات**
‣ **يعتمد على مكتبة التيليثون لذلك يكون البوت سريع**!
‣ **اكتشف الباقي بنفسك**.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ اضغط على الاسفل لعرض الاوامر الخاصه بي.
[𖠄 𝑃𝐴𝐵𝐿𝑂 𖠄](https://t.me/KKJTT)
"""

@JE313P.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ اضغط هنا لأضافتي", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("السورس", "https://t.me/KKJTT")],
        [Button.url("الدعم", f"https://t.me/{Config.SUPPORT}"), Button.url("القناة", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("الاوامر", data="help")]])
       return

    if event.is_group:
       await event.reply("**- اهلا بك انا اعمل بنجاح**")
       return



@JE313P.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ اضغط هنا لاضافتي", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("السورس", "https://t.me/KKJTT")],
        [Button.url("الدعم", f"https://t.me/{Config.SUPPORT}"), Button.url("القناة", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("الاوامر", data="help")]])
       return
