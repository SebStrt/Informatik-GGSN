print("Polybios Entschlüsselung")
print("============")

geheimtext = input("Geheimtext eigeben: ")
matrix_key = input("Schlüssel eingeben: ")
klartext = ""
klartext = geheimtext.lower()

geheimtext = geheimtext.replace("11","a")
geheimtext = geheimtext.replace("12","b")
geheimtext = geheimtext.replace("13","c")
geheimtext = geheimtext.replace("14","d")
geheimtext = geheimtext.replace("15","e")

geheimtext = geheimtext.replace("21","f")
geheimtext = geheimtext.replace("22","g")
geheimtext = geheimtext.replace("23","h")
geheimtext = geheimtext.replace("24","i")
geheimtext = geheimtext.replace("25","k")

geheimtext = geheimtext.replace("31","l")
geheimtext = geheimtext.replace("32","m")
geheimtext = geheimtext.replace("33","n")
geheimtext = geheimtext.replace("34","o")
geheimtext = geheimtext.replace("35","p")

geheimtext = geheimtext.replace("41","q")
geheimtext = geheimtext.replace("42","r")
geheimtext = geheimtext.replace("43","s")
geheimtext = geheimtext.replace("44","t")
geheimtext = geheimtext.replace("45","u")

geheimtext = geheimtext.replace("51","v")
geheimtext = geheimtext.replace("52","w")
geheimtext = geheimtext.replace("53","x")
geheimtext = geheimtext.replace("54","y")
geheimtext = geheimtext.replace("55","z")




alpha = "abcdefghiklmnopqrstuvwxyz"

for zeichen in alpha:
    if zeichen not in matrix_key:
        matrix_key = matrix_key+zeichen


tabelle = str.maketrans(alpha, matrix_key)
klartext = geheimtext.translate(tabelle)



print(klartext)
