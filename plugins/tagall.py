import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ "Hey bébé, où es-tu 🤗🥱",
    "Hé, t'as dormi ? Viens en ligne 😊",
    "Viens en vocal, on parle un peu 😃",
    "As-tu mangé ? 🥲",
    "Comment va tout le monde à la maison ? 🥺",
    "Tu sais, tu me manquais beaucoup 🤭",
    "Alors, comment ça va ? 🤨",
    "Tu vas m'arranger un coup ? 🙂",
    "Comment tu t'appelles ? 🥲",
    "As-tu pris ton petit-déjeuner ? 😋",
    "Prends-moi dans ton groupe, je veux être kidnappé 😍",
    "Ton partenaire te cherche, viens vite en ligne 😅😅",
    "Tu veux être mon ami ? 🤔",
    "T'es allé dormir ? 🙄🙄",
    "Joue une chanson, s'il te plaît 😕",
    "Tu viens d'où ? 🙃",
    "Hello, Namaste 😛",
    "Hello bébé, comment ça va ? 🤔",
    "Tu sais qui est mon propriétaire ?",
    "Allons jouer à un jeu 🤗",
    "Alors, comment ça va, bébé ? 😇",
    "Que fait ta maman ? 🤭",
    "Tu veux discuter avec moi ? 🥺🥺",
    "Hé, fou, viens en ligne 😶",
    "C'est un jour férié à l'école aujourd'hui ? 🤔",
    "Hé, bon matin 😜",
    "Écoute, j'ai une faveur à te demander 🙂",
    "Joue une chanson, s'il te plaît 😪",
    "Enchanté de te rencontrer ☺",
    "Salut 🙊",
    "Tu as fini tes études ? 😺",
    "Dis-moi quelque chose, stp 🥲",
    "Qui est Sonali... ?? 😅",
    "Peux-je avoir une photo de toi ? 😅",
    "Ta maman est là ? 😆😆😆",
    "Alors, comment va ta femme ? 😉",
    "Je t'aime 🙈🙈🙈",
    "Tu m'aimes ? 👀",
    "Quand tu vas attacher ta Rakhi ? 🙉",
    "Je te chante une chanson ? 😹",
    "Viens en ligne, je te chante une chanson 😻",
    "Tu utilises Instagram ? 🙃",
    "Tu me donnes ton numéro WhatsApp ? 😕",
    "Quel genre de musique tu aimes ? 🙃",
    "Est-ce que tout est fini pour toi ? 🙃",
    "D'où viens-tu ? 😊",
    "Écoute-moi 🧐",
    "Peux-tu faire un petit service pour moi ?",
    "Bye, mais ne parle plus avec moi après aujourd'hui 😠",
    "Comment vont tes parents ? ❤",
    "Que se passe-t-il ? 👱",
    "Tu me manques beaucoup 🤧❣️",
    "Tu m'as oublié 😏😏",
    "Tu ne devrais pas mentir 🤐",
    "Ne fais pas d'histoires maintenant 😒",
    "Que s'est-il passé ? 😮😮",
    "Salut 👀",
    "Aapk...",
    " **Votre ami(e) comme vous, me manque beaucoup 🙈** ",
    " **Aujourd'hui, je suis triste ☹️** ",
    " **Parles-moi s'il te plaît 🥺🥺** ",
    " **Que fais-tu en ce moment 👀** ",
    " **Comment ça va ? 🙂** ",
    " **D'où viens-tu..?🤔** ",
    " **Viens discuter avec moi..🥺** ",
    " **Je suis innocent(e) 🥺🥺** ",
    " **Hier c'était super amusant 🤭😅** ",
    " **Pourquoi ne parles-tu pas dans le groupe ? 😕** ",
    " **Es-tu en couple ? 👀** ",
    " **Tu es vraiment discret(ète) 😼** ",
    " **Tu sais chanter ? 😸** ",
    " **On va sortir un peu..? 🙈** ",
    " **Sois heureux(se) ✌️🤞** ",
    " **On peut être amis🥰** ",
    " **Pourquoi tu ne parles pas ? 🥺🥺** ",
    " **Ajoute quelques membres 🥲** ",
    " **Es-tu célibataire ou en couple ? 😉** ",
    " **Viens, on fait la fête 😋🥳** ",
    " **Hé, salut 🧐** ",
    " **Tu m'as oublié(e) ? 🥺** ",
    " **Viens ici :- [ @Hyoshcoder ] On va s'amuser 🤭🤭** ",
    " **Tu veux jouer à Truth and Dare ? 😊** ",
    " **Aujourd'hui, maman m'a grondé(e) 🥺🥺** ",
    " **Rejoins-nous ici :- [ @Hyoshcoder ] 🤗** ",
    " **Un cœur, c'est tout ce qu'il faut 😗😗** ",
    " **Où est ton ami(e) ? 🥺** ",
    " **Mon adorable propriétaire [ @Hyoshcoder ] 🥰** ",
    " **Où es-tu allé(e), mon cher(e) ? 😜** ",
    " **Bonne nuit, c'était une longue soirée 🥰** ",
           ]

@Client.on_message(filters.command(["tagall", "spam", "tagmember", "utag", "stag", "hftag", "bstag", "eftag", "tag", "etag", "utag", "atag"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("Cette commande est uniquement pour les groupes.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("Tu n'es pas administrateur, seul les administrateurs peuvent le faire.")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall Tapez comme ceci / Répondez à n'importe quel message la prochaine fois.")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall Tapez comme ceci / Répondez à n'importe quel message la prochaine fois...")
    else:
        return await message.reply("/tagall Tapez comme ceci / Répondez à n'importe quel message la prochaine fois ..")
    if chat_id in spam_chats:
        return await message.reply("Veuillez d'abord arrêter le processus en cours ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@Client.on_message(filters.command(["tagoff", "tagstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("Actuellement je ne fais pas ça ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("Tu n'es pas administrateur, seul les administrateurs peuvent taguer les membres.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦STOP♦")

