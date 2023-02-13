# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_CHANNEL2:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL2 and FORCE_SUB_GROUP and FORCE_SUB_CHANNEL:
        buttons = [
            [
                InlineKeyboardButton(text="ɢʀᴏᴜᴘ""ᴄʜᴀɴɴᴇʟ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_GROUP and FORCE_SUB_CHANNEL and FORCE_SYB_CHANNEL2:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ""ᴄʜᴀɴɴᴇʟ2", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_CHANNEL2:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ2", url=client.invitelink3),
            ],
            [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_CHANNEL2:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ""ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ2", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL2 and not FORCE_SUB_GROUP and not FORCE_SUB_CHANNEL:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ2", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_GROUP and not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL2:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ GROUP", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink3),
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ2", url=client.invitelink2)
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
