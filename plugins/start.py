from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/VKPROJECTS")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/VKPBOTS")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n__NOW SENT ME A YOUTUBE VIDEO LINK /help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
