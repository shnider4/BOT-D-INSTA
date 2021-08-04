
import pytz
import asyncio
from config import Config
from datetime import datetime
import shutil
import glob
from videoprops import get_audio_properties
from pyrogram.errors import FloodWait
from pyrogram.types import InputMediaPhoto, InputMediaVideo, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
IST = pytz.timezone('Asia/baghdad')
USER=Config.USER
copyright = " 🖤 @BASMYAT_BK"
session=f"./{USER}"

#A function to download content from Instagram
async def download_insta(command, m, dir):
    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    while True:
        output = await process.stdout.readline()
        print("___________")

        if output == b'':
            print("Finished Output")
            break
        if output:
            datetime_ist = datetime.now(IST)
            ISTIME = datetime_ist.strftime("%I:%M:%S %p - %d %B %Y")
            msg="الحالة الحالية ⚙️ : <code>{}</code>\nآخر تحديث :<code>{}</code>".format(output.decode("UTF8"), ISTIME)
            msg=msg.replace(f'{dir}/', 'DOWNLOADED : ')

            try:
                await m.edit(msg)
            except:
                pass
            print(output.decode("UTF8"))
    while True:
        error = await process.stderr.readline()

        if error == b'':
            print("Finished No error")

            break
        if error:
            datetime_ist = datetime.now(IST)
            ISTIME = datetime_ist.strftime("%I:%M:%S %p - %d %B %Y")
            ermsg="ERROR ❌ : <code>{}</code>\nآخر تحديث: <code>{}</code>".format(error.decode("UTF8"), ISTIME)
            try:
                await m.edit(ermsg)
            except:
                pass
            print(error.decode("UTF8"))
    return True


def acc_type(val):
    if(val):
        return "🔒Private🔒"
    else:
        return "🔓Public🔓"

def yes_or_no(val):
    if(val):
        return "Yes"
    else:
        return "No"

#A functionUpload Content to Telegram
async def upload(m, bot, chat_id,chat_idd, dir):

    videos=glob.glob(f"{dir}/*.mp4")
    VDO=[]
    GIF=[]
    
    for video in videos:
        try:
            has_audio = get_audio_properties(video)
            VDO.append(video)
        except Exception as e:
            has_audio=None
            GIF.append(video)
            pass
    PIC=glob.glob(f"{dir}/*.jpg")
    
    print(f"Gif- {GIF}")
    print(f"\n\nVideo - {VDO}")
    print(f"\n\nPictures - {PIC}")


    totalpics=len(PIC)
    totalgif=len(GIF)
    totalvideo=len(VDO)
    TOTAL=totalpics+totalvideo+totalgif
    if TOTAL==0:
        await m.edit("لا يوجد شيء للتنزيل.")
        return
    await m.edit("يتم الآن بدء التحميل إلى Telegram ...")
    await m.pin(disable_notification=False, both_sides=True)



    total=TOTAL
    up=0
    rm=TOTAL

    if totalpics:
        for i in range(0, len(PIC), 2):
            chunk = PIC[i:i + 2]
            print(chunk)
            media = []

            for photo in chunk:
                media.append(InputMediaPhoto(media=photo))
                up+=1
                rm-=1
            try:
                logo = "./logo/1.png"
                media.append(InputMediaPhoto(media=logo, caption=copyright))

                await bot.send_media_group(chat_id=chat_idd, media=media, disable_notification=True)


            except FloodWait as e:
                await asyncio.sleep(e.x)
                await bot.send_media_group(chat_id=chat_id, media=media, disable_notification=True)
            await m.edit(f"مجموع: {total}\nتم الرفع: {up} المتبقي للتحميل: {rm}")

    if totalvideo:
        for i in range(0, len(VDO), 2):
            chunk = VDO[i:i + 2]
            print(chunk)
            media = []
            for video in chunk:
                media.append(InputMediaVideo(media=video))
                up+=1
                rm-=1
            try:
                logo = "./logo/1.png"
                media.append(InputMediaPhoto(media=logo, caption=copyright))
                await bot.send_media_group(chat_id=chat_idd, media=media, disable_notification=True)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await bot.send_media_group(chat_id=chat_idd, media=media, disable_notification=True)
            await m.edit(f"مجموع: {total}\nتم الرفع: {up} المتبقي للتحميل: {rm}")
    if totalgif:
        for gif in GIF:
            try:
                await bot.send_video(chat_id=chat_idd, video=gif,caption=copyright)
                up+=1
                rm-=1
                await m.edit(f"مجموع: {total}\nتم الرفع: {up} المتبقي للتحميل: {rm}")
            except FloodWait as e:
                await bot.send_video(chat_id=chat_idd, video=gif)
                up+=1
                rm-=1
                await m.edit(f"مجموع: {total}\nتم الرفع: {up} المتبقي للتحميل: {rm}")
    await m.unpin()
    await bot.send_message(
        chat_id=chat_id,
        text=f"تم الرفع بنجاح {up}\n\nانضم إلى  قناة المطور وتابع اخر التحديثات  ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
					InlineKeyboardButton("‍💻Developer", url='https://t.me/Shnider_Bots'),

				],
				]
			)
		)
    total=TOTAL
    up=0
    rm=TOTAL
    shutil.rmtree(dir, ignore_errors=True)


