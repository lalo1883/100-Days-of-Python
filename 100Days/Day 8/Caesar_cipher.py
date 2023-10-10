
# Caesar cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    if direction == 'encode':
        new_word = ''
        indices = []
        for letra in text:
            if letra in alphabet:
                indice = alphabet.index(letra)
                indice = indice + shift
                indices.append(indice)
        for i in indices:
            new_word = new_word + alphabet[i]
            # print(new_word)
        # return new_word
    elif direction == 'decode':
        new_word = ''
        indices = []
        for letra in text:
            if letra in alphabet:
                indice = alphabet.index(letra)
                indice = indice + shift
                indices.append(indice)
        for i in indices:
            new_word = new_word + alphabet[i]
            # print(new_word)
    else:
        print('Incorrect option')

    print(new_word)


caesar(text, shift, direction)



