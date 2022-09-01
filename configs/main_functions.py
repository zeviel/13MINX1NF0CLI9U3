import amino
client = amino.Client()

def get_global_user_info():
    user_id = client.get_from_code(input("-- User link::: ")).objectId
    user_info = client.get_user_info(userId=user_id)
    print(
        f"""User Info:
account created time >> {user_info.createdTime}
nickname >> {user_info.nickname}
content >> {user_info.content}
icon link >> {user_info.icon}
user_Id >> {link_info.objectId}
amino_Id >> {user_info.aminoId}
web_url >> {user_info.webURL}"""
    )

def get_chat_info():
    chat_id = client.get_from_code(input("-- Chat Link::: ")).objectId
    chat_info = client.get_chat_thread(chatId=chat_id).json["thread"]
    print(
        f"""Chat info:
title >> {chat_info['title']}
content >> {chat_info['content']}
members_count >> {chat_info['membersCount']}
tippers_count >> {chat_info['tipInfo']['tippersCount']}
tipped_coins >> {chat_info['tipInfo']['tippedCoins']}
thread_Id >> {chat_id}
web_url >> {chat_info['webURL']}"""
    )

def get_account_info():
	email = input("-- Email::: ")
	password = input("-- Password::: ")
	client.login(email=email, password=password)
	account_info = client.get_account_info().json
	print(f"""Account info:
account created time >> {account_info['createdTime']}
email >> {account_info['email']}
phoneNumber >> {account_info['phoneNumber']}
password >> {password}
nickname >> {account_info['nickname']}
user_Id >> {account_info['uid']}
amino_Id >> {account_info['aminoId']}
web_url >> {account_info['webURL']}"""
    )
