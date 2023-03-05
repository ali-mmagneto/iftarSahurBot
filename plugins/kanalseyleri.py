# CODED BY :d

import pyrogram
from pyrogram import Client, filters
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import ChatMemberUpdated

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@Client.on_message(filters.group & filters.service)
async def hosveyabos(bot, cmu: ChatMemberUpdated):
    yeni = cmu.new_chat_member.user_id
    me = await bot.get_me()
    if yeni == me.user_id:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo="https://telegra.ph/file/5ea51a7229254f84767f6.jpg",
            caption='Bu gruba beni eklediğin için teşekkürler. Kullanım için /start yazabilirsin.')
        yenikanal = await bot.get_chat(message.chat.id)
        await bot.send_message(OWNER_ID, f"#YeniKanalEklenmesi\n\n**Kanal Adı**: {yenikanal.title}\n**Kanal id**: {yenikanal.id}\n**Ekleyen**: {message.from_user.first_name}\n**Ekleyen id**: {message.from_user.id}\n\nEğer bu kanalı sevmediysen `/ayril {yenikanal.id}` komutu ile botu Çıkartabilirsin..")

@Client.on_message(filters.command('ayril'))
async def baybay(bot, message):
    try:
        text = message.text.split(" ", 1)
        id = text[1]
        k = await bot.get_chat(id)
        m = await bot.send_photo(
            chat_id=id, 
            photo="https://telegra.ph/file/b9099e8d2f4a7075ec395.jpg",
            caption="Sahibim Bu Kanalda Bulunmamı Onaylamadı Gidiyom Ben..\n\nDestek ile konușabilirsin.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"Destek", url="https://t.me/mmagneto")]]))
        try:
            m.pin()
        except Exception:
            pass
        await bot.leave_chat(id)
        await message.reply_text(f"Bașarıyla {k.title} Kanalından Çıkıldı")
    except Exception as e:
        await message.reply_text(e)
