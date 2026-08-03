from typing import List

def contains_duplicate(words: List[str]) -> bool:
    count1 = len(words)
    count2 = len(set(words))
    if count1 == count2:
        return False
    else:
        return True

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
