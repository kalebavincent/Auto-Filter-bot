import random
import os
import sys
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
from info import ADMINS, LOG_CHANNEL, PICS, SUPPORT_LINK, UPDATES_LINK
from database.users_chats_db import db
from utils import temp, get_settings
from Script import script


@Client.on_chat_member_updated(filters.group)
async def bienvenue(bot, message):
    if message.new_chat_member and not message.old_chat_member:
        if message.new_chat_member.user.id == temp.ME:
            boutons = [[
                InlineKeyboardButton('Mise à jour', url=UPDATES_LINK),
                InlineKeyboardButton('Support', url=SUPPORT_LINK)
            ]]
            reply_markup = InlineKeyboardMarkup(boutons)
            utilisateur = message.from_user.mention if message.from_user else "Dear"
            await bot.send_photo(chat_id=message.chat.id, photo=random.choice(PICS), caption=f"👋 Bonjour {utilisateur},\n\nMerci de m'avoir ajouté au groupe <b>'{message.chat.title}'</b>, n'oubliez pas de me rendre administrateur. Si vous voulez en savoir plus, contactez le groupe de support. 😘</b>", reply_markup=reply_markup)
            if not await db.get_chat(message.chat.id):
                total = await bot.get_chat_members_count(message.chat.id)
                username = f'@{message.chat.username}' if message.chat.username else 'Private'
                await bot.send_message(LOG_CHANNEL, script.NEW_GROUP_TXT.format(message.chat.title, message.chat.id, username, total))       
                await db.add_chat(message.chat.id, message.chat.title)
            return
        settings = await get_settings(message.chat.id)
        if settings["welcome"]:
            WELCOME = settings['welcome_text']
            message_bienvenue = WELCOME.format(
                mention = message.new_chat_member.user.mention,
                title = message.chat.title
            )
            await bot.send_message(chat_id=message.chat.id, text=message_bienvenue)


@Client.on_message(filters.command('restart') & filters.user(ADMINS))
async def redemarrer_bot(bot, message):
    msg = await message.reply("Redémarrage...")
    with open('restart.txt', 'w+') as file:
        file.write(f"{msg.chat.id}\n{msg.id}")
    os.execl(sys.executable, sys.executable, "bot.py")

@Client.on_message(filters.command('leave') & filters.user(ADMINS))
async def quitter_un_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Donne-moi un ID de chat')
    r = message.text.split(None)
    if len(r) > 2:
        raison = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        raison = "Aucune raison fournie."
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        boutons = [[
            InlineKeyboardButton('Groupe de Support', url=SUPPORT_LINK)
        ]]
        reply_markup = InlineKeyboardMarkup(boutons)
        await bot.send_message(
            chat_id=chat,
            text=f'Bonjour amis,\nMon propriétaire m\'a demandé de quitter ce groupe, alors je pars ! Si vous avez besoin, ajoutez-moi à nouveau en contactant mon groupe de support.\nRaison - <code>{raison}</code>',
            reply_markup=reply_markup,
        )
        await bot.leave_chat(chat)
        await message.reply(f"<b>✅️ Bot quitté avec succès du groupe - `{chat}`</b>")
    except Exception as e:
        await message.reply(f'Erreur - {e}')

@Client.on_message(filters.command('ban_grp') & filters.user(ADMINS))
async def désactiver_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Donne-moi un ID de chat')
    r = message.text.split(None)
    if len(r) > 2:
        raison = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        raison = "Aucune raison fournie."
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Donne-moi un ID de chat valide')
    cha_t = await db.get_chat(int(chat_))
    if not cha_t:
        return await message.reply("Chat introuvable dans la base de données")
    if cha_t['is_disabled']:
        return await message.reply(f"Ce chat est déjà désactivé.\nRaison - <code>{cha_t['reason']}</code>")
    await db.disable_chat(int(chat_), raison)
    temp.BANNED_CHATS.append(int(chat_))
    await message.reply('Chat désactivé avec succès')
    try:
        boutons = [[
            InlineKeyboardButton('Groupe de Support', url=SUPPORT_LINK)
        ]]
        reply_markup = InlineKeyboardMarkup(boutons)
        await bot.send_message(
            chat_id=chat_, 
            text=f'Bonjour amis,\nMon propriétaire m\'a demandé de quitter ce groupe, alors je pars ! Si vous avez besoin, ajoutez-moi à nouveau en contactant mon groupe de support.\nRaison - <code>{raison}</code>',
            reply_markup=reply_markup)
        await bot.leave_chat(chat_)
    except Exception as e:
        await message.reply(f"Erreur - {e}")

