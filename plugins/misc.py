from info import *
from utils import *
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 

@Client.on_message(filters.command("start") & ~filters.channel)
async def start(bot, message):
    await add_user(message.from_user.id, message.from_user.first_name)
    await message.reply(text=script.START.format(message.from_user.mention),
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⇄  ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ  ⇄', url=f'http://telegram.me/Movies_villa_post_search_bot?startgroup=true')
            ],[InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/movies_villa_backup"),

InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="misc_help")],[InlineKeyboardButton('❂   ᴏᴜʀ  ᴜᴘᴅᴀᴛᴇꜱ  ᴄʜᴀɴɴᴇʟ   ❂', url=f'https://t.me/movies_villa_backup')]]))  
@Client.on_message(filters.command("help"))
async def help(bot, message):
    await message.reply(text=script.HELP,
                        disable_web_page_preview=True)

@Client.on_message(filters.command("about"))
async def about(bot, message):
    await message.reply(text=script.ABOUT.format((await bot.get_me()).mention),
                        disable_web_page_preview=True)

@Client.on_message(filters.command("stats") & filters.user(ADMIN))
async def stats(bot, message):
    g_count, g_list = await get_groups()
    u_count, u_list = await get_users()
    await message.reply(script.STATS.format(u_count, g_count))

@Client.on_message(filters.command("id"))
async def id(bot, message):
    text = f"<b>➲  ᴄʜᴀᴛ ɪᴅ:-</b>  `{message.chat.id}`\n"
    if message.from_user:
       text += f"<b>➲  ʏᴏᴜʀ ɪᴅ:-</b> `{message.from_user.id}`\n"
    if message.reply_to_message:
       if message.reply_to_message.from_user:
          text += f"<b>➲  ʀᴇᴘʟɪᴇᴅ ᴜꜱᴇʀ ɪᴅ:-</b> `{message.reply_to_message.from_user.id}`\n"
       if message.reply_to_message.forward_from:
          text += f"<b>➲  ʀᴇᴘʟɪᴇᴅ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀᴡᴀʀᴅ ꜰʀᴏᴍ ᴜꜱᴇʀ ɪᴅ:-</b> `{message.reply_to_message.forward_from.id}`\n"
       if message.reply_to_message.forward_from_chat:
          text += f"<b>➲  ʀᴇᴘʟɪᴇᴅ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀᴡᴀʀᴅ ꜰʀᴏᴍ ᴄʜᴀᴛ ɪᴅ:-</b> `{message.reply_to_message.forward_from_chat.id}\n`"
    await message.reply(text)

@Client.on_callback_query(filters.regex(r"^misc"))
async def misc(bot, update):
    data = update.data.split("_")[-1]
    if data=="home":
       await update.message.edit(text=script.START.format(update.from_user.mention),
                                 disable_web_page_preview=True,
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⇄  ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ  ⇄', url=f'http://telegram.me/Movies_villa_post_search_bot?startgroup=true')
            ],[InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/Movies_villae"),

InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="misc_help")],[InlineKeyboardButton('❂   ᴏᴜʀ  ᴜᴘᴅᴀᴛᴇꜱ  ᴄʜᴀɴɴᴇʟ   ❂', url=f'https://t.me/Hindi_movies_villa')]])) 
    elif data=="help":
       await update.message.edit(text=script.HELP, 
                                 disable_web_page_preview=True,
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🧑‍💻   ᴄᴏɴᴛᴀᴄᴛ  ᴛᴏ  ᴏᴡɴᴇʀ   🧑‍💻',url='https://t.me/ROYAL_GAGAN_DEEP_SINGH_MEHRA')],[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="misc_home"),InlineKeyboardButton("ɴᴇxᴛ", url="https://t.me/Punjabi_movies_villa")]])) 


    elif data=="about":
        await update.message.edit(text=script.ABOUT.format((await bot.get_me()).mention), 
                                  disable_web_page_preview=True,
                                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="misc_home")]]))
         
