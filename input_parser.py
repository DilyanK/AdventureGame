words_to_remove = ["at", "please"]

#This function takes the user input, filter it then return it.
def Parse_Input(user_input):
    output = ""

    for char in user_input:
        if char.isalpha() or char.isdigit() or char == " ":
            output += char

    while "  " in output:
        output.replace("  ", "")

    output = output.strip().lower().split(" ")

    filtered = []

    for word in output:
        if word not in words_to_remove:
            filtered.append(word)
    
    return filtered
