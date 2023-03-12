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
    elif message.reply_to_message.video:
        m = await message.reply_text("`Dönüştürülüyor...`")
        name_format = f"downloads/donusturulmussticker"
        image = await bot.download_media(
                    message = message.reply_to_message,
                    file_name=f"{name_format}.tgs")
        await m.edit("`Gönderiyorum...`")
        video = f"{name_format}.tgs"
        try:
            await bot.send_sticker(
                 chat_id=message.chat.id,
                 sticker=video)
            await m.delete()
        except Exception as e:
            await message.reply_text(e)
    elif message.reply_to_message.sticker:
        if message.reply_to_message.sticker.is_animated == True:
            try:
                name_format = "downloads/donusturulmusvideo"
                gif = await bot.download_media(
                          message = message.reply_to_message,
                          file_name=f"{name_format}.mp4")
                video = f"{name_format}.mp4"
                await bot.send_video(
                    chat_id = message.chat.id, 
                    video = video) 
            except Exception as e:
                await message.reply_text(e)
        elif message.reply_to_message.sticker.is_video == True:
            try:
                name_format = "downloads/donusturulmusvideo"
                gif = await bot.download_media(
                          message = message.reply_to_message,
                          file_name=f"{name_format}.mp4")
                video = f"{name_format}.mp4"
                await bot.send_video(
                    chat_id = message.chat.id, 
                    video = video) 
            except Exception as e:
                await message.reply_text(e)
        else:
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