@Client.on_message(filters.command("follow"))
async def follow_msg(bot, message):
    btn = [[
        InlineKeyboardButton(text="ᴛᴡɪᴛᴛᴇʀ", url="https://t.me/ROYAL_GAGAN_DEEP_SINGH_MEHRA"),
        InlineKeyboardButton(text="ɪɴꜱᴛᴀɢʀᴀᴍ", url="https://t.me/ROYAL_GAGAN_DEEP_SINGH_MEHRA")
        ],[
        InlineKeyboardButton(text="ɢɪᴛʜᴜʙ  ᴀᴄᴄᴏᴜɴᴛ", url="https://github.com/ROYAL-JATT")
    ],[
        InlineKeyboardButton(text="ᴏᴜʀ  ᴏꜰꜰɪᴄɪᴀʟ  ᴡᴇʙꜱɪᴛᴇ", url="https://t.me/ROYAL_GAGAN_DEEP_SINGH_MEHRA")
    ],[
        InlineKeyboardButton(text="ꜱᴜʙꜱᴄʀɪʙᴇ  ᴏᴜʀ  ʏᴛ  ᴄʜᴀɴɴᴇʟ", url="https://youtube.com/@Official_punjabi_movies_hd?si=fMczyyv52dTXWwJ2")
    ],[
        InlineKeyboardButton(text="ʀᴇᴠɩᴇᴡꜱ", url="https://t.me/Punjabi_movies_villa"),
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇꜱ", url="https://t.me/movies_villa_backup")
    ]]
    yt = await message.reply_photo(photo='https://telegra.ph/file/b681d379605d3d3a9fa1c.jpg', caption="<b>ᴏᴜʀ  ꜱᴏᴄɪᴀʟ  ᴍᴇᴅɪᴀ  ᴘʟᴀᴛꜰᴏʀᴍꜱ</b>", reply_markup=InlineKeyboardMarkup(btn))
    await asyncio.sleep(500)
    await yt.delete()
    await message.delete()

@Client.on_message(filters.private & filters.text & filters.incoming)
async def pm_text(bot, message):
    content = message.text
    user = message.from_user.first_name
    user_id = message.from_user.id
    if content.startswith("/") or content.startswith("#"): return  # ignore commands and hashtags
    await message.reply_text(
         text="<b>ʜʏ,\n\nɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴏᴠɪᴇs / sᴇʀɪᴇs ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ꜰɪʀsᴛ ʙᴜᴛᴛᴏɴ ᴏʀ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ɪɴ ʙᴏᴛ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ sᴇᴄᴏɴᴅ ʙᴜᴛᴛᴏɴ</b>",   
         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝  ʀᴇǫᴜᴇsᴛ ʜᴇʀᴇ​ ", url=f"https://t.me/Movies_villae")],[InlineKeyboardButton("🧑‍💻  ʙᴏᴛ ᴏᴡɴᴇʀ ", url=f"https://t.me/ROYAL_GAGAN_DEEP_SINGH_MEHRA")]]), disable_web_page_preview=True
    )
    await bot.send_message(
        chat_id=LOG_CHANNEL,
        text=f"<b>#𝐌𝐒𝐆\n\nNᴀᴍᴇ : {user}\n\nID : {user_id}\n\nMᴇssᴀɢᴇ : {content}</b>"
    )

@Client.on_message(filters.command("start") & ~filters.channel)
async def start(bot, message):
    await add_user(message.from_user.id, message.from_user.first_name)
    await message.reply(text=script.START.format(message.from_user.mention),
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Bᴜʏ Sᴜʙsᴄʀɪᴘᴛɪᴏɴ', callback_data="misc_buymoney")]]))
                                                         
   
 
@Client.on_message(filters.command("help"))
async def help(bot, message):
    await message.reply(text=script.HELP, 
                        disable_web_page_preview=True)

@Client.on_message(filters.command("stats") & filters.user(ADMIN))
async def stats(bot, message):
    g_count, g_list = await get_groups()
    u_count, u_list = await get_users()
    await message.reply(script.STATS.format(u_count, g_count))

@Client.on_message(filters.command("id"))
async def id(bot, message):
    text = f"Current Chat ID: `{message.chat.id}`\n"
    if message.from_user:
       text += f"Your ID: `{message.from_user.id}`\n"
    if message.reply_to_message:
       if message.reply_to_message.from_user:
          text += f"Replied User ID: `{message.reply_to_message.from_user.id}`\n"
       if message.reply_to_message.forward_from:
          text += f"Replied Message Forward from User ID: `{message.reply_to_message.forward_from.id}`\n"
       if message.reply_to_message.forward_from_chat:
          text += f"Replied Message Forward from Chat ID: `{message.reply_to_message.forward_from_chat.id}\n`"
    await message.reply(text)

@Client.on_callback_query(filters.regex(r"^misc"))
async def misc(bot, update):
    data = update.data.split("_")[-1]
    if data == "home":
        await update.message.edit(
            text=script.START.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ʜᴇʟᴘ", callback_data="misc_help"),
                                                InlineKeyboardButton("ʙᴜʏ", callback_data="misc_buymoney")]])
        )
    elif data == "help":
        await update.message.edit(
            text=script.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Bᴀᴄᴋ", callback_data="misc_home")]])
        )
    elif data == "buymoney":
        await update.message.edit(
            text=script.BUY.format((await bot.get_me()).mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("QR ᴄᴏᴅᴇ", callback_data="buy_qr")],[
         InlineKeyboardButton("UPI ɪᴅ", callback_data="buy_upi")],[
         InlineKeyboardButton("Mᴅɪsᴋ Vɪᴇᴡs", callback_data="buy_mdisk")]
    ])) 

         
@Client.on_message(filters.command("buy"))
async def buy(bot, message):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("QR ᴄᴏᴅᴇ", callback_data="buy_qr")],[
            InlineKeyboardButton("UPI ɪᴅ", callback_data="buy_upi")],[
            InlineKeyboardButton("Mᴅɪsᴋ Vɪᴇᴡs", callback_data="buy_mdisk")]
        ])
        await message.reply("Hᴏᴡ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴘᴀʏ?", reply_markup=keyboard)


@Client.on_callback_query(filters.regex(r"^buy"))
async def process_buy(bot, update):
    data = update.data.split("_")[-1]
    if data == "qr":
        # send photo
        photo_url = f"{UPI_PIC}"  # replace with your QR image URL
        await bot.send_photo(chat_id=update.message.chat.id, photo=photo_url)
        text = "Pᴀʏ 𝟸𝟶 Rᴜᴘᴘᴇ ᴀɴᴅ ᴛʜᴇɴ sᴇɴᴅ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴏғ ᴛʜᴇ ᴘᴀʏᴍᴇɴᴛ ʙᴇʟᴏᴡ, ᴀɴᴅ ᴀʟsᴏ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ID sᴏ I ᴄᴀɴ ᴠᴇʀɪғʏ Aғᴛᴇʀ Sᴇɴᴅɪɴɢ Vᴇʀɪғɪᴄᴀᴛɪᴏɴ Rᴇǫᴜᴇsᴛ."
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Sᴇɴᴅ Sᴄʀᴇᴇɴsʜᴏᴛ", url=f'https://t.me/{OWNER_USERNAME}')]
        ])
        await bot.send_message(chat_id=update.message.chat.id, text=text, reply_markup=keyboard)
    elif data == "upi":
        # send message and button
        text = "'sᴏʀʀʏ\nPᴀʏ' 20 Rᴜᴘᴘᴇ Oɴ `sm7355423@okhdfcbank` ᴀɴᴅ ᴛʜᴇɴ sᴇɴᴅ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴏғ ᴛʜᴇ ᴘᴀʏᴍᴇɴᴛ ʙᴇʟᴏᴡ, ᴀɴᴅ ᴀʟsᴏ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ID Aғᴛᴇʀ Sᴇɴᴅɪɴɢ Vᴇʀɪғɪᴄᴀᴛɪᴏɴ Rᴇǫᴜᴇsᴛ. ᴄᴀɴ ᴠᴇʀɪғʏ ᴛʜᴇ ᴘᴀʏᴍᴇɴᴛ."
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Sᴇɴᴅ Sᴄʀᴇᴇɴsʜᴏᴛ", url=f'https://t.me/{OWNER_USERNAME}')]
        ])
        await bot.send_message(chat_id=update.message.chat.id, text=text, reply_markup=keyboard)
    elif data == "mdisk":
        # send message and button
        text = "Sᴇɴᴅ 2000 Mᴅɪsᴋ Vɪᴇᴡs Tᴏ 6651109872 ᴀɴᴅ ᴛʜᴇɴ sᴇɴᴅ ᴀ Mᴇssᴀɢᴇ Tᴏ Tʜᴇ Bᴏᴛ Oᴡɴᴇʀ."
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Message", url=f'https://t.me/{OWNER_USERNAME}')]
        ])
        await bot.send_message(chat_id=update.message.chat.id, text=text, reply_markup=keyboard)

 
