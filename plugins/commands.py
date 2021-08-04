import re
import asyncio
import sys
import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import *
from instaloader import Profile

from pyrogram import Client, filters
from config import Config

chat_idd = Config.chat_idd
USER = Config.USER
OWNER = Config.OWNER
HOME_TEXT = Config.HOME_TEXT
HOME_TEXT_OWNER = Config.HOME_TEXT_OWNER
HELP = Config.HELP
session = f"./{USER}"

STATUS = Config.STATUS

insta = Config.L
buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("👨🏼‍💻Developer", url='https://t.me/Shnider_Bots'),
            InlineKeyboardButton("🤖Other Bots", url="https://t.me/Shnider_Bots"),

        ],
        [
            InlineKeyboardButton("🔗Source Code", url="https://t.me/Shnider_Bots"),
            InlineKeyboardButton("🧩Deploy Own Bot", url="https://t.me/Shnider_Bots")
        ],
        [
            InlineKeyboardButton("👨🏼‍🦯How To Use?", callback_data="help#subin"),
            InlineKeyboardButton("⚙️Update Channel", url="https://t.me/Shnider_Bots")

        ]

    ]
)


@Client.on_message(filters.command("start") & filters.private)
async def account(bot, message):
    if str(message.from_user.id) != OWNER:
        await message.reply_text(
            HOME_TEXT.format(message.from_user.first_name, message.from_user.id, USER, USER, USER, int(OWNER)),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("👨🏼‍💻Developer", url='https://t.me/Shnider_Bots'),
                        InlineKeyboardButton("🤖Other Bots", url="https://t.me/Shnider_Bots"),

                    ],
                    [
                        InlineKeyboardButton("🔗Source Code", url="https://t.me/Shnider_Bots"),
                        InlineKeyboardButton("🧩Deploy Own Bot", url="https://t.me/Shnider_Bots")
                    ],
                    [
                        InlineKeyboardButton("👨🏼‍🦯How To Use?", callback_data="help#subin"),
                        InlineKeyboardButton("⚙️Update Channel", url="https://t.me/Shnider_Bots")

                    ]

                ]
            )
        )
        return
    if 1 in STATUS:
        m = await message.reply_text("Getting Your data")
        try:
            profile = Profile.own_profile(insta.context)
            mediacount = profile.mediacount
            name = profile.full_name
            bio = profile.biography
            profilepic = profile.profile_pic_url
            username = profile.username
            igtvcount = profile.igtvcount
            followers = profile.followers
            following = profile.followees
            reply_markup = InlineKeyboardMarkup(
                [

                    [

                        InlineKeyboardButton("تحميل المنشورات المحفوضة 📥 ", callback_data=f"saved#{username}")

                    ],
                    [

                        InlineKeyboardButton("                   ", callback_data="0")

                    ],

                ]
            )
            await m.delete()
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=profilepic,
                caption=f"🏷 **Name**: {name}\n🔖 **Username**: {profile.username}\n📝**Bio**: {bio}\n📍 **Account Type**: {acc_type(profile.is_private)}\n🏭 **Is Business Account?**: {yes_or_no(profile.is_business_account)}\n👥 **Total Followers**: {followers}\n👥 **Total Following**: {following}\n📸 **Total Posts**: {mediacount}\n📺 **IGTV Videos**: {igtvcount}",
                reply_markup=reply_markup
            )
        except Exception as e:
            await m.edit(e)

    else:
        await message.reply_text("You must login first by /login")


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


@Client.on_message(filters.command("help") & filters.private)
async def help(bot, cmd):
    await cmd.reply_text(
        HELP,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
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
    )


@Client.on_message(filters.command("restart") & filters.private)
async def stop(bot, cmd):
    if str(cmd.from_user.id) != OWNER:
        await cmd.reply_text(
            HOME_TEXT.format(cmd.from_user.first_name, cmd.from_user.id, USER, USER, USER, OWNER),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
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
        )
        return
    msg = await bot.send_message(
        text="Restarting your bot..",
        chat_id=cmd.from_user.id
    )
    await asyncio.sleep(2)
    await msg.edit("All Processes Stopped and Restarted")
    os.execl(sys.executable, sys.executable, *sys.argv)


@Client.on_message(filters.text & filters.private & filters.incoming)
async def start(bot, cmd):
    text = cmd.text
    if text == "المطور" and str(cmd.from_user.id) != OWNER:
        await cmd.reply_text(
            HOME_TEXT.format(cmd.from_user.first_name, cmd.from_user.id, USER, USER, USER, OWNER),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
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
        )
