import pyrogram, os, asyncio

try: app_id = int(os.environ.get("app_id", None))
except Exception as app_id: print(f"⚠️ App ID Invalid {app_id}")
try: api_hash = os.environ.get("api_hash", None)
except Exception as api_id: print(f"⚠️ Api Hash Invalid {api_hash}")
try: bot_token = os.environ.get("bot_token", None)
except Exception as bot_token: print(f"⚠️ Bot Token Invalid {bot_token}")
try: ultroid_official = os.environ.get("ultroid_official", "`{ultroid_official}`")
except Exception as ultroid_official: print(f"⚠️ Ultroid_official Name Invalid {ultroid_official}")

ultroid_official = pyrogram.Client(
   name="@ultroid_official", api_id=app_id, api_hash=api_hash, bot_token=bot_token)

started_message = """
<b>Selete 1 Premium Membership 👇</b>"""

start_message = """
This Is Premium purchase Bot
Owned by @ultroid_Official

Check The Premium Plans By Click the Button Below 👇"""

pay_message = """
Pay On This Upi Id 👇
UPI Handle - ---@paytm
Dm - @UltroidxTeam

IMPORTANT - After Payment Send Screenshot Here👇"""

jatin_24x_message = """
Scan The Qr Code Below Button And Send the Screenshot Here👇"""

Info_message = """
हमारे मूवीज चैनल पर परम मूवी-प्रेमी के स्वर्ग का अनुभव करें। एक्शन से भरपूर ब्लॉकबस्टर से लेकर विचारोत्तेजक ड्रामा तक, विभिन्न शैलियों में फैली फिल्मों के विशाल संग्रह में गोता लगाएँ। उपयोगकर्ता के अनुकूल नेविगेशन, व्यक्तिगत अनुशंसाओं और विस्तृत मूवी जानकारी के साथ, हमारा चैनल सिनेमाई आनंद के लिए आपकी पसंदीदा जगह है। हमारे समुदाय से जुड़ें, ताज़ा ख़बरों से अपडेट रहें, और फ़िल्मों के ऐसे जादू का आनंद लें जैसा पहले कभी नहीं हुआ। अपनी उंगलियों पर असीमित मनोरंजन की दुनिया के लिए तैयार हो जाइए! 

💯 हमारे चैनल के गुण 

♻️ सभी ओटी प्लेटफॉर्म मूवी एक ही जगह पर । 

♻️ 5 लाख + फिल्में पहले से ही यहां उपलब्ध हैं ।

♻️ सबसे पहले टेलीग्राम पर नई रिलीज़ हुई मूवी डायरेक्ट वीडियो फॉर्मेट में। 

♻️ रोजाना 50+ मूवी रोजाना अपलोड ।

♻️ 24/7 आपकी सहायता के लिए ग्रुप"""

contact_message = """
Please Click Below Button ✅"""

MovizTube_message = """
Wow!!🤯
You Have Choosen Weekly Bot Membership Of Price ₹19
Choose Payment Method 👇"""

about_message = """
Wow!!🤯
You Have Choosen 1 Month Bot Membership Of Price ₹59
Choose Payment Method 👇"""

ultroidxTeam_message = """
Wow!!🤯
You Have Choosen 6 Month Bot Membership Of Price ₹399
Choose Payment Method 👇"""

Darkpixx_message = """
Wow!!🤯
You Have Choosen 1 Year Bot Membership Of Price ₹699
Choose Payment Method 👇"""

