import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '7671869618:AAEplVu9irkVnMbc6gCfj_7xJ65wjPhksWA')
    API_ID = int(os.environ.get("API_ID", '29946578'))
    API_HASH = os.environ.get("API_HASH", '57e0b762f105ab1db072fabe4d65114b')
    AUTH_USER = os.environ.get('AUTH_USERS', '6376631545').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "𝗥𝗼𝘆 𝗝𝗮𝗮𝘁™"#Here You Can Change with Your Name  or any custom name or title you prefer
