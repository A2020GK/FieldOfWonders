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
op = 0

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
        result += (f"{Fore.GREEN if op == 1 else ""}{i}{Fore.RESET}" if i in guessed else " ") + " ┃ "
    result = result.strip()
    result += "\n┗" + "┻".join(tbsplitter) + "┛"
    clear()
    print(result, end="\n\n")
    
    if op == 1:
        print(f"{Back.GREEN}Вы победили!{Back.RESET}\n")
    elif op == 2:
        print(f"{Back.RED}Вы проиграли!{Back.RESET}\n")
    elif op == 3:
        print("Правила:\nВам нужно угадывать буквы, укладываясь в выделенное количество попыток :)")
    elif op == 4:
        print(f"{Back.YELLOW}Такая буква уже была угаданна!{Back.RESET}\n")
    print(f"Осталось попыток: {Fore.CYAN}{attempts}{Fore.RESET}")
    print(f"Угаданно букв: {Fore.CYAN}{len(guessed)}{Fore.RESET}\n")
    print("Команды:\n0\tВыход\n1\tПравила\n")

char = ""
render()

try:
    while True:
        char = readchar.readchar().lower()
        if char == "0":
            op = 2
            break
        elif char == "1":
            op = 3
        elif char in word:
            if char in guessed:
                op = 4
            else:
                op = 0
                guessed.add(char)
                if set(word) == guessed:
                    op = 1
                    break
        else:
            op = 0
            attempts -= 1
            if attempts <= 0:
                op = 2
                break
        render()
    render()
    print(f"Слово: {word}")
except KeyboardInterrupt:
    print(Style.RESET_ALL)