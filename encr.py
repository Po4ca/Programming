def encrypt(text: str, shift: int) -> str:
	"""
		66 символов
		от 0 до 65 идексы

		66 - 0
		67 - 1
		68 - 2
		132 - 0

		% 66
	"""

	encrypted_text = ""

	for letter in text:
		if letter in alphabet:
			index = alphabet.index(letter)
			index = (index + shift) % len(alphabet)
			encrypted_text += alphabet[index]
		else:
			encrypted_text += letter
	return encrypted_text


def decrypt(text: str, shift: int, func) -> str:
	return(encrypt(text, shift * -1))


shift = 10
text = "Григорий"
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet += alphabet.upper()

encrypted_text = encrypt(text, shift)
print(encrypted_text)

decrypt_text = decrypt(encrypted_text, shift, encrypt)
print(decrypt_text)


for i in range(len(alphabet)):
	print(i, decrypt(encrypted_text, i, encrypt))