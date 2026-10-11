def atbasch(textin):
    textout = ""

    textin = textin.replace("ö", "oe")
    textin = textin.replace("ä", "ae")
    textin = textin.replace("ü", "ue")
    textin = textin.replace("ß", "ss")

    textin = textin.lower()


    tabelle = str.maketrans("abcdefghijklmnopqrstuvwxyz1234567890.,!?","?!,.0987654321zyxwvutsrqponmlkjihgfedcba")
    textout = textin.translate(tabelle)

    return textout