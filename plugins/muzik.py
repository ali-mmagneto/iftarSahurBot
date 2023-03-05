# CODED BY :d

from pyrogram import Client, filters
import os, youtube_dl, requests, time
from youtube_search import YoutubeSearch

@Client.on_message(filters.command('muzik'))
async def muzikk(bot, message):
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        m = await message.reply_text("`Arıyorum..`")
        text = message.text.split(" ", 1)
        aranacak = text[1]
        results = YoutubeSearch(aranacak, max_results=1).to_dict()
        if results:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]
            thumb_name = f'thumb{message.id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)
            await m.edit("`Buldum Indiriyorum...`")
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=False)
                audio_file = ydl.prepare_filename(info_dict)
                ydl.process_info(info_dict)
            rep = f"[İndirildi](https://t.me/iftarSahurTrRoBot)"
            carp, durationn, dur = 1, 0, duration.split(':')
            for i in range(len(dur)-1, -1, -1):
                durationn += (int(dur[i]) * carp)
                carp *= 60
            await m.edit("`Yüklüyorum..`")
            await bot.send_audio(
                chat_id=message.chat.id,
                audio=audio_file, 
                thumb=thumb_name,
                duration=durationn,
                caption=rep)
            await m.delete()
        else:
            await m.edit("`İstediğini Bulamadım 🥱`")
    except Exception as e:
        await message.reply_text(e)
