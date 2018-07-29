numInput = raw_input("Enter number: ")
nounInput = raw_input("Enter noun: ")

def pluralize(noun):
    if noun.endswith("ch"):
        return noun + "es"
    elif noun == "person":
        return "people"
    elif noun.endswith("ife"):
        return noun.replace("ife","ives")
    elif noun.endswith("us"):
        return noun.replace("us","i")
    elif noun.endswith("y") and noun[-2:] not in ("ay","ey","oy","uy"):
        return noun.replace("y","ies")
    else:
        return noun + "s"

print("Out: " + numInput + " " + pluralize(nounInput))