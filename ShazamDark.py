#
#█▀▄ ▀█ █ █▀█ █░█  █▀▀ ▄▀█ █▄█
#█▄▀ █▄ █ █▀▄ █▄█  █▄█ █▀█ ░█░
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @dziru
# meta pic: https://raw.githubusercontent.com/darkmodules/assets/master/DarkModules.png
# meta banner: https://raw.githubusercontent.com/darkmodules/assets/master/ShazamDark.png
# scope: hikka_min 1.5.0
# scope: hikka_only
# version: 1.0

from .. import utils, loader

@loader.tds
class ShazamDarkMod(loader.Module):
    """Module for searching music's. Works through @lybot"""

    strings = {
        "name": "ShazamDark",
        "dwait": "<emoji document_id=5334922351744132060>😉</emoji> <b>Just wait!</b>",
        "dentersong": "<emoji document_id=5335046240075784593>😠</emoji> <b>Provide the correct Song name!</b>",
        "denterwrong": "<emoji document_id=5335046240075784593>😠</emoji> <b>Provide the Song name!</b>",
        "dsaved": "<emoji document_id=5346032779303854340>😎</emoji> <b>Submitted successfully!</b>",
        }
    
    strings_ru = {
        "dwait": "<emoji document_id=5334922351744132060>😉</emoji> <b>Просто подождите!</b>",
        "dentersong": "<emoji document_id=5335046240075784593>😠</emoji> <b>Укажите правильное название песни!</b>",
        "denterwrong": "<emoji document_id=5335046240075784593>😠</emoji> <b>Укажите название песни!</b>",
        "dsaved": "<emoji document_id=5346032779303854340>😎</emoji> <b>Отправлено успешно!</b>",
        }
    
    strings_uz = {
        "dwait": "<emoji document_id=5334922351744132060>😉</emoji> <b>Shunchaki kuting!</b>",
        "dentersong": "<emoji document_id=5335046240075784593>😠</emoji> <b>To'g'ri Musiqa nomini kiriting!</b>",
        "denterwrong": "<emoji document_id=5335046240075784593>😠</emoji> <b>Musiqa nomini kiriting!</b>",
        "dsaved": "<emoji document_id=5346032779303854340>😎</emoji> <b>Muvaffaqiyatli yuborildi!</b>",
        }
        
    async def client_ready(self, client, db):
        self.db = db
        self.client = client
        dark = await client.get_messages("darkmodules", ids=85)
        await dark.react("👍")
        
    @loader.command(ru_doc="<песня> укажите название")
    async def mcdcmd(self, message):
        """<song> enter name"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not args:
            return await message.edit(self.strings("denterwrong"))
        try:
            music = await message.client.inline_query("lybot", args)
            await message.delete()
            await message.client.send_file(
                message.to_id,
                music[0].result.document,
                caption=self.strings("dsaved"),
                reply_to=reply.id if reply else None,
            )
        except:
            return await message.client.send_message(
                message.chat_id,
                self.strings("dentersong"),
            )