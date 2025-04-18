import random
from colorama import Fore,Style,Back
import readchar
import time

clear = lambda: print("\033c\033[3J", end='') 
clear()

print(f"""{Back.CYAN}                
   ПОЛЕ ЧУДЕС   
                {Style.RESET_ALL}""".strip())
print("Загрузка слов...")
words = open("russian_nouns.txt", "r", encoding="utf-8").read().split("\n")
print(f"Загрузка завершена. Загруженно {len(words)} слов.")
print("Старт...")

word = random.choice(words)
guessed = set()
won = 0

time.sleep(0.5)

clear()
attempts = input("Скока попыток хочет Босс? ")
if not attempts.isdigit():
    print("Ээээ, афигель?")
    exit()
attempts = int(attempts)

def render():
    tbsplitter = ["━━━"] * len(word)
    result = "┏" + "┳".join(tbsplitter) + "┓\n┃ "
    for i in word:
        result += (f"{Fore.GREEN if won == 1 else ""}{i}{Fore.RESET}" if i in guessed else " ") + " ┃ "
    result = result.strip()
    result += "\n┗" + "┻".join(tbsplitter) + "┛"
    clear()
    print(result, end="\n\n")
    
    if won == 1:
        print(f"{Back.GREEN}Вы победили!{Back.RESET}")
    elif won == 2:
        print(f"{Back.RED}Вы проиграли!{Back.RESET}")
    else:    
        print(f"Осталось попыток: {Fore.CYAN}{attempts}{Fore.RESET}")
        print(f"Угаданно букв: {Fore.CYAN}{len(guessed)}{Fore.RESET}\n")

char = ""
render()

try:
    while True:
        char = readchar.readchar()
        if char in word:
            guessed.add(char)
            if set(word) == guessed:
                won = 1
                break
        else:
            attempts -= 1
            if attempts <= 0:
                won = 2
                break
        render()
    render()
except KeyboardInterrupt:
    print(Style.RESET_ALL)