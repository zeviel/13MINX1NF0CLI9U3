import pyfiglet
from configs import main_functions, menu_configs
from tabulate import tabulate
print("""Script by DeLuvSushi
Github : https://github.com/deluvsushi""")
print(pyfiglet.figlet_format("aminoinfoclique", font="chunky", width=58))
print(tabulate(menu_configs.main_menu, tablefmt="github"))
select = input("Select >> ")

if select == "1":	main_functions.get_global_user_info()
elif select == "2":	main_functions.get_chat_info()
elif select == "3":	main_functions.get_account_info()
