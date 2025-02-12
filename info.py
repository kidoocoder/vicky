import os
import time

class Config(object):
    # Pyrogram Client
    API_ID    = int(os.environ.get("API_ID", "21803165"))  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "05e5e695feb30e25bef47484cc006da7") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7711451543:AAEcgbrmckS0xZv4WbVX-4GdyIircl870") # ⚠️ Required
    
    # Other Configs
    BOT_START_TIME = time.time()
    OWNER    = int(os.environ.get("OWNER", "673088758"))  # ⚠️ Required
    SUDO = list(map(int, os.environ.get("SUDO", "673082758").split()))  # ⚠️ Required
    # Web Response Config
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))

class Txt(object):

    SEND_NUMBERS_MSG = """
**❪ 𝖲ᴇɴᴅ 𝖳ʜᴇ 𝖳ᴏᴛᴀʟ 𝖭ᴜᴍʙᴇʀ 𝖸ᴏᴜ 𝖧ᴀᴠᴇ ❫**

**☛ ʜᴏᴡ ᴍᴀɴʏ ɴᴜᴍʙᴇʀ ᴅᴏ ʏᴏᴜ ʜᴀᴠᴇ.**
"""

    SEND_TARGET_CHANNEL = """
**❪ 𝖲ᴇɴᴅ 𝖳ʜᴇ 𝖳ᴀʀɢᴇᴛ 𝖢ʜᴀɴɴᴇʟ 𝖫ɪɴᴋ ᴏʀ 𝖴sᴇʀɴᴀᴍᴇ ❫**

**☛ 𝖥ᴏʀ 𝖤xᴀᴍᴘʟᴇ:- <code> ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ </code> ᴏʀ <code> ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ </code>**
"""

    SEND_SESSION_MSG = """
**❪ 𝖲ᴇɴᴅ 𝖲ᴛʀɪɴɢ 𝖲ᴇssɪᴏɴ ❫**

**☛ 𝖦ᴇɴᴇʀᴀᴛᴇ 𝖲ᴛʀɪɴɢ 𝖲ᴇssɪᴏɴ 𝖥ᴏʀᴍ <a href=t.me/king_string_session_bot>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>**


"""

    SEND_API_ID = """
**❪ Sᴇɴᴅ ᴀᴘɪ ɪᴅ ❫**

☛ Api_id ɢᴇᴛ ғʀᴏᴍ my.telegram.org**
"""
    SEND_API_HASH = """
**❪ Sᴇɴᴅ ᴀᴘɪ ʜᴀsʜ ❫**

**☛ Api_hash ɢᴇᴛ ғʀᴏᴍ my.telegram.org**
"""

    MAKE_CONFIG_DONE_MSG = """
**Yᴏᴜʀ {} ᴀᴄᴄᴏᴜɴᴛs ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ 👥**

**Aɴᴅ Lᴏɢɪɴᴇᴅ ᴛᴏ ᴛʜᴇ Tᴀʀɢᴇᴛ Cʜᴀɴɴᴇʟ/Gʀᴏᴜᴘ ᴛᴏ Rᴇᴘᴏʀᴛ ɪᴛ. ✅**

**➜ Cʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟʟᴏᴡ ᴛᴏ sᴇᴇ ᴛʜᴇ Nᴜᴍʙᴇʀ ᴏғ Tᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ ʏᴏᴜ ᴀᴅᴅᴇᴅ..**
"""

    ADDED_ACCOUNT = """
**Yᴏᴜʀ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ {} ᴀᴄᴄᴏᴜɴᴛs 👥**

**➜ Cʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟʟᴏᴡ ᴛᴏ sᴇᴇ ᴛʜᴇ Mᴏʀᴇ Iɴғᴏ ᴏғ ᴛʜᴇ Tᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛs ᴡʜɪᴄʜ ʏᴏᴜ ʜᴀᴠᴇᴅ ᴀᴅᴅᴇᴅ.**
"""

    ACCOUNT_INFO = """
<b> Nᴀᴍᴇ :- </b> <code> {0} </code>
<b> Usᴇʀ ɪᴅ :- </b> <code> {1} </code>
"""

    REPORT_CHOICE = """
**❪ 𝐒ᴇʟᴇᴄᴛ 𝐑ᴇᴀsᴏɴ 𝐅ᴏʀ 𝐑ᴇᴘᴏʀᴛ 👤 ❫**

**𝟷. 𝐑ᴇᴘᴏʀᴛ ғᴏʀ ᴄʜɪʟᴅ ᴀʙᴜsᴇ**
**𝟸. 𝐑ᴇᴘᴏʀᴛ ғᴏʀ ᴄᴏᴘʏʀɪɢʜᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ**
**𝟹. 𝐑ᴇᴘᴏʀᴛ ғᴏʀ ɪᴍᴘᴇʀsᴏɴᴀᴛɪᴏɴ**
**𝟺. 𝐑ᴇᴘᴏʀᴛ ᴀɴ ɪʀʀᴇʟᴇᴠᴀɴᴛ ɢᴇᴏɢʀᴏᴜᴘ**
**𝟻. 𝐑ᴇᴘᴏʀᴛ ᴀɴ ɪʟʟᴇɢᴀʟ ᴅʀᴜɢ**
**𝟼. 𝐑ᴇᴘᴏʀᴛ ғᴏʀ Vɪᴏʟᴇɴᴄᴇ**
**𝟽. 𝐑ᴇᴘᴏʀᴛ ғᴏʀ ᴏғғᴇɴsɪᴠᴇ ᴘᴇʀsᴏɴ ᴅᴇᴛᴀɪʟ**
**𝟾. 𝐑ᴇᴀsᴏɴ ғᴏʀ Pᴏʀɴᴏɢʀᴀᴘʜʏ**
**𝟿. 𝐑ᴇᴘᴏʀᴛ ғᴏʀ sᴘᴀᴍ**

**Wʜᴀᴛs ʏᴏᴜʀ  ʀᴇᴀsᴏɴ: sᴇʟᴇᴄᴛ 𝟷-𝟿 👇**
"""

    SEND_NO_OF_REPORT_MSG = """
**❪ 𝐒ᴇʟᴇᴄᴛ 𝐍ᴜᴍʙᴇʀ 𝐎ғ 𝐑ᴇᴘᴏʀᴛs 👤 ❫**

**Sᴇɴᴅ Nᴜᴍʙᴇʀ ᴏғ ʀᴇᴘᴏʀᴛs ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴛʜɪs @{}**

**Tʜᴇ ʙᴏᴛ ᴡɪʟʟ ᴋᴇᴇᴘ ʀᴇᴘᴏʀᴛɪɴɢ ᴛᴏ ᴛᴀʀɢᴇᴛ ᴄʜᴀɴɴᴇʟ ᴏʀ ɢʀᴏᴜᴘ ᴜɴᴛɪʟ ɪᴛ's ʀᴇᴀᴄʜ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴏғ ʀᴇᴘᴏʀᴛ.** 🎯
"""

    START_MSG = """
<b>✦ » Hᴇʟʟᴏ {}</b>,

<b>✦ » Tʜɪs Bᴏᴛ ɪs ғᴏʀ ᴛᴏ ʀᴇᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ᴏʀ ɢʀᴏᴜᴘ ɪɴ ᴍᴀss ʟᴇᴠᴇʟ ᴛʜʀᴏᴜɢʜ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ sᴇssɪᴏɴ sᴛʀɪɴɢ ᴡʜɪᴄʜ ʏᴏᴜ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ʙʏ :- <a href=t.me/king_string_session_bot>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b> 

<b>✦ » Tʜɪs ʙᴏᴛ ɪs sᴏʟᴇʟʏ ᴄʀᴇᴀᴛᴇ ᴏʀ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ :- <a href=t.me/II_VIKRANT_II>𝐕ɪᴋʀᴀɴᴛ</a></b>
"""

    HELP_MSG = """
**🔆 𝐇ᴇʟᴘ...**

**📚 Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:**

**⏣ /start - ᴄʜᴇᴄᴋ I'ᴍ ᴀʟɪᴠᴇ** 
**⏣ /make_config - Tᴏ Mᴀᴋᴇ Cᴏɴғɪɢ** 
**⏣ /del_config - Dᴇʟᴇᴛᴇ ᴛʜᴇ Cᴏɴғɪɢ**
**⏣ /target - Tᴏ sᴇᴇ ᴛʜᴇ ᴛᴀʀɢᴇᴛ ᴄʜᴀɴɴᴇʟ**
**⏣ /see_accounts - Sᴇᴇ ᴀʟʟ ᴛʜᴇ ᴀᴄᴄᴏᴜɴᴛs ʏᴏᴜ ᴀᴅᴅᴇᴅ**
**⏣ /see_accounts - Aᴅᴅ ɴᴇᴡ ᴀᴄᴄᴏᴜɴᴛs**
**⏣ /report - Rᴇᴘᴏʀᴛ ᴛʜᴇ ᴛᴀʀɢᴇᴛ**
**⏣ /restart - Rᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ**

**💢 Fᴇᴀᴛᴜʀᴇs:**

**► Rᴇᴘᴏʀᴛ ᴀ sɪɴɢʟᴇ ᴄʜᴀɴɴᴇʟ ᴏʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴍᴜʟᴛɪᴘʟᴇ Iᴅ's**

**► Tʏᴘᴇ ᴏғ ʀᴇᴘᴏʀᴛ ᴏᴘᴛɪᴏɴ ᴀᴠᴀɪʟᴀʙʟᴇ**

**► Fᴀᴄɪʟɪᴛɪᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ᴛʜᴇ Tᴀʀɢᴇᴛ Cʜᴀɴɴᴇʟ ᴏʀ Gʀᴏᴜᴘ**

**► Fᴀᴄɪʟɪᴛɪᴇ ᴛᴏ ᴀᴅᴅ ᴛʜᴇ ᴍᴜʟᴛɪᴘʟᴇs ᴀᴄᴄᴏᴜɴᴛs ᴀғᴛᴇʀ ᴏɴᴄᴇ ʏᴏᴜ ᴍᴀᴋᴇ ᴄᴏɴғɪɢ**

**► Aʟʟ ᴛʜᴇ ᴀᴄᴄᴏᴜɴᴛs ʏᴏᴜ ᴀᴅᴅᴇᴅ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ Jᴏɪɴᴇᴅ ᴛʜᴇ ᴛᴀʀɢᴇᴛ ᴄʜᴀɴɴᴇʟ ᴏʀ ɢʀᴏᴜᴘ**

**► Nᴏ ɴᴇᴇᴅ ᴛᴏ ᴇɴᴛᴇʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ, ᴘᴀssᴡᴏʀᴅ ᴏʀ ᴏᴛᴘ Jᴜsᴛ sᴇɴᴅ sᴇssɪᴏɴ sᴛʀɪɴɢ ᴀɴᴅ ᴛʜᴀᴛ's ɪᴛ**

**► Cʜᴇᴄᴋ ᴛʜᴇ sᴇʀᴠᴇʀ sᴛᴀᴛᴜs ᴀɴᴅ ʀᴇsᴏᴜʀᴄᴇs**
"""

    ABOUT_MSG = """
**- 𝖬ʏ ɴᴀᴍᴇ : <a href=https://t.me/{}>{}</a>**
**- 𝖢ʀᴇᴀᴛᴏʀ : <a href=t.me/II_VIKRANT_II>𝐕ɪᴋʀᴀɴᴛ</a>**
**- 𝖫ɪʙʀᴀʀʏ : Pʏʀᴏɢʀᴀᴍ**
**- 𝖫ᴀɴɢᴜᴀɢᴇ : 𝖯ʏᴛʜᴏɴ 𝟥**
**- 𝖣ᴀᴛᴀʙᴀsᴇ : 𝖬ᴏɴɢᴏ ᴅʙ**
**- 𝖡ᴏᴛ sᴇʀᴠᴇʀ : 𝖧ᴇʀᴏᴋᴜ 𝖱ᴇɴᴅᴇʀ**
"""
