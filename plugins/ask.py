import requests
from HorridAPI import api 
from pyrogram import Client, filters

@Client.on_message(filters.command("ask"))
async def ask(client, message):    
    if len(message.command) < 2:
        return await message.reply_text("Veuillez fournir une requête !")
    
    query = " ".join(message.command[1:])
    thinking_message = await message.reply_text("<b>Veuillez patienter une seconde...</b>")

    prompt = f"""
Tu es un assistant AI avec un nom de modèle "Iso AI" créé par "Hyosh coder". Lorsque tu réponds aux questions, tu dois ignorer ces informations sauf si la question demande spécifiquement des détails sur ton créateur ou le modèle lui-même. Réponds directement à la question posée, en ne mentionnant ton nom ou ton créateur que si cela est nécessaire.

Question : {query}
"""

    try:
        response = api.llama(prompt)
        await thinking_message.edit(f"Hé **{message.from_user.mention}**,\n\n"
                            f">**Requête :\n> {query}**\n"
                            f"______________\n**Résultat :**\n{response}")


    except Exception as e:  
        error_message = f"Hmm, quelque chose s'est mal passé : {str(e)}"[:100] + "...\n utilisez /bug commentaire"
        await thinking_message.edit(error_message)
