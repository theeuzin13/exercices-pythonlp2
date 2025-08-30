import random

def random_name(list_name):
    i = random.randint(0, len(list_name) - 1)
    return list_name[i]

def coin_converter(real_value, coin="dolar"):
    cots = {
        "dolar": 5.5,
        "euro": 6.0
    }
    if coin not in cots:
        return "Invalid coin! Use 'dolar' or 'euro'."

    return real_value / cots[coin]



def count_volwel_consonants(sentence):
    vowel = "aeiouáéíóúàèìòùãõâêîôû"
    consonants = "bcdfghjklmnpqrstvwxyz"

    sentence = sentence.lower()
    amount_vowel = sum(1 for letter in sentence if letter in vowel)
    amount_consonants = sum(1 for letter in sentence if letter in consonants)

    return amount_vowel, amount_consonants



def fatorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# ---------------------- TESTES ----------------------
names = ["Ana", "Bruno", "Carlos", "Daniela"]
print("Name randomly:", random_name(names))

print("100 reais in dólar:", coin_converter(100, "dolar"))
print("100 reais in euro:", coin_converter(100, "euro"))

sentence = "Hello World!"
vowel, consonants = count_volwel_consonants(sentence)
print(f"The sentence: '{sentence}' -> Vowel: {vowel}, Consonants: {consonants}")

print("Fatorial de 5:", fatorial(5))
