import requests
from pyrogram import Client, filters
from PyroUbot import *

__MODULE__ = "ᴘᴀsᴀɴɢᴀɴ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴋᴇᴄᴏᴄᴏᴋᴀɴ ᴘᴀsᴀɴɢᴀɴ ⦫</b>

<blockquote><b>⎆ ᴘᴇʀɪɴᴛᴀʜ :
ᚗ <code>{0}pasangan</code> nama1, nama2

⌭ ᴘᴇɴᴊᴇʟᴀsᴀɴ:
ᚗ Meramal kecocokan pasangan</blockquote>
"""


@PY.UBOT("pasangan")
async def cek_kecocokan(_, message):
    text = message.text[len(message.command[0]) + 2:].strip()

    if "," not in text:
        return await message.reply("**Gunakan format:**\n`.pasangan nama1, nama2`")

    nama1, nama2 = map(str.strip, text.split(",", 1))

    api_url = f"https://api.siputzx.my.id/api/primbon/kecocokan_nama_pasangan?nama1={nama1}&nama2={nama2}"
    
    try:
        response = requests.get(api_url)
        data = response.json()

        if data.get("status"):
            hasil = data["data"]
            teks = (
                "<blockquote>"
                f"<emoji id=6026321200597176575>🃏</emoji> **Kecocokan Nama Pasangan** <emoji id=6026321200597176575>🃏</emoji>\n"
                f"<emoji id=5204015897500469606>😢</emoji> **{hasil['nama_anda']}**\n <emoji id=5226859896539989141>😘</emoji> **{hasil['nama_pasangan']}**\n\n"
                f"<emoji id=5217466996337165348>👍</emoji> **Sisi Positif:**\n`{hasil['sisi_positif']}`\n\n"
                f"<emoji id=5436223772510142944>👎</emoji> **Sisi Negatif:**\n`{hasil['sisi_negatif']}`\n\n"
                f"<emoji id=5238039443008408242>💌</emoji> **Catatan:**\n_{hasil['catatan']}_"
                "</blockquote>"
            )
            await message.reply_photo(hasil["gambar"], caption=teks)
        else:
            await message.reply("⚠️ **Gagal mendapatkan data kecocokan.**")
    
    except Exception as e:
        await message.reply(f"❌ **Terjadi kesalahan:** `{e}`")
