from pyrogram import Client, filters
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

@Client.on_message(filters.command('info'))
async def info(bot, message):
    try:
        if not message.reply_to_message:
            text = await bot.get_chat(message.chat.id)
            await message.reply_text(text)
            async for photo in bot.get_chat_photos(message.chat.id, limit=1):
                LOGGER.info(photo)
                caption = f"Grup Adı: {text.title}\nGrup Id: {text.id}\n\nSenin Adın: {message.from_user.first_name}\nSenin Id: {message.from_user.id}\nSen: {message.from_user.mention}"
                await message.reply_photo(photo.file_id, caption=caption) 
        else:
            text = message.from_user
            async for photo in bot.get_chat_photos(message.reply_to_message.from_user.id, limit=1):
                LOGGER.info(photo)
                caption = f"Adı: {message.reply_to_message.from_user.first_name}\nId: {message.reply_to_message.from_user.id}\nDc Id: {message.reply_to_message.from_user.dc_id}O: {message.reply_to_message.from_user.mention}"
                await message.reply_photo(photo.file_id, caption=caption) 
    except Exception as e:
        await message.reply_text(e)
