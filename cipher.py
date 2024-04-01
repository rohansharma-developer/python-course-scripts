alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift  %= 26

def caesar(some_text, shift_amount, dir):
  txt = ""
  for letter in some_text:
    position = alphabet.index(letter)
    if dir == "encode":
        new_position = position + shift_amount
    elif dir == "decode":
        new_position = position - shift_amount
    txt += alphabet[new_position]
  print(f"The decoded text is {txt}")

from art import logo
print(logo)

caesar(some_text=text, shift_amount=shift, dir=direction)