@Client.on_message(filters.command('leave') & filters.private &  filters.chat(ADMIN))
async def leave_a_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Gɪᴠᴇ ᴍᴇ ᴀ ᴄʜᴀᴛ ɪᴅ')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        buttons = [[
            InlineKeyboardButton('𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url=f'https://t.me/{OWNER_USERNAME}')
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat,
            text='<b>Hᴇʟʟᴏ Fʀɪᴇɴᴅs, \nMʏ ᴀᴅᴍɪɴ ʜᴀs ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ɢʀᴏᴜᴘ sᴏ ɪ ɢᴏ! Iғ ʏᴏᴜ ᴡᴀɴɴᴀ ᴀᴅᴅ ᴍᴇ ᴀɢᴀɪɴ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ Oᴡɴᴇʀ.</b>',
            reply_markup=reply_markup,
        )

        await bot.leave_chat(chat)
        await message.reply(f"ʟᴇғᴛ ᴛʜᴇ ᴄʜᴀᴛ `{chat}`")
    except Exception as e:
        await message.reply(f'Error - {e}')

@Client.on_message(filters.command("gsend") & filters.private &  filters.chat(ADMIN))
async def send_chatmsg(bot, message):
    if message.reply_to_message:
        target_id = message.text
        command = ["/gsend"]
        for cmd in command:
            if cmd in target_id:
                target_id = target_id.replace(cmd, "")
        success = False
        try:
            chat = await bot.get_chat(int(target_id))
            await message.reply_to_message.copy(int(chat.id))
            success = True
        except Exception as e:
            await message.reply_text(f"<b>Eʀʀᴏʀ :- <code>{e}</code></b>")
        if success:
            await message.reply_text(f"<b>Yᴏᴜʀ Mᴇssᴀɢᴇ Hᴀs Bᴇᴇɴ Sᴜᴄᴇssғᴜʟʟʏ Sᴇɴᴅ To {chat.id}.</b>")
        else:
            await message.reply_text("<b>Aɴ Eʀʀᴏʀ Oᴄᴄᴜʀʀᴇᴅ !</b>")
    else:
        await message.reply_text("<b>Cᴏᴍᴍᴀɴᴅ Iɴᴄᴏᴍᴘʟᴇᴛᴇ...</b>")

@Client.on_chat_join_request(filters.group | filters.channel)
async def autoapprove(client, message: ChatJoinRequest):
    chat = message.chat 
    user = message.from_user 
    print(f"{user.first_name} Jᴏɪɴᴇᴅ (ᴀᴘᴘʀᴏᴠᴇᴅ)") 
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVE == "on":
        await client.send_message(chat_id=chat.id, text=APPROVETEXT.format(mention=user.mention, title=chat.title))
