def remove_fourth_character(message: str) -> str:
    before_second = message[:3] # "I"
    after_second = message[4:]  # "will never change."

    new_message = before_second + after_second
    return new_message



# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
