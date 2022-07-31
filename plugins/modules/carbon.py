from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client as bot
from plugins.function import make_carbon
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
aiohttpsession = ClientSession()

C = "**ᴍᴀᴅᴇ ʙʏ [ᴀᴛʜᴜʟ](https://github.com/athulx80)**"
F = InlineKeyboardMarkup(
[[
     InlineKeyboardButton("⭕ ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/+L8SWfrF_7m04ODZl")
]]
)





@bot.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "**𝖱𝖾𝗉𝗅𝗒 𝖳𝗈 𝖳𝖾𝗑𝗍 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖳𝗈 𝗆𝖺𝗄𝖾 𝖢𝖺𝗋𝖻𝗈𝗇.**"
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "**𝖱𝖾𝗉𝗅𝗒 𝖳𝗈 𝖳𝖾𝗑𝗍 𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖳𝗈 𝗆𝖺𝗄𝖾 𝖢𝖺𝗋𝖻𝗈𝗇.**"
        )
    user_id = message.from_user.id
    m = await message.reply_text("**𝙲𝚁𝙴𝙰𝚃𝙸𝙽𝙶 𝙲𝙰𝚁𝙱𝙾𝙽...**")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("**𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙲𝙰𝚁𝙱𝙾𝙽...**")
    await message.reply_photo(
        photo=carbon,
        caption=C,
        reply_markup=F)
    await m.delete()
    carbon.close()
