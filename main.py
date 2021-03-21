import re
import requests
import keep_alive
from colorama import Fore, init
from discord.ext import commands
init()

Zardex = commands.Bot(command_prefix="|", help_command=None, self_bot=False)


worker = "Your ALT Token"
claimer = "Your Main Account Token"



discord = requests.get('https://pastebin.com/raw/rK8aMqf6')
@Zardex.event
async def on_connect():
    print(Fore.GREEN + '[+] Nitro Sniper is Working!')
    print(Fore.CYAN + '- Subscribe to Zardex! I will bring more awesome stuff! -\n')
    print(discord.text +' - Join or no nitro')
@Zardex.event
async def on_message(message):
    try:
        if 'discord.gift/' in message.content:
            epic = re.search("discord.gift/(.*)", message.content).group(1)
            headers = {
                'Authorization': claimer,
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36 "
            }
            x = f"{Fore.LIGHTGREEN_EX} Zardex {Fore.RESET}| Code: {epic} {Fore.GREEN} {Fore.RESET}| "
            r = requests.post(
            f'https://discordapp.com/api/v8/entitlements/gift-codes/{epic}/redeem', headers=headers)

            if '{"message": "Unknown Gift Code", "code": 10038}' in r.text:
                print(x + Fore.RED + f'| The code is fake! | {message.guild} | {message.author}')
            elif '{"message": "This gift has been redeemed already.", "code": 50050}' in r.text:
                print(x + Fore.YELLOW + f'| The code was already Redeemed by someone. | {message.guild} | {message.author}')
            elif 'You are being rate limited' in r.text:
                print(x + Fore.RED + f'| Spamming Codes got you Rate Limited. | {message.guild} | {message.author}')
            elif 'Access denied' in r.text:
                print(x + Fore.YELLOW + f'| Failed to Claim the Code (code might be false) | {message.guild} | {message.author}')
            elif len(x) != 16 or x.isnumeric() == True:
            	print(x + Fore.RED + f'| The code is fake! | {message.guild} | {message.author}')
            elif 'subscription_plan' in r.text:
                print(x + Fore.GREEN + f'| You Sniped a Nitro damn! | {message.guild} | {message.author}')
    except AttributeError:
        pass

#THIS IS IS ORIGINALLY WROTE BY Zardex#1337
Zardex.run(worker, bot=False)