@ultroid_official.on_message(pyrogram.filters.private & pyrogram.filters.command(["start"]))
def start_command(bot, update):
  update.reply(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@ultroid_official.on_message(pyrogram.filters.private & pyrogram.filters.command(["owner"]))
def contact_command(bot, update):
  update.reply(contact_message.format(update.from_user.mention), reply_markup=contact_buttons(bot, update), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@ultroid_official.on_message(pyrogram.filters.private & pyrogram.filters.command(["buy"]))
def started_command(bot, update):
  update.reply(started_message.format(update.from_user.mention), reply_markup=started_buttons(bot, update), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@ultroid_official.on_callback_query(pyrogram.filters.regex("start"))
def strat_callback(bot, update):
  update.message.edit(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@ultroid_official.on_callback_query(pyrogram.filters.regex("owner"))
def strat_callback(bot, update):
  update.message.edit(contact_message.format(update.from_user.mention), reply_markup=contact_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@ultroid_official.on_callback_query(pyrogram.filters.regex("buy"))
def strat_callback(bot, update):
  update.message.edit(started_message.format(update.from_user.mention), reply_markup=started_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)
   
@ultroid_official.on_callback_query(pyrogram.filters.regex("about"))
def about_callback(bot, update): 
  bot = bot.get_me()
  update.message.edit(about_message.format(version=pyrogram.__version__, username=bot.mention), reply_markup=about_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@ultroid_official.on_callback_query(pyrogram.filters.regex("MovizTube"))
def MovizTube_callback(bot, update): 
  bot = bot.get_me()
  update.message.edit(MovizTube_message.format(version=pyrogram.__version__, username=bot.mention), reply_markup=MovizTube_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@ultroid_official.on_callback_query(pyrogram.filters.regex("ultroidxTeam"))
def ultroidxTeam_callback(bot, update): 
  bot = bot.get_me()
  update.message.edit(ultroidxTeam_message.format(version=pyrogram.__version__, username=bot.mention), reply_markup=ultroidxTeam_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@ultroid_official.on_callback_query(pyrogram.filters.regex("Darkpixx"))
def Darkpixx_callback(bot, update): 
  bot = bot.get_me()
  update.message.edit(Darkpixx_message.format(version=pyrogram.__version__, username=bot.mention), reply_markup=Darkpixx_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@ultroid_official.on_callback_query(pyrogram.filters.regex("pay"))
def pay_callback(bot, update): 
  bot = bot.get_me()
  update.message.edit(pay_message.format(version=pyrogram.__version__, username=bot.mention), reply_markup=pay_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@ultroid_official.on_callback_query(pyrogram.filters.regex("jatin_24x"))
def jatin_24x_callback(bot, update): 
  bot = bot.get_me()
  update.message.edit(jatin_24x_message.format(version=pyrogram.__version__, username=bot.mention), reply_markup=jatin_24x_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@ultroid_official.on_callback_query(pyrogram.filters.regex("Info"))
def Info_callback(bot, update): 
  bot = bot.get_me()
  update.message.edit(Info_message.format(version=pyrogram.__version__, username=bot.mention), reply_markup=Info_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)
   
def start_buttons(bot, update):
   bot = bot.get_me()
   buttons = [[
    pyrogram.types.InlineKeyboardButton("⊰⁠⊹ Premium Plans ♪", callback_data="buy"),
    ],[
    pyrogram.types.InlineKeyboardButton("⊰⁠⊹ Check Facility ★", callback_data="Info"),
    ]]
   return pyrogram.types.InlineKeyboardMarkup(buttons)

def contact_buttons(bot, update):
   bot = bot.get_me()
   buttons = [[
    pyrogram.types.InlineKeyboardButton("Contact Owner ✅", url=f"http://t.me/ultroidXTeam"), # Set Orginal Owner Id Username 
    ],[
    pyrogram.types.InlineKeyboardButton("🔺Back ", callback_data="start"),
    ]]
   return pyrogram.types.InlineKeyboardMarkup(buttons)

def started_buttons(bot, update):
  bot = bot.get_me()
  buttons = [[
   pyrogram.types.InlineKeyboardButton("☞ 1 Week : ₹19 ", callback_data="MovizTube"),
   pyrogram.types.InlineKeyboardButton("☞ 1 Month : ₹59 ", callback_data="about"),
   ],[
   pyrogram.types.InlineKeyboardButton("☞ 6 Month : ₹399 ", callback_data="ultroidxTeam"),
   pyrogram.types.InlineKeyboardButton("☞ 1 year : ₹699 ", callback_data="Darkpixx"),
   ],[
   pyrogram.types.InlineKeyboardButton("Get Help", url=f"http://t.me/Chat_Darkpixx_Bot"), # Set your Second Contact Id Link Telegram Bot Username
   ],[
   pyrogram.types.InlineKeyboardButton("🔺Back ", callback_data="start"),
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

def about_buttons(bot, update):
  buttons = [[
   pyrogram.types.InlineKeyboardButton("Pay On Upi", callback_data="pay"),
   ],[
   pyrogram.types.InlineKeyboardButton("Scan QR code", callback_data="jatin_24x"),
   ],[
   pyrogram.types.InlineKeyboardButton("🔺Back ", callback_data="buy"),
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)
   
def MovizTube_buttons(bot, update):
  buttons = [[
   pyrogram.types.InlineKeyboardButton("Pay On Upi", callback_data="pay"),
   ],[
   pyrogram.types.InlineKeyboardButton("Scan QR code", callback_data="jatin_24x"),
   ],[
   pyrogram.types.InlineKeyboardButton("🔺Back ", callback_data="buy"),
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

def Darkpixx_buttons(bot, update):
  buttons = [[
   pyrogram.types.InlineKeyboardButton("Pay On Upi", callback_data="pay"),
   ],[
   pyrogram.types.InlineKeyboardButton("Scan QR code", callback_data="jatin_24x"),
   ],[
   pyrogram.types.InlineKeyboardButton("🔺Back ", callback_data="buy"),
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

def ultroidxTeam_buttons(bot, update):
  buttons = [[
   pyrogram.types.InlineKeyboardButton("Pay On Upi", callback_data="pay"),
   ],[
   pyrogram.types.InlineKeyboardButton("Scan QR code", callback_data="jatin_24x"),
   ],[
   pyrogram.types.InlineKeyboardButton("🔺Back ", callback_data="buy"),
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

def pay_buttons(bot, update):
  buttons = [[
   pyrogram.types.InlineKeyboardButton("Send S-Short", url=f"http://t.me/Chat_Darkpixx_Bot"),
   ],[
   pyrogram.types.InlineKeyboardButton("Get QR code", callback_data="jatin_24x"),
   ],[
   pyrogram.types.InlineKeyboardButton("Change Plan", callback_data="buy"),
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

def jatin_24x_buttons(bot, update):
  buttons = [[
   pyrogram.types.InlineKeyboardButton("QR Code", url=f"https://telegra.ph/file/078426a49ab11b2b4b274.jpg"),
   ],[
   pyrogram.types.InlineKeyboardButton("Send S-Short", url=f"http://t.me/Chat_Darkpixx_Bot"),
   ],[
   pyrogram.types.InlineKeyboardButton("Get Upi Id", callback_data="pay"),
   ],[
   pyrogram.types.InlineKeyboardButton("Change Plan", callback_data="buy"),
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

def Info_buttons(bot, update):
  buttons = [[
   pyrogram.types.InlineKeyboardButton("ᴍᴀᴋᴇ ғɪʀsᴛ ᴘᴜʀᴄʜᴀsᴇ", callback_data="buy"),
   ],[
   pyrogram.types.InlineKeyboardButton("🔺Back ", callback_data="start"),
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

print("𝙘𝙧𝙚𝙯𝙮𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧 𝘽𝙤𝙩 𝘿𝙚𝙥𝙡𝙤𝙮 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡 ✅")
print("𝘽𝙤𝙩 𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝘽𝙮 https://github.com/sahildesai07")

ultroid_official.run()
