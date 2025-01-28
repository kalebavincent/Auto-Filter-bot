class script(object):

    START_TXT = """<b>ʜᴇʏ<spoiler> {} </spoiler>, <i>{}</i>
    
ᴊᴇ sᴜɪs ᴜɴ ᴘᴜɪssᴀɴᴛ ʙᴏᴛ ᴅᴇ ғɪʟᴛʀᴀɢᴇ ᴀᴜᴛᴏᴍᴀᴛɪǫᴜᴇ ᴀᴠᴇᴄ ᴜɴ ʀᴀᴄᴄᴏᴜʀᴄɪssᴇᴜʀ ᴅᴇ ʟɪᴇɴs. ᴠᴏᴜs ᴘᴏᴜᴠᴇᴢ ᴍ'ᴜᴛɪʟɪsᴇʀ ᴄᴏᴍᴍᴇ ғɪʟᴛʀᴇ ᴀᴜᴛᴏᴍᴀᴛɪǫᴜᴇ ᴀᴠᴇᴄ ᴜɴ ʀᴀᴄᴄᴏᴜʀᴄɪssᴇᴜʀ ᴅᴇ ʟɪᴇɴs ᴅᴀɴs ᴠᴏᴛʀᴇ ɢʀᴏᴜᴘᴇ... ᴄ'ᴇsᴛ ғᴀᴄɪʟᴇ ᴀ̀ ᴜᴛɪʟɪsᴇʀ, ɪʟ sᴜғғɪᴛ ᴅᴇ ᴍ'ᴀᴊᴏᴜᴛᴇʀ ᴇɴ ᴛᴀɴǫᴜᴇ ǫᴜ'ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴇᴜʀ ᴅᴀɴs ᴠᴏᴛʀᴇ ɢʀᴏᴜᴘᴇ ᴇᴛ ᴊᴇ ғᴏᴜʀɴɪʀᴀɪ ᴅᴇs ғɪʟᴍs ᴀᴠᴇᴄ ᴠᴏᴛʀᴇ ʀᴀᴄᴄᴏᴜʀᴄɪssᴇᴜʀ ᴅᴇ ʟɪᴇɴs... ♻️</b>"""


    MY_ABOUT_TXT = """★ sᴇʀᴠᴇᴜʀ : <a href=https://www.heroku.com>ʜᴇʀᴏᴋᴜ</a>  
★ ʙᴀsᴇ ᴅᴇ ᴅᴏɴɴᴇ́ᴇs : <a href=https://www.mongodb.com>ᴍᴏɴɢᴏᴅʙ</a>  
★ ʟᴀɴɢᴀɢᴇ : <a href=https://www.python.org>ᴘʏᴛʜᴏɴ</a>  
★ ʙɪʙʟɪᴏᴛʜᴇ̀ǫᴜᴇ : <a href=https://pyrogram.org>ᴘʏʀᴏɢʀᴀᴍ</a>"""

    MY_OWNER_TXT = """★ Nᴀᴍᴇ: Hʏᴏsʜᴄᴏᴅᴇʀ  
★ Uѕᴇʀɴᴀᴍᴇ: @hyoshcoder  
★ Cᴏᴜɴᴛʀʏ: Cᴏɴɢᴏ ᴄᴅ"""

    STATUS_TXT = """🗂 Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>  
👤 Tᴏᴛᴀʟ Uѕᴇʀs: <code>{}</code>  
👥 Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>  
🤑 Pʀᴇᴍɪᴜᴍ Uѕᴇʀs: <code>{}</code>  
✨ Uѕᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code>  
🗳 Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code>  
🚀 Bᴏᴛ Uᴘᴛɪᴍᴇ: <code>{}</code>"""

    NEW_GROUP_TXT = """#NᴇᴡGʀᴏᴜᴘ  
Tɪᴛʟᴇ - {}  
ID - <code>{}</code>  
Uѕᴇʀɴᴀᴍᴇ - {}  
Tᴏᴛᴀʟ - <code>{}</code>"""

    NEW_USER_TXT = """#NouvelUtilisateur
★ Nom : {}
★ ID : <code>{}</code>
"""

    NOT_FILE_TXT = """👋 ʙᴏɴᴊᴏᴜʀ {},

Je ɴᴇ ᴛʀᴏᴜᴠᴇ ᴘᴀs ʟᴇ <b>{}</b> dans ᴍᴀ ʙᴀsᴇ ᴅᴇ ᴅᴀᴛᴀʙᴀsᴇ ! 🥲

👉 Fᴀɪᴛᴇs ᴜɴᴇ ʀᴇʜᴇʀᴄʜᴇ sᴜʀ Gᴏᴏɢʟᴇ et vᴇʀɪғɪᴇᴢ qᴜᴇ vᴏᴛʀᴇ ᴏʀᴛʜᴏɢʀᴀᴘʜᴇ esᴛ cᴏʀʀᴇᴄᴛᴇ.
👉 Vᴇʀɪғɪᴇᴢ ʟᴇs ɪɴsᴛʀᴜᴄᴛɪᴏɴs pᴏᴜʀ ᴏʙᴛᴇɴɪʀ ᴅᴇ ʙᴇᵗᴛʀᴇs ʀᴇsᴜʟᴛᴀᴛs.
👉 ᴏᴜ ʟᴇ ɴᴏᴍ ᴘᴇᴜᴛ-ᴇᴛʀᴇ ᴇɴᴄᴏʀᴇ ᴘᴜʙʟɪᴇ.
"""
    
    EARN_TXT = """<b>COMMENT GAGNER DE L'ARGENT AVEC CE BOT

➥ MAINTENANT, VOUS POUVEZ AUSSI GAGNER DE L'ARGENT EN UTILISANT CE BOT.

» ÉTAPE 1 : Ajoutez ce bot dans votre groupe avec des permissions d'administrateur.

» ÉTAPE 2 : Créez un compte sur <a href=https://telegram.me/how_to_download_channel/14>mdisklink.link</a> [ Vous pouvez également utiliser un autre site de raccourcissement ]

» ÉTAPE 3 : Cliquez sur le bouton ci-dessous pour savoir comment connecter votre raccourcisseur avec ce bot.

➥ CE BOT EST GRATUIT POUR TOUS, VOUS POUVEZ L'UTILISER DANS VOS GROUPES GRATUITEMENT.</b>
"""

    HOW_TXT = """<b><b>COMMENT CONNECTER VOTRE PROPRE RACCORCISSEUR ‼️

➥ SI VOUS SOUHAITEZ CONNECTER VOTRE PROPRE RACCORCISSEUR, ENVOYEZ SIMPLEMENT LES DÉTAILS DONNÉS DANS LE FORMAT CORRECT DANS VOTRE GROUPE

➥ FORMAT ↓↓↓

<code>/set_shortlink site_raccourcisseur api_raccourcisseur</code>

➥ EXEMPLE ↓↓↓

<code>/set_shortlink mdisklink.link 5843c3cc645f5077b2200a2c77e0344879880b3e</code>

➥ SI VOUS VOULEZ SAVOIR QUEL RACCORCISSEUR VOUS AVEZ CONNECTÉ À VOTRE GROUPE, ENVOYEZ CETTE COMMANDE AU GROUPE /get_shortlink

📝 NOTE : Vous ne devez pas être un administrateur anonyme dans le groupe. Envoyez la commande sans être un administrateur anonyme.</b>
"""

    IMDB_TEMPLATE = """✅ J'ai trouvé : <code>{query}</code>

🏷 Titre : <a href={url}>{title}</a>
🎭 Genres : {genres}
📆 Année : <a href={url}/releaseinfo>{year}</a>
🌟 Note : <a href={url}/ratings>{rating} / 10</a>
☀️ Langues : {languages}
📀 Durée : {runtime} Minutes

🗣 Demandé par : {message.from_user.mention}
©️ Propulsé par : <b>{message.chat.title}</b>
"""

    FILE_CAPTION = """<i>{file_name}</i>

🚫 VEUILLEZ CLIQUER SUR LE BOUTON FERMER SI VOUS AVEZ VU LE FILM 🚫
"""

    WELCOME_TEXT = """👋 Bonjour {mention}, Bienvenue dans le groupe {title} ! 💞"""

    HELP_TXT = """<b>Note - <spoiler>Essayez chaque commande sans argument pour voir plus de détails 😹</spoiler></b>"""
    
    ADMIN_COMMAND_TXT = """<b>Voici les commandes administratives 👇
/index_channels - vérifier le nombre d'ID de chaîne indexés ajoutés
/stats - obtenir le statut du bot
/delete - supprimer des fichiers en utilisant une requête
/delete_all -supprimer tous les fichiers indexés
/broadcast - envoyer un message à tous les utilisateurs du bot
/grp_broadcast - envoyer un message à tous les groupes
/pin_broadcast - envoyer un message épinglé à tous les utilisateurs du bot
/pin_grp_broadcast - envoyer un message épinglé à tous les groupes
/restart - redémarrer le bot
/leave - faire quitter le bot d'un groupe particulier
/unban_grp - activer un groupe
/ban_grp - désactiver un groupe
/ban_user - bannir un utilisateur du bot
/unban_user - débannir un utilisateur du bot
/users - obtenir les détails de tous les utilisateurs
/chats - obtenir tous les groupes
/invite_link - générer un lien d'invitation
/set_pm_search - activer/désactiver la recherche en PM
/index - indexer les chaînes accessibles par le bot</b>
"""
    
    USER_COMMAND_TXT = """<b>Voici les commandes utilisateur du bot 👇

/start - pour vérifier si le bot est vivant ou non
/settings - pour modifier les paramètres du groupe à votre guise
/set_template - pour définir un modèle IMDb personnalisé
/set_caption - pour définir une légende personnalisée pour les fichiers du bot
/set_shortlink - l'administrateur du groupe peut définir un raccourcisseur personnalisé
/get_custom_settings - pour obtenir les détails des paramètres de votre groupe
/set_welcome - pour définir un message de bienvenue personnalisé pour les nouveaux membres du groupe
/set_tutorial - pour définir un lien de tutoriel personnalisé dans le bouton de la page de résultats
/id - pour vérifier l'ID du groupe ou du canal
/set_fsub - pour définir les chaînes de souscription forcée
/remove_fsub - pour supprimer toutes les chaînes de souscription forcée</b>
"""
    
    SOURCE_TXT = """<b>RÉPONSITIORE GITHUB DU BOT -

- CE BOT EST UN PROJET OPEN SOURCE.

- SOURCE - <a href=https://github.com/HA-Bots/Auto-Filter-Bot>ICI</a>

- DÉVELOPPEUR - @HA_Bots
"""

    PREMIUM_PLAN_TEXT = """<b><i><u>- PLANS DISPONIBLES - </u>

- 30Rs - 1 SEMAINE
- 50Rs - 1 MOIS
- 120Rs - 3 MOIS
- 220Rs - 6 MOIS

<u>🎁 CARACTÉRISTIQUES PREMIUM 🎁</u>

○ PAS BESOIN DE VÉRIFIER
○ PAS BESOIN D'OUVRIR LE LIEN
○ FICHIERS DIRECTS
○ EXPÉRIENCE SANS PUBLICITÉ
○ LIEN DE TÉLÉCHARGEMENT HAUTE VITESSE
○ FILMS ET SÉRIES ILLIMITÉS
○ SUPPORT ADMIN COMPLET
○ LES DEMANDES SERONT COMPLÉTÉES EN 1H SI DISPONIBLES

✨ UPI ID - <code>{ID UPI}</code>

CLIQUEZ POUR VÉRIFIER VOTRE PLAN ACTIF /myplan

💢 VOUS DEVEZ ENVOYER UNE CAPTURE D'ÉCRAN APRÈS PAIEMENT

‼️ APRÈS AVOIR ENVOYÉ UNE CAPTURE D'ÉCRAN, VEUILLEZ NOUS LAISSER UN PEU DE TEMPS POUR VOUS AJOUTER À LA LISTE PREMIUM</i></b>
"""


