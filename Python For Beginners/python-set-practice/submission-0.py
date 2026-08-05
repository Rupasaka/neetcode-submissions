from typing import List

def contains_duplicate(words: List[str]) -> bool:
    pass
    set1 = set(words)
    length1= len(words)
    length2=len(set1)
    if length1 == length2:
        return False
    else:
        return True

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
