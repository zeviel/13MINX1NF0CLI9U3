import AminoLab

client = AminoLab.Client()

def get_global_user_info():
    link_info = client.get_from_link(input("User Link >> "))
    user_info = client.get_user_info(user_Id=link_info.object_Id)
    print(
        f"""User Info:
account created time >> {user_info.createdTime}
nickname >> {user_info.nickname}
content >> {user_info.content}
icon link >> {user_info.icon}
user_Id >> {link_info.object_Id}
amino_Id >> {user_info.amino_Id}
web_url >> {user_info.web_URL}"""
    )

def get_chat_info():
    link_info = client.get_from_link(input("Chat Link >> "))
    ndc_Id = link_info.ndc_Id; thread_Id = link_info.object_Id
    chat_info = client.get_thread(ndc_Id=ndc_Id, thread_Id=thread_Id)["thread"]
    print(
        f"""Chat info:
title >> {chat_info['title']}
content >> {chat_info['content']}
members_count >> {chat_info['membersCount']}
tippers_count >> {chat_info['tipInfo']['tippersCount']}
tipped_coins >> {chat_info['tipInfo']['tippedCoins']}
thread_Id >> {thread_Id}
web_url >> {chat_info['webURL']}"""
    )

def get_account_info():
    email = input("Email >> ")
    password = input("Password >> ")
    client.auth(email=email, password=password)
    account_info = client.get_account_info()["account"]
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
