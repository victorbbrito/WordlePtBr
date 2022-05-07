from turtle import back
from wordle import Wordle
from colorama import Back, Fore
from typing import List
from letter_state import LetterState
import random


def main():

    word_set = load_word_set("wordle\lista_palavras.txt")
    palavra_secreta = random.choice(list(word_set))
    wordle = Wordle(palavra_secreta)

    while wordle.posso_tentar:
        palavra = input("Digite a palavra: ")

        if len(palavra) != wordle.TAMANHO_PALAVRA:
            print(Fore.RED + f"A palavra secreta tem 5 letras." + Fore.RESET)
            continue

        wordle.tentativa(palavra)
        display_results(wordle)

    if wordle.resolvido:
        print("Parabéns você resolveu")
    else:
        print(
            f"Suas chances acabaram e você não conseguiu resolver a palavra. #{palavra_secreta}#")


def display_results(wordle: Wordle):
    lines = []
    for palavra in wordle.tentativas:
        result = wordle.adivinhar(palavra)
        colored_string = convert_result_to_color(result)
        lines.append(colored_string)

    for _ in range(wordle.tentativas_restantes):
        lines.append(' '.join(['_'] * wordle.TAMANHO_PALAVRA))

    draw_border_around(lines)


def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as file:
        for line in file.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set


def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.esta_na_posicao:
            color = Fore.YELLOW
        elif letter.tem_na_palavra:
            color = Fore.MAGENTA
        else:
            color = Fore.BLACK
        colored_letter = color + letter.caractere + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)


def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):

    content_length = size + pad * 2
    top_border = "╔" + "═" * content_length + "╗"
    bottom_border = "╚" + "═" * content_length + "╝"
    space = " " * pad

    print(top_border)

    for line in lines:
        print("║" + space + line + space + "║")

    print(bottom_border)


if __name__ == "__main__":
    main()
