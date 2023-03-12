from pyrogram import Client, filters
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

@Client.on_message(filters.command('bilgi'))
async def info(bot, message):
    try:
        if not message.reply_to_message:
            text = await bot.get_chat(message.chat.id)
            await message.reply_text(text)
            async for photo in bot.get_chat_photos(message.chat.id, limit=1):
                LOGGER.info(photo)
                caption = f"**Grup Adı**: {text.title}\n**Grup Id**: `{text.id}`\n\n**Senin Adın**: {message.from_user.first_name}\n**Senin Kullanıcı Adı**: @{message.from_username}**Senin Id**: `{message.from_user.id}`\n**Senin Dc**: {message.from_user.dc_id}\n**Sen**: {message.from_user.mention}"
                await message.reply_photo(photo.file_id, caption=caption) 
        else:
            text = message.from_user
            await message.reply_text(text)
            async for photo in bot.get_chat_photos(message.reply_to_message.from_user.id, limit=1):
                LOGGER.info(photo)
                caption = f"**Adı**: {message.reply_to_message.from_user.first_name}\n**Kullanıcı Adı**: @{message.reply_to_message.from_user.username}\n**Id**: `{message.reply_to_message.from_user.id}`\n**Dc Id**: {message.reply_to_message.from_user.dc_id}\n**O**: {message.reply_to_message.from_user.mention}"
                await message.reply_photo(photo.file_id, caption=caption) 
    except Exception as e:
        await message.reply_text(e)
