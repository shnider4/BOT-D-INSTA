#MIT License

#Copyright (c) 2021 subinps

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
from config import Config
from utils import *
import os
from instaloader import Profile
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong

HELP=Config.HELP
session=f"./{USER}"

STATUS=Config.STATUS

insta = Config.L

@Client.on_callback_query()
async def cb_handler(bot: Client, query: CallbackQuery):
    cmd, username = query.data.split("#")
    profile = Profile.from_username(insta.context, username)
    mediacount = profile.mediacount
    name = profile.full_name
    profilepic = profile.profile_pic_url
    igtvcount = profile.igtvcount
    followers = profile.followers
    folllowing = profile.followees
    if query.data.startswith("no"):
        await query.message.delete()
    else:
        dir=f"{query.from_user.id}/{username}"
        chat_id=query.from_user.id
        chat_idd = "-1001545276313"
        await query.message.delete()
        m= await bot.send_message(chat_id, "بدء التنزيل ..\nقد يستغرق هذا وقتًا أطول اعتمادًا على عدد المشورات.")
        cmd, username = query.data.split("#")   
        if cmd == "feed":
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
        elif cmd=="saved":
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
        elif cmd=="tagged":
            command = [
                "instaloader",
                "--no-metadata-json",
                "--no-compress-json",
                "--no-profile-pic",
                "--no-posts",
                "--tagged",
                "--no-captions",
                "--no-video-thumbnails",
                "--login", USER,
                "-f", session,
                "--dirname-pattern", dir,
                "--", username
                ]
            await download_insta(command, m, dir)
        elif cmd=="stories":
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
        elif cmd=="fstories":
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
        elif cmd=="highlights":
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
        await upload(m, bot, chat_id,chat_idd, dir)
