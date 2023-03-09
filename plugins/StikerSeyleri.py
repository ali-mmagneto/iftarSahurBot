from pyrogram import Client, filters 
from PIL import Image



@Client.on_message(filters.command('donustur'))
async def donusturucu(bot, message):
    user_id = message.from_user.id
    message_id = message.reply_to_message.id
    name_format = f"Mickey_{user_id}_{message_id}"
    if message.reply_to_message.photo:
        m = await message.reply_text("`Dönüştürülüyor...`")
        image = await bot.download_media(
                    message = message.reply_to_message,
                    file_name=f"{name_format}.jpg")
        await m.edit("`Gönderiyorum...`")
        im = Image.open(image).convert("RGB")
        im.save(f"{name_format}.webp", "webp")
        sticker = f"{name_format}.webp"
        await m.reply_sticker(sticker)
        await m.delete()
        os.remove(sticker)
        os.remove(image)
    elif message.reply_to_message.sticker:
        m = await message.reply_text("`Dönüştürülüyor...`")
        sticker = await bot.download_media(
                      message = message.reply_to_message,
                      file_name=f"{name_format}.webp")
        await m.edit("`Gönderiyorum...`")
        im = Image.open(sticker).convert("RGB")
        im.save(f"{name_format}.jpg", "jpeg")
        image = f"{name_format}.jpg"
        await m.reply_photo(image)
        await m.delete()
        os.remove(image)
        os.remove(sticker) 
