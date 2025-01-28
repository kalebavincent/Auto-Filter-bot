from info import ADMINS
from speedtest import Speedtest, ConfigRetrievalError
from pyrogram import Client, filters, enums
from utils import get_size
from datetime import datetime


@Client.on_message(filters.command('id'))
async def showid(client, message):
    chat_type = message.chat.type
    replied_to_msg = bool(message.reply_to_message)
    if replied_to_msg:
        return await message.reply_text(f"""L'ID du canal du message transféré {replied_to_msg.chat.title} est, <code>{replied_to_msg.chat.id}</code>.""")
    if chat_type == enums.ChatType.PRIVATE:
        await message.reply_text(f'★ ID de l\'utilisateur: <code>{message.from_user.id}</code>')

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        await message.reply_text(f'★ ID du groupe: <code>{message.chat.id}</code>')

    elif chat_type == enums.ChatType.CHANNEL:
        await message.reply_text(f'★ ID du canal: <code>{message.chat.id}</code>')


@Client.on_message(filters.command('speedtest') & filters.user(ADMINS))
async def speedtest(client, message):
    msg = await message.reply_text("Lancement du test de vitesse...")
    try:
        speed = Speedtest()
    except ConfigRetrievalError:
        await msg.edit("Impossible de se connecter au serveur pour le moment, réessayez plus tard !")
        return
    speed.get_best_server()
    speed.download()
    speed.upload()
    speed.results.share()
    result = speed.results.dict()
    photo = result['share']
    text = f'''
➲ <b>INFORMATIONS SUR LE TEST DE VITESSE</b>
┠ <b>Upload:</b> <code>{get_size(result['upload'])}/s</code>
┠ <b>Download:</b>  <code>{get_size(result['download'])}/s</code>
┠ <b>Ping:</b> <code>{result['ping']} ms</code>
┠ <b>Temps:</b> <code>{datetime.strptime(result['timestamp'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")}</code>
┠ <b>Données envoyées:</b> <code>{get_size(int(result['bytes_sent']))}</code>
┖ <b>Données reçues:</b> <code>{get_size(int(result['bytes_received']))}</code>

➲ <b>SERVEUR DU TEST DE VITESSE</b>
┠ <b>Nom:</b> <code>{result['server']['name']}</code>
┠ <b>Pays:</b> <code>{result['server']['country']}, {result['server']['cc']}</code>
┠ <b>Sponsor:</b> <code>{result['server']['sponsor']}</code>
┠ <b>Latence:</b> <code>{result['server']['latency']}</code>
┠ <b>Latitude:</b> <code>{result['server']['lat']}</code>
┖ <b>Longitude:</b> <code>{result['server']['lon']}</code>

➲ <b>DETAILS DU CLIENT</b>
┠ <b>Adresse IP:</b> <code>{result['client']['ip']}</code>
┠ <b>Latitude:</b> <code>{result['client']['lat']}</code>
┠ <b>Longitude:</b> <code>{result['client']['lon']}</code>
┠ <b>Pays:</b> <code>{result['client']['country']}</code>
┠ <b>Fournisseur d'accès (ISP):</b> <code>{result['client']['isp']}</code>
┖ <b>Note de l'ISP:</b> <code>{result['client']['isprating']}</code>
'''
    await message.reply_photo(photo=photo, caption=text)
    await msg.delete()
