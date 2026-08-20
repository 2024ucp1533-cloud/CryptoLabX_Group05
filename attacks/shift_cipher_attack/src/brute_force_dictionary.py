import re
from shift_cipher import decrypt


def load_dictionary(filename):
    words = set()

    with open(filename, "r") as file:
        for line in file:
            word = line.strip().lower()
            if word:
                words.add(word)

    return words


def score_text(text, dictionary):
    words = re.findall(r"[a-zA-Z]+", text.lower())

    score = 0

    for word in words:
        if word in dictionary:
            score += 1

    return score


def dictionary_attack(ciphertext, dictionary):
    best_key = None
    best_score = -1
    best_plaintext = ""

    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = score_text(plaintext, dictionary)

        if score > best_score:
            best_score = score
            best_key = key
            best_plaintext = plaintext

    return best_key, best_plaintext, best_score


if __name__ == "__main__":
    dictionary = load_dictionary("../dictionary/english_words.txt")

    ciphertext = "KHOOR ZRUOG"

    key, plaintext, score = dictionary_attack(ciphertext, dictionary)

    print("Ciphertext:", ciphertext)
    print("Predicted Key:", key)
    print("Predicted Plaintext:", plaintext)
    print("Dictionary Score:", score)
