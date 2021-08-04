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
You can Download almost anything From your Instagram Account.

<b>What Can Be Downloaded?:</b>

1. All posts of any Profile. (Both Public and Private,for private profiles you need to be a follower.)
2. All Posts from your feed.
3. Stories of any profile (Both Public and Private,for private profiles you need to be a follower.)
4. DP of any profile (No need to follow)
5. Followers and Followees List of any Profile.
6. List of followees who follows back the given username.
7. List of followees who are not following back the given username.
8. Stories of your Followees.
9. Tagged posts of any profile.
10. Your saved Posts.
11. IGTV videos.
12. Highlights from any profiles.
13. Any Public Post from Link(Post/Reels/IGTV)


<b>How to Download:</b>

Its Easy!!
You Need to login into your account by /login. 

You have two Options:

1. From Username:

Just send any instagram username.

For Example:
<code>samantharuthprabhuoffl</code>
<code>subin_p_s_</code>
<code>_chill_manh_7</code>


2. From URL:

You can also sent a post link to download the post or video.

For Example:
<code>https://www.instagram.com/p/CL4QbUiLRNW/?utm_medium=copy_link</code>


<b>Available Commands and Usage</b>

/start - Check wheather bot alive.
/restart - Restart the bot (If you messed up anything use /restart.)
/help - Shows this menu.
/save - post

"""
    HOME_TEXT = """
<b>Helo, [{}](tg://user?id={})

This is a bot of [{}](www.instagram.com/{}) to manage his Instagram account. 
I can only work for my master [{}](tg://user?id={}).
أنا مساعدك لإدارة النشر في قنوات التليكرام 

استخدم  /help في معرفة ما يمكنني فعله من أجلك..

Use /help to know What I can Do?</b>
"""
    HOME_TEXT_OWNER = """
<b>Helo, [{}](tg://user?id={})
أنا مساعدك لإدارة النشر في قنوات التليكرام الخاص بك.

استخدم  /help في معرفة ما يمكنني فعله من أجلك.</b>
"""

