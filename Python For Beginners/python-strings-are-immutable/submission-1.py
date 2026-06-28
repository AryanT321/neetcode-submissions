def remove_fourth_character(word: str) -> str:
    string = word[4:]
    string2 = word[:3]
    return string2 + string


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
