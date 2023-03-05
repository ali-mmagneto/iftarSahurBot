from pyrogram import Client, filters
import os, youtube_dl, requests, time
from youtube_search import YoutubeSearch

@Client.on_message(filters.command('muzik'))
async def muzikk(bot, message):
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
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
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=False)
                audio_file = ydl.prepare_filename(info_dict)
                ydl.process_info(info_dict)
            rep = f"İndirildi [İndiren Bot](https://t.me/iftarvesahurBot)"
            await message.reply_audio(
                audio=audio_file,
                caption=rep)
    except Exception as e:
        await message.reply_text(e)
