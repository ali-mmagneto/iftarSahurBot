from pyrogram import Client, filters
import os, youtube_dl, requests, time
from youtube_search import YoutubeSearch
import asyncio

async def indir(link, ydl_opts):
    download_directory = "downloads/ytvideo.mp4"
    command_to_exec = [
        "yt-dlp",
        "-c",
        "--max-filesize", str(Config.TG_MAX_FILE_SIZE),
        "--embed-subs",
        "-f", ydl_opts,
        "--hls-prefer-ffmpeg", link,
        "-o", download_directory
    ]
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    return download_directory
@Client.on_message(filters.command('ytvideo'))
async def ytvideooo(bot, message):
    ydl_opts = {"format": "bestvideo[ext=mp4]"}
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
            video = await indir(link, ydl_opts)
            rep = f"[İndirildi](https://t.me/iftarSahurTrRoBot)"
            carp, durationn, dur = 1, 0, duration.split(':')
            for i in range(len(dur)-1, -1, -1):
                durationn += (int(dur[i]) * carp)
                carp *= 60
            await m.edit("`Yüklüyorum..`")
            await bot.send_video(
                chat_id=message.chat.id,
                video=video, 
                thumb=thumb_name,
                duration=durationn,
                caption=title)
            await m.delete()
        else:
            await m.edit("`İstediğini Bulamadım 🥱`")
    except Exception as e:
        await message.reply_text(e) 
