import re
import time
import asyncio
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait
from info import ADMINS, INDEX_EXTENSIONS
from database.ia_filterdb import save_file
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import temp, get_readable_time

lock = asyncio.Lock()

@Client.on_callback_query(filters.regex(r'^index'))
async def index_files(bot, query):
    _, ident, chat, lst_msg_id, skip = query.data.split("#")
    if ident == 'yes':
        msg = query.message
        await msg.edit("Indexation en cours...")
        try:
            chat = int(chat)
        except:
            chat = chat
        await index_files_to_db(int(lst_msg_id), chat, msg, bot, int(skip))
    elif ident == 'cancel':
        temp.CANCEL = True
        await query.message.edit("Tentative d'annulation de l'indexation...")

@Client.on_message(filters.command('index') & filters.private & filters.incoming & filters.user(ADMINS))
async def send_for_index(bot, message):
    if lock.locked():
        return await message.reply('Veuillez attendre la fin du processus précédent.')
    i = await message.reply("Transférez le dernier message ou envoyez le lien du dernier message.")
    msg = await bot.listen(chat_id=message.chat.id, user_id=message.from_user.id)
    await i.delete()
    if msg.text and msg.text.startswith("https://t.me"):
        try:
            msg_link = msg.text.split("/")
            last_msg_id = int(msg_link[-1])
            chat_id = msg_link[-2]
            if chat_id.isnumeric():
                chat_id = int(("-100" + chat_id))
        except:
            await message.reply('Lien de message invalide !')
            return
    elif msg.forward_from_chat and msg.forward_from_chat.type == enums.ChatType.CHANNEL:
        last_msg_id = msg.forward_from_message_id
        chat_id = msg.forward_from_chat.username or msg.forward_from_chat.id
    else:
        await message.reply('Ce n\'est ni un message transféré ni un lien.')
        return
    try:
        chat = await bot.get_chat(chat_id)
    except Exception as e:
        return await message.reply(f'Erreur - {e}')

    if chat.type != enums.ChatType.CHANNEL:
        return await message.reply("Je peux indexer uniquement les canaux.")

    s = await message.reply("Envoyez le numéro de message à ignorer.")
    msg = await bot.listen(chat_id=message.chat.id, user_id=message.from_user.id)
    await s.delete()
    try:
        skip = int(msg.text)
    except:
        return await message.reply("Le numéro est invalide.")

    buttons = [[
        InlineKeyboardButton('OUI', callback_data=f'index#yes#{chat_id}#{last_msg_id}#{skip}')
    ],[
        InlineKeyboardButton('FERMER', callback_data='close_data'),
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(f"Voulez-vous indexer le canal {chat.title} ?\nMessages Totals : <code>{last_msg_id}</code>", reply_markup=reply_markup)

async def index_files_to_db(lst_msg_id, chat, msg, bot, skip):
    start_time = time.time()
    total_files = 0
    duplicate = 0
    errors = 0
    deleted = 0
    no_media = 0
    unsupported = 0
    badfiles = 0
    current = skip
    
    async with lock:
        try:
            async for message in bot.iter_messages(chat, lst_msg_id, skip):
                time_taken = get_readable_time(time.time()-start_time)
                if temp.CANCEL:
                    temp.CANCEL = False
                    await msg.edit(f"Annulation réussie !\nTerminé en {time_taken}\n\n<code>{total_files}</code> fichiers sauvegardés dans la base de données !\nFichiers dupliqués ignorés : <code>{duplicate}</code>\nMessages supprimés ignorés : <code>{deleted}</code>\nMessages non-média ignorés : <code>{no_media + unsupported}</code>\nMédia non supporté : <code>{unsupported}</code>\nErreurs survenues : <code>{errors}</code>\nMauvais fichiers ignorés : <code>{badfiles}</code>")
                    return
                current += 1
                if current % 30 == 0:
                    btn = [[
                        InlineKeyboardButton('ANNULER', callback_data=f'index#cancel#{chat}#{lst_msg_id}#{skip}')
                    ]]
                    try:
                        await msg.edit_text(text=f"Messages reçus : <code>{current}</code>\nMessages sauvegardés : <code>{total_files}</code>\nFichiers dupliqués ignorés : <code>{duplicate}</code>\nMessages supprimés ignorés : <code>{deleted}</code>\nMessages non-média ignorés : <code>{no_media + unsupported}</code>\nMédia non supporté : <code>{unsupported}</code>\nErreurs survenues : <code>{errors}</code>\nMauvais fichiers ignorés : <code>{badfiles}</code>", reply_markup=InlineKeyboardMarkup(btn))
                    except FloodWait as e:
                        await asyncio.sleep(e.value)
                if message.empty:
                    deleted += 1
                    continue
                elif not message.media:
                    no_media += 1
                    continue
                elif message.media not in [enums.MessageMediaType.VIDEO, enums.MessageMediaType.DOCUMENT]:
                    unsupported += 1
                    continue
                media = getattr(message, message.media.value, None)
                if not media:
                    unsupported += 1
                    continue
                elif not (str(media.file_name).lower()).endswith(tuple(INDEX_EXTENSIONS)):
                    unsupported += 1
                    continue
                media.caption = message.caption
                file_name = re.sub(r"@\w+|(_|\-|\.|\+)", " ", str(media.file_name))
                sts = await save_file(media)
                if sts == 'suc':
                    total_files += 1
                elif sts == 'dup':
                    duplicate += 1
                elif sts == 'err':
                    errors += 1
        except Exception as e:
            await msg.reply(f'Indexation annulée en raison d\'une erreur - {e}')
        else:
            await msg.edit(f'Sauvegarde réussie de <code>{total_files}</code> dans la base de données !\nTerminé en {time_taken}\n\nFichiers dupliqués ignorés : <code>{duplicate}</code>\nMessages supprimés ignorés : <code>{deleted}</code>\nMessages non-média ignorés : <code>{no_media + unsupported}</code>\nMédia non supporté : <code>{unsupported}</code>\nErreurs survenues : <code>{errors}</code>\nMauvais fichiers ignorés : <code>{badfiles}</code>')
