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
                await message.reply_photo(photo) 
        else:
            text = message.from_user
            await message.reply_text(text)
    except Exception as e:
        await message.reply_text(e)
