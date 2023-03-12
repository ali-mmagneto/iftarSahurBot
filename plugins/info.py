from pyrogram import Client, filters


@Client.on_message(filters.command('info'))
async def info(bot, message):
    try:
        if not message.reply_to_message:
            text = await bot.get_chat(message.chat.id)
            await message.reply_text(text)
            await message.reply_photo(text.photo.small_photo_unique_id)
        else:
            text = message.from_user
            await message.reply_text(text)
    except Exception as e:
        await message.reply_text(e)
