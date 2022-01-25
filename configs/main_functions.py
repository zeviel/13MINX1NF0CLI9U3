import amino
from pyfiglet import figlet_format
from colorama import init, Fore, Style
init()
print(
    f"""{Fore.CYAN}
Script by deluvsushi
Github : https://github.com/deluvsushi"""
)
print(figlet_format("aminowallspam", font="stop"))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
link_info = client.get_from_code(input("-- User link::: ")).json["linkInfoV2"]
com_id = link_info["extensions"]["linkInfo"]["ndcId"]
user_id = link_info["extensions"]["linkInfo"]["objectId"]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
message = input("-- Message::: ")
while True:
	try:
		sub_client.comment(userId=user_id, message=message)
		print("-- Comment is sent...")
	except Exception as e:
		print(e)
		
import amino
from pyfiglet import figlet_format
from colorama import init, Fore, Style
init()
print(
    f"""{Fore.RED}
Script by deluvsushi
Github : https://github.com/deluvsushi"""
)
print(figlet_format("aminocommentbo", font="smslant"))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
link_info = client.get_from_link(input("-- Blog link::: ")).json["linkInfoV2"]
com_id = link_info["extensions"]["linkInfo"]["ndcId"]
blog_id = link_info["extensions"]["linkInfo"]["objectId"]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
message = input("-- Message::: ")
while True:
	try:
		sub_client.comment(blogId=blog_id, message=message)
		print("-- Comment is sent...")
	except Exception as e:
		print(e)
		
import amino
from pyfiglet import figlet_format
from colored import fore, style, attr
from concurrent.futures import ThreadPoolExecutor
attr(0)
print(
    f"""{fore.DARK_SEA_GREEN_2 + style.BOLD}
Script by deluvsushi
Github : https://github.com/deluvsushi"""
)
print(figlet_format("aminowalladvfxck", font="drpepper", width=78))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
message = input("-- Message::: ")
print(
"""
[1] Send Wall Advertise to Online Users
[2] Send Wall Advertise to Recent Users
"""
)
select = int(input("-- Select::: "))

if select == 1:
    with ThreadPoolExecutor(max_workers=100) as executor:
        while True:
            try:
                for i in range(100, 2500, 15000):
                    online_users = sub_client.get_online_users(
                        start=i, size=100)
                    for user_id, nickname in zip(
                            online_users.userId, online_users.nickname):
                        print(f"Sent advertise to::: {nickname}|{user_id}")
                        _ = [
                            executor.submit(
                                sub_client.comment,
                                message,
                                user_id)]
            except Exception as e:
                print(e)

elif select == 2:
    with ThreadPoolExecutor(max_workers=100) as executor:
        while True:
            try:
                for i in range(100, 2500, 15000):
                    recent_users = sub_client.get_all_users(
                        type="recent", start=i, size=100)
                    for user_id, nickname in zip(
                            recent_users.user_Id, recent_users.nickname):
                        print(f"Sent advertise to::: {nickname}|{user_id}")
                        _ = [
                            executor.submit(
                                sub_client.comment,
                                message,
                                user_id)]
            except Exception as e:
                print(e)

import amino
from pyfiglet import figlet_format
from colored import fore, style, attr
from concurrent.futures import ThreadPoolExecutor
attr(0)
print(
    f"""{fore.DARK_ORANGE + style.BOLD}
Script by deluvsushi
Github : https://github.com/deluvsushi"""
)
print(figlet_format("aminoadvbo", font="chunky"))
old = []
def advertise(data: str):
    users_list = []
    for user_id in data.profile.userId:
        users_list.append(user_Id)
    return users_list

client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
message = input("-- Message::: ")    
while True:
	try:
		print("-- Sending advertise...")
		online_users = advertise(sub_client.get_online_users(size=100))
		for user_id in old:
			if user_id in users:
				users.remove(user_id)
		sub_client.start_chat(userId=online_users, message=message)
		with ThreadPoolExecutor(max_workers=100) as executor:
			_ = [executor.submit(sub_client.start_chat, online_users, message) for user_id in users]
	except amino.lib.util.exceptions.VerificationRequired as e:
		print(f"-- VerificationRequired::: {e.args[0]['url']}")
		verification = input("-- Press enter after verification!")
	except Exception as e:
		print(e)
	

import amino
from pyfiglet import figlet_format
from colored import fore, style, attr
from concurrent.futures import ThreadPoolExecutor
attr(0)
print(
    f"""{fore.CADET_BLUE_1 + style.BOLD}
Script by deluvsushi
Github : https://github.com/deluvsushi"""
)
print(figlet_format("Aminolikefxck", font="fourtops"))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)

while True:
    try:
        with ThreadPoolExecutor(max_workers=20) as executor:
            for i in range(0, 2500, 15000):
                recent_blogs = sub_client.get_recent_blogs(
                    start=i, size=100).blog_Id
                for blog_id in recent_blogs:
                    executor.submit(client.like, blog_id)
                    print(f"-- Liked::: {blog_id}")
    except Exception as e:
        print(e)


import amino
from colorama import init, Fore
from pyfiglet import figlet_format
init()
print(f"""{Fore.YELLOW}Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(figlet_format("aminochatidfinder", font="rectangles"))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
print(
"""
[1] Get Joined Chats ChatId
[2] Get Public Chats ChatId
"""
)
select = int(input("-- Select::: "))

if select == 1:
    try:
        joined_chats = sub_client.get_chat_threads(start=0, size=100)
        for chat_id, title in zip(
                joined_chats.chatId, joined_chats.title):
            print(f"-- {chat_id}:{title}")
    except Exception as e:
        print(e)

elif select == 2:
    try:
        public_chats = client.get_public_chat_threads(start=0, size=100)
        for chat_id, title in zip(
                public_chats.chatId, public_chats.title):
            print(f"-- {chat_id}:{title}")
    except Exception as e:
        print(e)


import amino
client = amino.Client()

def get_global_user_info():
    link_info = client.get_from_code(input("-- User link::: "))
    user_info = client.get_user_info(userId=link_info.object_Id)
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
    link_info = client.get_from_code(input("-- Chat Link::: ")).json["linkInfoV2"]
    chat_id = link_info["extensions"]["linkInfo"]["objectId"]
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
    account_info = client.get_account_info().json["account"]
    print(
        f"""Account info:
account created time >> {account_info['createdTime']}
email >> {account_info['email']}
phoneNumber >> {account_info['phoneNumber']}
password >> {password}
nickname >> {account_info['nickname']}
user_Id >> {account_info['uid']}
amino_Id >> {account_info['aminoId']}
web_url >> {account_info['webURL']}"""
    )
