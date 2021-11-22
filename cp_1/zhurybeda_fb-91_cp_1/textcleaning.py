filename = 'text.txt'
file = open(filename, 'rt')
text = file.read()

file.close()

text = text.lower() #lowercase
BAN = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890-,./[]:;\'\"-<>!?@#$%^&*()+=…–№‹›«»‐~’́"
for char in BAN:
    text = text.replace(char, "")
non_spaces_text = "".join(text.split())
spaces_text = " ".join(text.split())

nspace_text_file = open("non_spaces_text.txt", "w")
nspace_text_file.write(non_spaces_text)
nspace_text_file.close()

space_text_file = open("spaces_text.txt", "w")
space_text_file.write(spaces_text)
space_text_file.close()
