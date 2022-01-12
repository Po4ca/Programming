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
	alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
	alphabet += alphabet.upper()

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


shift = 34223
text = "Артемий ты не хороший человек который не пришел сегоня на занятие а мы тут угараем и шифруеми"

encrypted_text = encrypt(text, shift)
print(encrypted_text)

decrypt_text = decrypt(encrypted_text, shift, encrypt)
print(decrypt_text)

