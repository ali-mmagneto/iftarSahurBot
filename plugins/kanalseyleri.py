import pyrogram
from pyrogram import Client, filters
from config import OWNER_ID

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@Client.on_message(filters.group & filters.service)
async def hosveyabos(bot, message):
    await bot.send_photo(
        chat_id=message.chat.id,
        photo="https://telegra.ph/file/5ea51a7229254f84767f6.jpg",
        caption='Bu gruba beni eklediğin için teşekkürler. Kullanım için /start yazabilirsin.')
    yenikanal = await bot.get_chat(message.chat.id)
    LOGGER.info(yenikanal)
