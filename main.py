import asyncio, random
from telethon import TelegramClient, events

# Telegram config

    "Haram ke pille": "Haram 

    username = event.pattern_match.group(1)
    count = int(event.pattern_match.group(2)) if event.pattern_match.group(2) else random.randint(5, 6)

    try:
        # Agar @username diya hai
        if username:
            user = await client.get_entity(username)
            target_id = user.id
            target_mention = f"[{user.first_name}](tg://user?id={user.id})"

        # Agar reply diya hai
        elif event.is_reply:
            user = await (await event.get_reply_message()).get_sender()
            target_id = user.id
            target_mention = f"[{user.first_name}](tg://user?id={user.id})"

        # Nahi to error
        else:
            return await event.reply("Reply karo ya `.bro @username 10` likho.")

        await event.reply(f"Brother {count} 🤍🫂...")
        for _ in range(count):
            await asyncio.sleep(0.5)
            await event.reply(f"{target_mention} {random.choice(bhai_msgs)}", parse_mode='md')

        # Target reset
        target_id = None
        target_mention = None

    except Exception as e:
        await event.reply(f"Error: {e}")

# .stop command
@client.on(events.NewMessage(pattern=r'\.stop'))
async def stop(event):
    if event.sender_id not in allowed_users:
        return
    global target_id, target_mention, auto_reply_enabled, active_count_target
    target_id = None
    target_mention = None
    auto_reply_enabled = False
    active_count_target = None
    await event.reply("💦💦")

# Auto reply listener
@client.on(events.NewMessage)
async def auto_trigger(event):
    global target_id, target_mention, auto_reply_enabled, active_count_target
    msg = event.raw_text.lower()

    if target_id and event.sender_id == target_id:
        if not auto_reply_enabled or event.sender_id == active_count_target:
            return
        for k, v in keyword_replies.items():
            if k in msg:
                return await event.reply(f"{target_mention} {v}", parse_mode='md')
        for _ in range(random.randint(5, 6)):
            await asyncio.sleep(0.4)
            await event.reply(f"{target_mention} {random.choice(custom_msgs)}", parse_mode='md')

# Start the client
client.start()
print("KAiF Raid UserBot is running...")
client.run_until_disconnected()
