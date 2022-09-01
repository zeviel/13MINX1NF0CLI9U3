import amino
from .utils import configs
from tabulate import tabulate

def retrieve_user_info(client: amino.Client):
	user_id = client.get_from_code(input("[User link]::: ")).objectId
	user_info = client.get_user_info(userId=user_id)
	print(f"""
[createdTime]::: [{user_info.createdTime}]
[nickname]::: [{user_info.nickname}]
[content]::: [{user_info.content}]
[iconLink]::: [{user_info.icon}]
[userId]::: [{user_id}]
[aminoId]::: [{user_info.aminoId}]
[webURL]::: [{user_info.webURL}]""")

def retrieve_chat_info(client: amino.Client):
	chat_id = client.get_from_code(input("[Chat link]::: ")).objectId
	chat_info = client.get_chat_thread(chatId=chat_id).json["thread"]
	print(f"""
[title]::: [{chat_info['title']}]
[content]::: [{chat_info['content']}]
[membersCount]::: [{chat_info['membersCount']}]
[tippersCount]::: [{chat_info['tipInfo']['tippersCount']}]
[tippedCoins]::: [{chat_info['tipInfo']['tippedCoins']}]
[chatId]::: [{chat_id}]
[webURL]::: [{chat_info['webURL']}]""")

def get_account_info(client: amino.Client):
	account_info = client.get_account_info().json
	print(f"""
[createdTime]::: [{account_info['createdTime']}]
[email]::: [{account_info['email']}]
[phoneNumber]::: [{account_info['phoneNumber']}]
[password]::: [{password}]
[nickname]::: [{account_info['nickname']}]
[userId]::: [{account_info['uid']}]
[aminoId]::: [{account_info['aminoId']}]
[webURL]::: [{account_info['webURL']}]""")

def start():
	client = amino.Client()
	print(configs.MAIN_MENU)
	email = input("[Email]::: ")
	password = input("[Password]::: ")
	client.login(email=email, password=password)
	print(tabulate(configs.main_menu, tablefmt="github"))
	select = int(input("[Select]::: "))
	if select == 1:
		retrieve_user_info(client)
	elif select == 2:
		retrieve_chat_info(client)
	elif select == 3:
		retrieve_account_info(client)

start()
