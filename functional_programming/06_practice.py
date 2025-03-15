#!/usr/bin/python3
import string
from collections import Counter
from functools import reduce

# Text analysis tool: input ->text
# output: statistics-> freq word, avg word lenght, most used words

# func pure!! clean and tokenize text


def tokenize(text):
    # remove  any punctuation and remove lowercase
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    # partir el texto en palabras
    tokens = text.split()
    return tokens


def word_frequency(tokens):
    return Counter(tokens)


def avg_word_lenght(tokens):
    total_lenght = reduce(lambda total, word: total + len(word), tokens, 0)
    return total_lenght / len(tokens) if tokens else 0  # ternary operation in python


def most_common_words(frequency, num=5):
    return frequency.most_common(num)


def analyze_text(text):
    tokens = tokenize(text)
    frequency = word_frequency(tokens)
    avg_word_l = avg_word_lenght(tokens)
    common_words = most_common_words(frequency)

    print(f"total de palabras {len(tokens)}")
    print(f"Promedio tam palabras:{avg_word_lenght(tokens)}")
    print(f"Palabras mas comunes:{most_common_words(frequency)}")
    for word, freq in common_words:
        print(f"{word}:{freq}")


if __name__ == "__main__":
    text = "Arre que llegando al caminito aquimichu, aquimichu, arre que llegnado el caminito, aquimichu, aquimichu"
    analyze_text(text)
