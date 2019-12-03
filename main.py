from telethon import TelegramClient, sync, events

print('Started')

api_id = 1111                  # API ID
api_hash = "dfdfsdfsdfsd"              # API Hash
phone_number = "number"    # Номер телефона аккаунта, с которого будет выполняться код
username = 'ru_modx' # канал @telegram\
client = TelegramClient('your_account', api_id, api_hash) #не может быть одной и той же сессии с одним именем

@client.on(events.NewMessage(chats=(username)))
async def normal_handler(event):
    if "ловата" in event.message.to_dict()['message'] or "october" in event.message.to_dict()['message']: #обычно ждем тебя после этих мсг
        print('newmsg from ru_modx: ' + event.message.to_dict()['message'])


client.start()
client.run_until_disconnected()



