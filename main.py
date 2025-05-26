import asyncio, random
from telethon import TelegramClient, events

# Telegram config
api_id = 23593382
api_hash = '4b73f8a581a09927e3ee82a05bf1ecac'
session_name = 'Cyb_Exploit'

client = TelegramClient(session_name, api_id, api_hash)

OWNER_ID = 7750987859
sudo_users = set()
allowed_users = {OWNER_ID}

target_id = None
target_mention = None
auto_reply_enabled = False
active_count_target = None

bhai_msgs = [ "Tera dard mera dard hai bhai.",
    "Bhabhi ke haath ka khana khilwado voi.",
    "Tere jaisa bhai har kisi ko mile, yahi dua hai.",
    "Bhai ke liye jaan bhi haazir hai.",
    "Aur btao bhaiya bhabhi kaisi hai.",
    "Kisne maa chudai tu bta bhai gand me haath chada duga unki.",
    "Gand mar duga tujko kisi ne kuch bola to.",
    "Bhai ke saath ladayi ho sakti hai, dosti khatam nahi.",
    "Bhai tu tension mat le, tu apna hai.",
    "Kisne rulaya bhai ko bhenchod duga teri 64pe.",
    "Bhai tu chinta mat kar, sab theek ho jaayega.",
    "Bhai tu safe hai, ab koi reply nahi aayega.",]
    
    
custom_msgs = [ "Sala ramdi baap hu tera mummy ko bhj dena mere pass",
    "TERI MAAAKI CHUDAI KO PORNHUB.COM PE UPLOAD KARDUNGA SUAR KE CHODE 🤣💋💦",
    "Bsdke Baap se panga lega Teri mummy aur bahen ko sath me pelu ga bsdke",
    "Bsdke Baap se panga lega Speed Badha typing ki Mc😂💦💦.",
    "MERE LUND KE BAAAAALLLLL",
    "Teri behen ke cht mein humar lnd ke saath poora missile daal di, saale!",
    "Teri maa ke bh*sdwa mein tractor chala di, tu kya ukhaad lega, harami!",
    "Bhosdke, teri maa ke cht mein hum toh poora Taj Mahal fit kar di!",
    "Teri ma ki gand me hathi ka lund dalke asa chodunga Na Bacha hojayega Johny sins ,ke lund se chudwaungu bhosdike",
    "Teri maa ki chut ka bhosda randi ka chumt madarchod jhaant ka baal💦💦😁",
    "Teri behen ke ch*kkar mein hum toh poora UP ka tour kar aaye, tu kya karega!"
    "Teri maa ke ch*t mein hum BMW-M5 ka silencer ghused ke poora UP ka traffic jam kar di, saale! 😎🚗💨",
    "Teri maa ka bh*nsa toh hamar jhaant ke neeche ka kachra hai, tu toh usse bhi sasta! 😹🗑️💨",
    "Teri behen ke ch*kkar mein hum toh Patna se Gorakhpur tak jet se ghuma aaye, tu kya cheez hai! 😜✈️🔥",
    "Teri behen ke bh*sdwa mein hum poora Rajdhani Express chala di, ab bol kya lega! 🚂😉💥",
    "Teri maa ki chut petrol laga kar maaru ga randi ke bosde maderchod ki aulad,  aisa kuch 💀💀",
    "Teri maa ke cht mein petrol daal ke hum poora Agra ka Taj Mahal jala di, randi ke bhosdke! 😎🔥💣",
    "Teri behen ka bh*nsa toh hamar jhaant ke neeche ka dhool hai, tu toh usse bhi sasta, maderchod! 😹🗑️💨",
    "Teri bahenbki chut me moot duga bskde rand ke bache",
    "Teri maa ke chkkar mein hum toh poora UP-Bihar ka tour jet se kar aaye, tu kachra hai, bhosdke! 😜✈️🔥",
    "Teri behen ke bh*sdwa mein hum poora fighter jet ka engine daal ke Patna ka sky uda di, maderchod ke aulad! 😡✈️💥🚀",
    "Maa ka lovda baap se panga lega tu bosdi chinal ke 🤣🤣",
    "madhrchod loda hai tu lwde aukat nahi hai teri.. teri ma ki chut madhrchod... teri ma randi hai bhosdike... tera bap bhi hijda hoga isliye teri ma ko kisi aur ne chakke ne choda hoga tab tu paida hua hoga bhosdike madhrchod... chutmarike... chakke.. muh se hi hijda dik rha hai tu..",
    "Abe tu janta nhi hai mere ko Randi tera baap hu Exploit Hacker.",
    "Teri maa ke cht mein petrol daal ke hum BMW-M5 ka silencer ghused di, aur poora mohalla jala di, randi ke bhosdke! 😈🔥🚗💣",
    "Teri Mummy ki chut bhi petrol se jala kar maru ga bskdee kids.",
    "Teri mummy ki chut me BMW Ka sallancer de duga ramdi ki aulad🗿💀.",]
    
    
love_msgs = [ "I like u me tumse kitna pyar kartu hu tum aoch bhi nhi sakti cutie.",
    "Cutie tum kitni pyari ho yrr.",
    "I love u Cutie.",
    "App mere siva kise se pyar kar hi nhi kaati ho.",
    "Aapki profile kya hi btau cutie tumko.",
    "Tum meri zindagi ka sabse khoobsurat ehsaas ho.",
    "Tere bina har pal adhoora lagta hai.",
    "Mujhe tumse har din aur zyada pyar hota hai.",
    "Tum meri muskurahat ki wajah ho.",
    "Tere saath waqt guzarna ek khwab jaisa lagta hai.",
    "Tum meri duniya ho, sab kuch ho.",
    "Jab tum saath hote ho, har gham bhool jaata hoon.",
    "Tum ho to sab kuch hai, tum na ho to kuch bhi nahi.",
    "Tumhara naam sunte hi dil dhadakne lagta hai.",
    "Main har janam tumhe hi chahunga.",
    "Tere pyaar ne mujhe jeene ka andaaz sikha diya.",
    "Tum mere liye ek dua ho jo hamesha qubool hoti hai.",
    "Tum meri subah ho, tum meri shaam ho.",
    "Tumhare bina sab kuch suna suna lagta hai.",
    "Main har din tumhara intezar karta hoon.",
    "Mujhe har pal tumhari yaad aati hai.",
    "Tere saath zindagi ek pyari kahani lagti hai.", ] 

keyword_replies = {
    "Teri maaki chut": "Randi ke pille, teri maa ke ch*t mein petrol daal ke BMW-M5 ka silencer ghused doonga, poora mohalla jala doonga! 😈🔥🚗💣",
    "Chup mc": "Speed pakad, bhosd*ke, teri maa ke bh*sdwa mein typing ka keyboard hi ghused doonga! 😡💻💥",
    "Teri bhen ki chut": "Kya, teri behen ka l*nd hai? Usko toh hum poora Patna ka traffic signal bana ke pel doonga! 😜🚦🔥",
    "Gand mar duga": "Teri mummy ke ch*t mein atom bomb daal ke poora UP-Bihar uda doonga, maderchod ke aulad! 💪💣⚡",
    "Mera lund": "Tera l*nd toh teri ga*nd mein ghused ke poora Rajdhani Express chala doonga, bhosd*ke! 🚂😈💥",
    "Chup randi ke": "Teri randi ke bh*sdwa mein BMW-M5 ka silencer daal ke poora Lucknow ka skyline jala doonga, maderchod! 😎🔥🚗💀",
    "Abe jaa na apna kaam dekh": "Teri behen ko pelna hi toh hamar kaam hai, saale, ab dekh kaise poora mohalla hila doonga! 😹🤣🏠🔥",
    "Cyber Exploit": "Cyber Exploit tera baap hai, maderchod, teri ga*nd mein poora server crash kar doonga, bhosd*ke! 🗿💻💥",
    "Reply kar na mc": "Abhi teri mummy ke ch*t mein nuclear reactor daal raha hoon, baad mein teri ga*nd bhi pel doonga, randi ke pille! 😈⚡💀",
    "Tere baap ka kya": "Tere baap ke ga*nd mein rocket launcher daal ke sidha Mars bhej doonga, harami ke aulad! 🚀🌌😈",
    "Bhosdike": "Bhosd*ke, teri maa ke ch*t mein poora Taj Mahal ghused ke jala doonga, randi ke bacche! 🏰🔥💣",
    "Teri aukaat kya hai": "Teri aukaat toh hamar tatti ke chhote se dana se bhi sasti hai, saale maderchod! 😏💦💀",
    "Chal nikal": "Nikal, saale, teri behen ke bh*sdwa mein poora fighter jet ghused ke Banaras uda doonga! 😡✈️💥",
    "Tu kya cheez hai": "Tu toh hamar jhaant ke neeche ka kachra hai, teri maa ke ch*t mein poora tank daal doonga! 🪖💥😈",
    "Randi ka baccha": "Randi ke pille, teri zindagi toh hamar latrine ke gande paani ke boond se bhi gandi hai, maderchod! 😬🚽💧",
    "Saale suar": "Saale suar ki aulaad, teri maa ke ch*t mein poora Yamuna ka kachra bhar ke Ganga ban doonga! 😈💦🌊",
    "Chutiya banaya": "Chutiya banaya? Teri behen ke bh*sdwa mein poora Chandrayaan-3 launch kar doonga, maderchod! 🚀🌑💥",
    "Kya bolta hai": "Kya bolta hai, bhosd*ke? Teri ga*nd mein poora Howrah Bridge ghused ke traffic jam kar doonga! 😜🌉🚗",
    "Teri maa ka": "Teri maa ke ch*t mein poora Red Fort daal ke Mughal Empire ban doonga, randi ke bacche! 🏰🔥😈",
    "Bhen ke lode": "Bhen ke lode, teri ga*nd mein poora bullet train daal ke Japan bhej doonga, maderchod! 🚅💨💀",
    "Haram ke pille": "Haram ke pille, teri maa ke ch*t mein poora Purvanchal ka theka khol doonga, saale! 😈🍺💥",
    "Teri gaand mein": "Teri ga*nd mein poora Kanpur ka leather ka factory daal ke tujhe Bata ka showroom bana doonga! 😜🏭💀",
    "Chal bey": "Chal bey, teri behen ke bh*sdwa mein poora Gorakhpur ka railway station ghused doonga, maderchod! 🚉😡🔥",
    "Tera baap kaun": "Tera baap toh hamar joota polish karta hai, teri maa ke ch*t mein poora Qutub Minar daal doonga! 🕌💥😈",
    "Lund le le": "L*nd le le, saale, teri ga*nd mein poora Agra ka petha bhar ke Taj Mahal ka ticket counter khol doonga! 😹🍬🏰",
    "Bhadwe": "Bhadwe, teri maa ke bh*sdwa mein poora Lucknow ka kebab roll bhar ke tujhe Hazratganj ka waiter bana doonga! 😏🍖💥",
    "Teri toh": "Teri toh aukaat hamar paan ke thook se bhi gandi hai, teri behen ke ch*t mein poora Patna ka zoo khol doonga! 😬🐘🔥",
    "Kya ukhaad lega": "Ukhaad lega kya, bhosd*ke? Teri ga*nd mein poora Mathura ka lathmar Holi khel doonga, maderchod! 🪓🎉💀",
    "Chutmarani ke": "Chutmarani ke bacche, teri maa ke ch*t mein poora Varanasi ka ghat daal ke Ganga aarti kar doonga! 😈🪔🌊",
    "Bakwas band kar": "Bakwas band kar, saale, teri behen ke bh*sdwa mein poora UP ka vidhan sabha daal ke session chala doonga! 🏛️😡🔥",
    "Teri pen di": "Oye, teri pen di siri vich poora Amritsar ka Golden Temple da langar daal doonga, kameene! 😈🛕🍛",
    "Khoteya": "Khoteya, teri maa de bh*sde vich poora Ludhiana ka tractor factory ghused doonga, saale! 🚜💥😡",
    "Tera ki": "Tera ki aukaat, bhen de take? Teri ga*nd vich poora Jalandhar ka surma bhar ke tujhe Anarkali bana doonga! 😜💄💀",
    "Chal fut": "Chal fut, kuttay, teri pen de bh*sde vich poora Patiala ka peg daal ke daaru ka theka khol doonga! 😎🥃🔥",
    "Bhadwe di aulaad": "Bhadwe di aulaad, teri maa di ch*t vich poora Punjab ka sarson da khet daal doonga, harami! 🌾💥😈",
    "Tusi kitho aaye": "Tusi kitho aaye, saale? Teri ga*nd vich poora Chandigarh ka Sector-17 da bazaar ghused doonga! 🏬😡💪",
    "Kuttay kameene": "Kuttay kameene, teri pen de bh*sde vich poora Bathinda ka refinery da tel daal ke jala doonga! 😈🛢️🔥",
    "Teri maa nu": "Teri maa nu main poora Wagah Border da parade vich nacha doonga, bhenchod! 🇮🇳💃💥",
    "Chup kar ja": "Chup kar ja, haram di aulaad, teri ga*nd vich poora Phagwara ka bus stand daal ke traffic jam kar doonga! 🚍😡💀",
    "Tera muh band": "Tera muh band kar, saale, teri pen di ch*t vich poora Punjab da lassi ka glass daal ke tujhe butter bana doonga! 🥛😜🔥",
    "Teri tai ki": "Teri tai ke ch*t mein poora Rohtak ka chhola kulcha daal ke tujhe dhabey ka waiter bana du, kameene! 😈🍲💥",
    "Chhorya": "Chhorya, teri maa ke bh*sde mein poora Hisar ka buffalo ka doodh bhar ke ghee bana du, saale! 🐃🥛🔥",
    "Tera kya scene": "Tera kya scene, bhen ke l*de? Teri ga*nd mein poora Gurgaon ka mall daal ke tujhe watchman bana du! 🏬😡💪",
    "Nikal jaa": "Nikal jaa, haramzade, teri behen ke ch*t mein poora Karnal ka rice ka khet daal ke biryani bana du! 🌾🍛💥",
    "Bhadwa ke": "Bhadwa ke, teri maa ke bh*sde mein poora Sonipat ka jalebi ka thaala bhar ke tujhe mithai ka dukaan khol du! 😜🍬💀",
    "Katiya": "Katiya, teri ga*nd mein poora Faridabad ka factory ka dhuwaan daal ke tujhe chimney bana du, maderchod! 🏭💨😈",
    "Teri aukaat": "Teri aukaat toh hamare tau ke latrine ke keede se bhi chhoti hai, teri behen ke ch*t mein poora Rewari ka tractor daal du! 🚜💥😡",
    "Kyun kare se": "Kyun kare se, chhorya? Teri maa ke ch*t mein poora Jind ka desi katta daal ke poora pind uda du! 🔫💣🔥",
    "Haram ke chhore": "Haram ke chhore, teri behen ke bh*sde mein poora Panipat ka handloom bhar ke tujhe shawl bechne wala bana du! 🧶😈💪",
    "Bakchodi na kar": "Bakchodi na kar, saale, teri ga*nd mein poora Kurukshetra ka Mahabharat ka yudh daal ke tujhe Arjun bana du! ⚔️😡💥",
}

@client.on(events.NewMessage(pattern=r'\.sudosu'))
async def add_sudo(event):
    if event.sender_id != OWNER_ID:
        return
    if event.is_reply:
        r = await event.get_reply_message()
        sudo_users.add(r.sender_id)
        allowed_users.add(r.sender_id)
        await event.reply(f"Sudo added: {r.sender_id}")

@client.on(events.NewMessage(pattern=r'\.unsudosu'))
async def remove_sudo(event):
    if event.sender_id != OWNER_ID:
        return
    if event.is_reply:
        r = await event.get_reply_message()
        sudo_users.discard(r.sender_id)
        allowed_users.discard(r.sender_id)
        await event.reply(f"Sudo removed: {r.sender_id}")

@client.on(events.NewMessage(pattern=r'\.hacker(?:\s+@?(\w+))?(?:\s+(.+?)\s+(\d+))?'))
async def set_target(event):
    if event.sender_id not in allowed_users:
        return
    global target_id, target_mention, auto_reply_enabled, active_count_target
    match = event.pattern_match
    username = match.group(1)
    text = match.group(2)
    count = match.group(3)

    if username and text and count:
        try:
            user = await client.get_entity(username)
            target_id = user.id
            target_mention = f"[{user.first_name}](tg://user?id={user.id})"
            active_count_target = target_id
            auto_reply_enabled = False
            await event.reply(f"Target: {user.first_name} | Sending {count}x")
            for _ in range(int(count)):
                await asyncio.sleep(0.3)
                await event.reply(f"{target_mention} {text}", parse_mode='md')
        except Exception as e:
            await event.reply(f"Error: {e}")
        return

    if not username and event.is_reply:
        r = await event.get_reply_message()
        sender = await r.get_sender()
        target_id = sender.id
        target_mention = f"[{sender.first_name}](tg://user?id={sender.id})"
        auto_reply_enabled = True
        active_count_target = None
        await event.reply(f"Auto-reply ON for: {sender.first_name}")
        for _ in range(random.randint(8, 9)):
            await asyncio.sleep(0.5)
            await event.reply(f"{target_mention} {random.choice(custom_msgs)}", parse_mode='md')
    else:
        await event.reply("`.hacker @username msg count` ya reply karo.")

