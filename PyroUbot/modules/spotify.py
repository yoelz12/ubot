from pyrogram import Client, filters
import requests
import os
from PyroUbot import *

__MODULE__ = "sᴘᴏᴛɪғʏ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴘᴏᴛɪғʏ ⦫</b>
<blockquote><b>
⎆ Perintah :
ᚗ <code>{0}spotify</code> judul lagu
⊶ Mendownload Music Yang Di Inginkan.</b></blockquote>
"""

@PY.UBOT("spotify")
async def spotify_search(client, message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply_text("Gunakan format: /spotify <judul lagu>")
        return
    
    proses_msg = await message.reply_text("🔎 Mencari lagu...")
    search_url = f"https://api.botcahx.eu.org/api/search/spotify?query={query}&apikey=moire"
    search_response = requests.get(search_url).json()
    
    if not search_response["status"] or not search_response["result"]["status"]:
        await proses_msg.edit_text("Gagal mencari lagu.")
        return
    
    tracks = search_response["result"]["data"]
    if not tracks:
        await proses_msg.edit_text("Tidak ditemukan hasil untuk pencarian tersebut.")
        return
    
    track_url = tracks[0]["url"]
    
    await proses_msg.edit_text("👅 Mengunduh lagu...")
    
    download_url = f"https://api.botcahx.eu.org/api/download/spotify?url={track_url}&apikey=moire"
    download_response = requests.get(download_url).json()
    
    if not download_response["status"]:
        await proses_msg.edit_text("Gagal mengunduh lagu.")
        return
    
    data = download_response["result"]["data"]
    file_url = data["url"]
    track_title = data["title"]
    track_duration = data["duration"]
    artist_name = data["artist"]["name"]
    spotify_url = data["artist"]["external_urls"]["spotify"]
    
    user_id = message.from_user.id
    audio_path = f"downloaded_audio_{user_id}.mp3"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(file_url, headers=headers, stream=True)
    if response.status_code != 200:
        await proses_msg.edit_text("Gagal mengunduh lagu. Server menolak permintaan (403 Forbidden).")
        return
    
    with open(audio_path, "wb") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)
    
    caption = (f"🎵 <b>{track_title}</b>\n"
               f"👤 Artist: {artist_name}\n"
               f"⏳ Durasi: {track_duration}\n"
               f"🔗 <a href='{spotify_url}'>Dengarkan di Spotify</a>")
    
    await client.send_audio(
        chat_id=message.chat.id,
        audio=audio_path,
        title=track_title,
        caption=caption
    )
    
    os.remove(audio_path)    
    await proses_msg.delete()
