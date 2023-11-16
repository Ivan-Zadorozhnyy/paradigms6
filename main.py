import matplotlib.pyplot as plt
from collections import Counter
import string

with open('../pythonProject2/inp.txt', 'r') as file:
    encrypted_text = file.read()

encrypted_text = encrypted_text.lower()

filtered_text = ''.join(filter(lambda char: char in string.ascii_lowercase, encrypted_text))

letter_freq = Counter(filtered_text)

for letter, freq in letter_freq.items():
    print(f"{letter}: {freq}")

letters, freqs = zip(*sorted(letter_freq.items()))
plt.figure(figsize=(10, 5))
plt.bar(letters, freqs, color='skyblue')
plt.xlabel('Letter')
plt.ylabel('Frequency')
plt.title('Letter Frequency Histogram')
plt.show()

reference_freqs = {
    'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3, 'e': 12.7,
    'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.15,
    'k': 0.77, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5,
    'p': 1.9, 'q': 0.095, 'r': 6.0, 's': 6.3, 't': 9.1,
    'u': 2.8, 'v': 0.98, 'w': 2.4, 'x': 0.15, 'y': 2.0,
    'z': 0.074
}


def caesar_decrypt(text, key):
    decrypted_text = ''.join(chr((ord(char) - ord('a') - key) % 26 + ord('a')) if char.isalpha()
                             else char for char in text)
    return decrypted_text


def calculate_difference(decrypted_text, reference_freqs):
    letter_freq = Counter(decrypted_text)
    difference = sum(
        abs(reference_freqs.get(char, 0) - letter_freq.get(char, 0) * 100 / len(decrypted_text)
            ) for char in string.ascii_lowercase
    ) / 26
    return difference


key_differences = {}
for key in range(26):
    decrypted_text = caesar_decrypt(filtered_text, key)
    key_differences[key] = calculate_difference(decrypted_text, reference_freqs)

sorted_keys = sorted(key_differences, key=key_differences.get)

for i in range(3):
    print(f"Key {sorted_keys[i]}: {key_differences[sorted_keys[i]]} difference")
