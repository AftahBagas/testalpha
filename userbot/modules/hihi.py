from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=r"^\.hihi$")
async def sayhi(e):
    await e.edit(
        "\nđşâ¨â¨đşâ¨đşđşđş"
        "\nđşâ¨â¨đşâ¨â¨đşâ¨"
        "\nđşđşđşđşâ¨â¨đşâ¨"
        "\nđşâ¨â¨đşâ¨â¨đşâ¨"
        "\nđşâ¨â¨đşâ¨đşđşđş"
        "\nâď¸âď¸âď¸âď¸âď¸âď¸âď¸âď¸")


CMD_HELP.update({
    "hihi":
    "đ **Cmd** : `.hihi`\
    \nđ **Descriptions** : pesan untuk hiiiiiiii."
})