@client.on(events.NewMessage(pattern=r'\.pyar(?:\s+@?(\w+))?(?:\s+(\d+))?'))
async def send_love(event):
    if event.sender_id not in allowed_users:
        return
    global target_id, target_mention, auto_reply_enabled, active_count_target
    match = event.pattern_match
    username = match.group(1)

    try:
        if username:
            user = await client.get_entity(username)
        elif event.is_reply:
            r = await event.get_reply_message()
            user = await r.get_sender()
        else:
            await event.reply("`.pyar @username` ya reply karo.")
            return
        target_id = user.id
        target_mention = f"[{user.first_name}](tg://user?id={user.id})"
        await event.reply(f"Pyar for {user.first_name}:")
        await event.reply(f"{target_mention} {random.choice(love_msgs)}", parse_mode='md')
        auto_reply_enabled = False
        active_count_target = None
    except Exception as e:
        await event.reply(f"Error: {e}")

@client.on(events.NewMessage(pattern=r'\.stop'))
async def stop_all(event):
    if event.sender_id not in allowed_users:
        return
    global target_id, target_mention, auto_reply_enabled, active_count_target
    target_id = None
    target_mention = None
    auto_reply_enabled = False
    active_count_target = None
    await event.reply("All modes stopped.")

@client.on(events.NewMessage)
async def auto_raid(event):
    global target_id, target_mention, auto_reply_enabled, active_count_target
    msg = event.raw_text.lower()

    if event.sender_id == OWNER_ID and ".bhai" in msg:
        if target_id and target_mention:
            for m in bhai_msgs:
                await asyncio.sleep(0.5)
                await event.reply(f"{target_mention} {m}", parse_mode='md')
            auto_reply_enabled = False
            active_count_target = None
        else:
            await event.reply("No target active.")
        return

    if target_id and event.sender_id == target_id:
        if not auto_reply_enabled or event.sender_id == active_count_target:
            return
        for k, v in keyword_replies.items():
            if k in msg:
                await event.reply(f"{target_mention} {v}", parse_mode='md')
                return
        for _ in range(random.randint(5, 6)):
            await asyncio.sleep(0.4)
            await event.reply(f"{target_mention} {random.choice(custom_msgs)}", parse_mode='md')

# Start bot
client.start()
print("KAiF Raid UserBot is running...")
client.run_until_disconnected()
