import amino
client = amino.Client()

def get_global_user_info():
    user_id = client.get_from_code(input("[User link]::: ")).objectId
    user_info = client.get_user_info(userId=user_id)
    print(
        f"""UserInfo:::
[createdTime]::: [{user_info.createdTime}]
[nickname]::: [{user_info.nickname}]
[content]::: [{user_info.content}]
[iconLink]::: [{user_info.icon}]
[userId]::: [{user_id}]
[aminoId]::: [{user_info.aminoId}]
[webURL]::: [{user_info.webURL}]"""
    )

def get_chat_info():
    chat_id = client.get_from_code(input("[Chat link]::: ")).objectId
    chat_info = client.get_chat_thread(chatId=chat_id).json["thread"]
    print(
        f"""ChatInfo:::
[title]::: [{chat_info['title']}]
[content]::: [{chat_info['content']}]
[membersCount]::: [{chat_info['membersCount']}]
[tippersCount]::: [{chat_info['tipInfo']['tippersCount']}]
[tippedCoins]::: [{chat_info['tipInfo']['tippedCoins']}]
[chatId]::: [{chat_id}]
[webURL]::: [{chat_info['webURL']}]"""
    )

def get_account_info():
	email = input("[Email]::: ")
	password = input("[Password]::: ")
	client.login(email=email, password=password)
	account_info = client.get_account_info().json
	print(f"""AccountInfo:::
[createdTime]::: [{account_info['createdTime']}]
[email]::: [{account_info['email']}]
[phoneNumber]::: [{account_info['phoneNumber']}]
[password]::: [{password}]
[nickname]::: [{account_info['nickname']}]
[userId]::: [{account_info['uid']}]
[aminoId]::: [{account_info['aminoId']}]
[webURL]::: [{account_info['webURL']}]"""
    )
