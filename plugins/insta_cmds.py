import asyncio
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from instaloader import Profile
from utils import *
import datetime
now = datetime.datetime.now().time()
chat_idd = Config.chat_idd
USER = Config.USER
OWNER = Config.OWNER
HOME_TEXT_OWNER = Config.HOME_TEXT_OWNER
HELP = Config.HELP
HOME_TEXT = Config.HOME_TEXT
session = f"./{USER}"
STATUS = Config.STATUS

insta = Config.L
buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("👨🏼‍💻Developer", url='https://t.me/Shnider_Bots'),
            InlineKeyboardButton("🤖Other Bots", url="https://t.me/Shnider_Bots")
        ],
        [
            
            InlineKeyboardButton("⚙️Update Channel", url="https://t.me/Shnider_Bots")
        ]

    ]
)


@Client.on_message(filters.command("feed") & filters.private)
async def feed(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, OWNER),
            reply_markup=buttons,
            disable_web_page_preview=True
        )
        return
    text = message.text
    username = USER
    count = None
    if " " in text:
        cmd, count = text.split(' ')
    if 1 not in STATUS:
        await message.reply_text("You Must Login First /login ")
        return
    m = await message.reply_text(f"Fetching Posts in Your Feed.")
    chat_id = message.from_user.id
    chat_idd
    dir = f"{chat_id}/{username}"
    await m.edit("Starting Downloading..\nThis may take longer time Depending upon number of posts.")
    if count:
        command = [
            "instaloader",
            "--no-metadata-json",
            "--no-compress-json",
            "--no-profile-pic",
            "--no-posts",
            "--no-captions",
            "--no-video-thumbnails",
            "--login", USER,
            "--sessionfile", session,
            "--dirname-pattern", dir,
            ":feed",
            "--count", count
        ]
    else:
        command = [
            "instaloader",
            "--no-metadata-json",
            "--no-compress-json",
            "--no-profile-pic",
            "--no-posts",
            "--no-captions",
            "--no-video-thumbnails",
            "--login", USER,
            "--sessionfile", session,
            "--dirname-pattern", dir,
            ":feed"
        ]

    await download_insta(command, m, dir)
    await upload(m, bot, chat_id, chat_idd, dir)


@Client.on_message(filters.command("saved") & filters.private)
async def saved(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, OWNER),
            reply_markup=buttons,
            disable_web_page_preview=True
        )
        return
    text = message.text
    username = USER

    if 1 not in STATUS:
        await message.reply_text("يجب عليك تسجيل الدخول أولا / تسجيل الدخول")
        return
    count = None
    if " " in text:
        cmd, count = text.split(' ')
    m = await message.reply_text(f"جاري تنزيل المحفوضات 🔃 .")
    chat_id = message.from_user.id
    dir = f"{chat_id}/{username}"
    await m.edit("بدء التنزيل ..\nقد يستغرق هذا وقتًا أطول اعتمادًا على عدد المنشورات ✅✅ .")
    if count:
        command = [
            "instaloader",
            "--no-metadata-json",
            "--no-compress-json",
            "--no-profile-pic",
            "--no-posts",
            "--no-captions",
            "--no-video-thumbnails",
            "--login", USER,
            "-f", session,
            "--dirname-pattern", dir,
            ":saved",
            "--count", count
        ]
    else:
        command = [
            "instaloader",
            "--no-metadata-json",
            "--no-compress-json",
            "--no-profile-pic",
            "--no-posts",
            "--no-captions",
            "--no-video-thumbnails",
            "--login", USER,
            "-f", session,
            "--dirname-pattern", dir,
            ":saved"
        ]
    await download_insta(command, m, dir)
    await upload(m, bot, chat_id, chat_idd, dir)


@Client.on_message(filters.command("story") & filters.private)
async def story(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, OWNER),
            reply_markup=buttons,
            disable_web_page_preview=True
        )
        return
    text = message.text
    username = USER

    if 1 not in STATUS:
        await message.reply_text("You Must Login First /login ")
        return
    if " " in text:
        cmd, username = text.split(' ')
        profile = Profile.from_username(insta.context, username)
        is_followed = yes_or_no(profile.followed_by_viewer)
        type = acc_type(profile.is_private)
        if type == "🔒Private🔒" and is_followed == "No":
            await message.reply_text(
                "Sorry!\nI can't fetch details from that account.\nSince its a Private account and you are not following <code>@{username}</code>.")
            return
    m = await message.reply_text(f"Fetching stories of <code>@{username}</code>")
    chat_id = message.from_user.id
    dir = f"{chat_id}/{username}"
    await m.edit("Starting Downloading..\nThis may take longer time Depending upon number of posts.")
    command = [
        "instaloader",
        "--no-metadata-json",
        "--no-compress-json",
        "--no-profile-pic",
        "--no-posts",
        "--stories",
        "--no-captions",
        "--no-video-thumbnails",
        "--login", USER,
        "-f", session,
        "--dirname-pattern", dir,
        "--", username
    ]
    await download_insta(command, m, dir)
    await upload(m, bot, chat_id, chat_idd, dir)


@Client.on_message(filters.command("stories") & filters.private)
async def stories(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, OWNER),
            reply_markup=buttons,
            disable_web_page_preview=True
        )
        return
    username = USER
    if 1 not in STATUS:
        await message.reply_text("You Must Login First /login ")
        return
    m = await message.reply_text(f"Fetching stories of all your followees")
    chat_id = message.from_user.id
    chat_idd = "-1001545276313"
    dir = f"{chat_id}/{username}"
    await m.edit("Starting Downloading..\nThis may take longer time Depending upon number of posts.")
    command = [
        "instaloader",
        "--no-metadata-json",
        "--no-compress-json",
        "--no-profile-pic",
        "--no-captions",
        "--no-posts",
        "--no-video-thumbnails",
        "--login", USER,
        "-f", session,
        "--dirname-pattern", dir,
        ":stories"
    ]
    await download_insta(command, m, dir)
    await upload(m, bot, chat_id, chat_idd, dir)


@Client.on_message(filters.command("highlights") & filters.private)
async def highlights(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, OWNER),
            reply_markup=buttons,
            disable_web_page_preview=True
        )
        return
    username = USER
    if 1 not in STATUS:
        await message.reply_text("You Must Login First /login ")
        return
    text = message.text
    if " " in text:
        cmd, username = text.split(' ')
        profile = Profile.from_username(insta.context, username)
        is_followed = yes_or_no(profile.followed_by_viewer)
        type = acc_type(profile.is_private)
        if type == "🔒Private🔒" and is_followed == "No":
            await message.reply_text(
                "Sorry!\nI can't fetch details from that account.\nSince its a Private account and you are not following <code>@{username}</code>.")
            return
    m = await message.reply_text(f"Fetching highlights from profile <code>@{username}</code>")
    chat_id = message.from_user.id

    dir = f"{chat_id}/{username}"
    await m.edit("Starting Downloading..\nThis may take longer time Depending upon number of posts.")
    command = [
        "instaloader",
        "--no-metadata-json",
        "--no-compress-json",
        "--no-profile-pic",
        "--no-posts",
        "--highlights",
        "--no-captions",
        "--no-video-thumbnails",
        "--login", USER,
        "-f", session,
        "--dirname-pattern", dir,
        "--", username
    ]
    await download_insta(command, m, dir)
    await upload(m, bot, chat_id, chat_idd, dir)



