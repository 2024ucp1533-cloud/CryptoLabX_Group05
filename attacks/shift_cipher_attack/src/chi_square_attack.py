from shift_cipher import decrypt

ENGLISH_FREQUENCIES = {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253,
    'E': 12.702, 'F': 2.228, 'G': 2.015, 'H': 6.094,
    'I': 6.966, 'J': 0.153, 'K': 0.772, 'L': 4.025,
    'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929,
    'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056,
    'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150,
    'Y': 1.974, 'Z': 0.074
}


def chi_square_score(text):
    letters = [char.upper() for char in text if char.isalpha()]
    total_letters = len(letters)

    if total_letters == 0:
        return float("inf")

    score = 0

    for letter in ENGLISH_FREQUENCIES:
        observed = letters.count(letter)
        expected = ENGLISH_FREQUENCIES[letter] * total_letters / 100

        score += ((observed - expected) ** 2) / expected

    return score


def chi_square_attack(ciphertext):
    best_key = None
    best_score = float("inf")
    best_plaintext = ""

    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = chi_square_score(plaintext)

        if score < best_score:
            best_score = score
            best_key = key
            best_plaintext = plaintext

    return best_key, best_plaintext, best_score


if __name__ == "__main__":
    ciphertext = "KHOOR ZRUOG"

    key, plaintext, score = chi_square_attack(ciphertext)

    print("Ciphertext:", ciphertext)
    print("Predicted Key:", key)
    print("Predicted Plaintext:", plaintext)
    print("Chi-Square Score:", round(score, 2))