@Client.on_message(filters.command('unban_grp') & filters.user(ADMINS))
async def réactiver_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Donne-moi un ID de chat')
    chat = message.command[1]
    try:
        chat_ = int(chat)
    except:
        return await message.reply('Donne-moi un ID de chat valide')
    sts = await db.get_chat(int(chat))
    if not sts:
        return await message.reply("Chat introuvable dans la base de données")
    if not sts.get('is_disabled'):
        return await message.reply('Ce chat n\'est pas encore désactivé.')
    await db.re_enable_chat(int(chat_))
    temp.BANNED_CHATS.remove(int(chat_))
    await message.reply("Chat réactivé avec succès")

@Client.on_message(filters.command('invite_link') & filters.user(ADMINS))
async def générer_lien_invite(bot, message):
    if len(message.command) == 1:
        return await message.reply('Donne-moi un ID de chat')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        return await message.reply('Donne-moi un ID de chat valide')
    try:
        lien = await bot.create_chat_invite_link(chat)
    except Exception as e:
        return await message.reply(f'Erreur - {e}')
    await message.reply(f'Voici ton lien d\'invitation : {lien.invite_link}')

@Client.on_message(filters.command('ban_user') & filters.user(ADMINS))
async def bannir_utilisateur(bot, message):
    if len(message.command) == 1:
        return await message.reply('Donne-moi un ID utilisateur ou un nom d\'utilisateur')
    r = message.text.split(None)
    if len(r) > 2:
        raison = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        raison = "Aucune raison fournie."
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except Exception as e:
        return await message.reply(f'Erreur - {e}')
    else:
        if k.id in ADMINS:
            return await message.reply('Tu es administrateur')
        jar = await db.get_ban_status(k.id)
        if jar['is_banned']:
            return await message.reply(f"{k.mention} est déjà banni.\nRaison - <code>{jar['ban_reason']}</code>")
        await db.ban_user(k.id, raison)
        temp.BANNED_USERS.append(k.id)
        await message.reply(f"{k.mention} a été banni avec succès")
   
@Client.on_message(filters.command('unban_user') & filters.user(ADMINS))
async def débannir_utilisateur(bot, message):
    if len(message.command) == 1:
        return await message.reply('Donne-moi un ID utilisateur ou un nom d\'utilisateur')
    r = message.text.split(None)
    if len(r) > 2:
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except Exception as e:
        return await message.reply(f'Erreur - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if not jar['is_banned']:
            return await message.reply(f"{k.mention} n'est pas encore banni.")
        await db.remove_ban(k.id)
        temp.BANNED_USERS.remove(k.id)
        await message.reply(f"{k.mention} a été débanni avec succès")
    
@Client.on_message(filters.command('users') & filters.user(ADMINS))
async def list_users(bot, message):
    raju = await message.reply('Récupération de la liste des utilisateurs')
    users = await db.get_all_users()
    out = "Les utilisateurs enregistrés dans la base de données sont :\n\n"
    async for user in users:
        out += f"**Nom :** {user['name']}\n**ID :** `{user['id']}`"
        if user['ban_status']['is_banned']:
            out += ' (Utilisateur banni)'
        if user['verify_status']['is_verified']:
            out += ' (Utilisateur vérifié)'
        out += '\n\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('users.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('users.txt', caption="Liste des utilisateurs")
        await raju.delete()
        os.remove('users.txt')

@Client.on_message(filters.command('chats') & filters.user(ADMINS))
async def list_chats(bot, message):
    raju = await message.reply('Récupération de la liste des chats')
    chats = await db.get_all_chats()
    out = "Les chats enregistrés dans la base de données sont :\n\n"
    async for chat in chats:
        out += f"**Titre :** {chat['title']}\n**ID :** `{chat['id']}`"
        if chat['chat_status']['is_disabled']:
            out += ' (Chat désactivé)'
        out += '\n\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('chats.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('chats.txt', caption="Liste des chats")
        await raju.delete()
        os.remove('chats.txt')
