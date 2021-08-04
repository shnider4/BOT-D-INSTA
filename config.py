import os
from instaloader import Instaloader
class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    USER = os.environ.get("INSTAGRAM_USERNAME", "")
    OWNER = os.environ.get("OWNER_ID", "")
    INSTA_SESSIONFILE_ID = os.environ.get("INSTA_SESSIONFILE_ID", None)
    chat_idd = os.environ.get("CHANNEL_ID", "")
    S = "0"
    STATUS = set(int(x) for x in (S).split())
    L=Instaloader()
    HELP="""
<b>أنا مساعد لإدارة النشر في قنوات التليكرام :</b>

<b>الاوامر </b>

/start - Check  bot alive.
/restart - Restart the bot 
/help - Shows this menu.
/save - post

"""
    HOME_TEXT = """
<b>Helo, [{}](tg://user?id={})

This is a bot of [{}](www.instagram.com/{}) to manage . 
I can only work for my master [{}](tg://user?id={}).
أنا مساعد لإدارة النشر في قنوات التليكرام 

استخدم  /help في معرفة ما يمكنني فعله من أجلك..

Use /help to know What I can Do?</b>
"""
    HOME_TEXT_OWNER = """
<b>Helo, [{}](tg://user?id={})
أنا مساعدك لإدارة النشر في قنوات التليكرام الخاص بك.

استخدم  /help في معرفة ما يمكنني فعله من أجلك.</b>
"""


