def mutate_string_1(string, position, character):
    string = string[:position] + character + string[position + 1 :]
    return string


def mutate_string_2(string, position, character):
    l = list(string)
    l[position] = character
    string = "".join(l)
    return string
