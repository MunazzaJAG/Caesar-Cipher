import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    output_text = ""

    if direction == 'decode':
        shift *= -1

    for i in text:
        if i in alphabet:
            a = (alphabet.index(i)) + shift #shift amount
            a %= len(alphabet)  # incase we reach the end and hit z/a we circle back
            output_text += alphabet[a]
        # if character (i) != an alphabet
        else:  
            output_text += i

    print(f"Here is the {direction}d result:{output_text}")


should_continue= True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart=input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == 'no':
        should_continue=False
