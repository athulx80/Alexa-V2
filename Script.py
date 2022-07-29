class script(object):
    START_TXT = """𝖧𝖾𝗒𝗒 {},
𝖬𝗒 𝖭𝖺𝗆𝖾 𝖨𝗌 <a href=https://t.me/{}>{}</a> 𝖨 𝖠𝗆 𝖠 𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅𝗅 𝖠𝗎𝗍𝗈𝖥𝗂𝗅𝗍𝖾𝗋 𝖡𝗈𝗍 𝖶𝗂𝗍𝗁 𝖲𝗈𝗆𝖾 𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌..."""
    HELP_TXT = """𝖧𝖾𝗒𝗒 {}
𝖧𝖾𝗋𝖾 𝖨𝗌 𝖳𝗁𝖾 𝖧𝖾𝗅𝗉 𝖥𝗈𝗋 𝖬𝗒 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌."""
    ABOUT_TXT = """➲ 𝖬𝗒 𝖭𝖺𝗆𝖾: {}
➲ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋: <a href=https://t.me/athulx80>𝖠𝗍𝗁𝗎𝗅</a>
➲ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒: 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆
➲ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾: 𝖯𝗒𝗍𝗁𝗈𝗇 𝟥
➲ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾: <a href=https://www.mongodb.com/>𝖬𝗈𝗇𝗀𝗈𝖣𝖡</a>
➲ 𝖡𝗈𝗍 𝖲𝖾𝗋𝗏𝖾𝗋: 𝖧𝖾𝗋𝗈𝗄𝗎
➲ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌: 𝖵1.0.2 [ 𝖡𝖤𝖳𝖠 ]"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>  
- Filter is the feature were users can set automated replies for a particular keyword and 𝙰𝚃𝙷𝚄𝙻 will respond whenever a keyword is found the message
<b>NOTE:</b>
1. FILTER BOT should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
➾ /filter - <code>add a filter in chat</code>
➾ /filters - <code>list all the filters of a chat</code>
➾ /del - <code>delete a specific filter in chat</code>
➾ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>
- BOT Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. BOT supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:http://www.example.com/)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
➾ /connect  - <code>connect a particular chat to your PM</code>
➾ /disconnect  - <code>disconnect from a chat</code>
➾ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
These are the extra features of ALEXA
<b>Commands and Usage:</b>
➾ /id - <code>get id of a specifed user.</code>
➾ /info  - <code>get information about a user.</code>
➾ /imdb  - <code>get the film information from IMDb source.</code>
➾ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my OWNER⚡
<b>Commands and Usage:</b>
➾ /logs - <code>to get the rescent errors</code>
➾ /stats - <code>to get status of files in db.</code>
➾ /delete - <code>to delete a specific file from db.</code>
➾ /users - <code>to get list of my users and ids.</code>
➾ /chats - <code>to get list of the my chats and ids </code>
➾ /leave  - <code>to leave from a chat.</code>
➾ /disable  -  <code>do disable a chat.</code>
➾ /ban  - <code>to ban a user.</code>
➾ /unban  - <code>to unban a user.</code>
➾ /channel - <code>to get list of total connected channels</code>
➾ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """✮ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ: <code>{}</code>
✮ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : <code>{}</code>
✮ ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘꜱ: <code>{}</code>
✮ ᴜꜱᴇᴅ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱
✮ ꜰʀᴇᴇ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
✮ 𝐆𝐫𝐨𝐮𝐩 ›› {}(<code>{}</code>)
✮ 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ›› <code>{}</code>
✮ 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ›› {}
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
✮ 𝐈𝐃 ›› <code>{}</code>
✮ 𝐍𝐚𝐦𝐞 ›› {}
"""
    CARBON_TXT = """ <b>𝖢𝖠𝖱𝖡𝖮𝖭 𝖬𝖮𝖣𝖴𝖫𝖤</b>
<b>𝖸𝗈𝗎 𝖢𝖺𝗇 𝖡𝖾𝖺𝗎𝗍𝗂𝖿𝗒 𝖸𝗈𝗎𝗋 𝖢𝗈𝖽𝖾𝗌 𝖡𝗒 𝖴𝗌𝗂𝗇𝗀 𝖳𝗁𝖾 𝖥𝖾𝖺𝗍𝗎𝗋𝖾...</b>
<b>𝖢𝗈𝗆𝗆𝖺𝗇𝖽..!</b>
<b>/carbon ›› 𝖱𝖾𝗉𝗅𝗒 𝖳𝗈 𝖠𝗇𝗒 𝖳𝖾𝗑𝗍 𝖬𝖾𝗌𝗌𝖺𝗀𝖾</b>
<b>𝖱𝖾𝗉𝗅𝗒 𝖳𝗈 𝖠𝗇𝗒 𝖳𝖾𝗑𝗍 𝖬𝖾𝗌𝗌𝖺𝗀𝖾

𝖶𝗈𝗋𝗄𝗌 𝖮𝗇 𝖡𝗈𝗍𝗁 𝖦𝗋𝗈𝗎𝗉 𝖠𝗇𝖽 𝖯𝖬</b>"""
