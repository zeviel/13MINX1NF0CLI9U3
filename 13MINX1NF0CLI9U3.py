from tabulate import tabulate
from pyfiglet import figlet_format
from configs import main_functions, menu_configs
print("""Script by DeLuvSushi
Github : https://github.com/deluvsushi""")
print(figlet_format("13MINX1NF0CLI9U3", font="chunky", width=58))
print(tabulate(menu_configs.main_menu, tablefmt="github"))
select = int(input("-- Select::: "))

if select == 1:	main_functions.get_global_user_info()
elif select == 2:	main_functions.get_chat_info()
elif select == 3:	main_functions.get_account_info()
