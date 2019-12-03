from telethon import TelegramClient
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetMessagesRequest
from telethon.tl.functions.messages import GetHistoryRequest, ReadHistoryRequest
from telethon.tl.types import InputPeerChannel

api_id = 702976                  # API ID
api_hash = "49681e1bbc95e5e01250ec1537ae3185"              # API Hash
phone_number = "+375293164122"    # Номер телефона аккаунта, с которого будет выполняться код

client = TelegramClient('your_account', api_id, api_hash) #не может быть одной и той же сессии с одним именем
await client.connect()

username = 'ru_modx' # канал @telegram
dp = client.get_entity(username)
messages = client.get_messages(username,100,search='ловата')
print(messages)

