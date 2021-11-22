filename = 'coded_text.txt'
file = open(filename, 'rt')
text = file.read()

file.close()

text = text.lower()
BAN = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890-,./[]:;\'\"-<>!?@#$%^&*()+=…–№‹›«»‐~’́"
for char in BAN:
    text = text.replace(char, "")

text = text.replace("ё","е")
non_spaces_text = "".join(text.split())
nspace_text_file = open("coded_text.txt", "w")
nspace_text_file.write(non_spaces_text)
nspace_text_file.close()