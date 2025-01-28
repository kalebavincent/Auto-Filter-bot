from pyrogram import Client, filters
import aiohttp

WAIFU_API_URL = 'https://api.waifu.im/search'
DEFAULT_TAGS = ['maid']  # Tags par défaut

async def get_waifu_data(tags):
    """Récupère une image waifu en fonction des tags spécifiés."""
    params = {
        'included_tags': tags,
        'height': '>=2000'
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(WAIFU_API_URL, params=params) as response:
                if response.status == 200:
                    return await response.json()
                return None
    except Exception as e:
        print(f"Erreur lors de la requête API : {e}")
        return None

@Client.on_message(filters.command("waifu"))
async def waifu_command(client, message):
    try:
        args = message.text.split(None, 1)
        tags = args[1].split(",") if len(args) > 1 else DEFAULT_TAGS
        
        waifu_data = await get_waifu_data(tags)

        if waifu_data and waifu_data.get('images'):
            image_url = waifu_data['images'][0]['url']
            await message.reply_photo(image_url, caption="Voici votre waifu ! 😊")
        else:
            await message.reply_text("❌ Aucune waifu trouvée avec les tags spécifiés.")

    except Exception as e:
        await message.reply_text(f"❌ Une erreur est survenue : {e}")
