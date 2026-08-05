from typing import List

def count_unique_words(words: List[str]) -> int:
    pass
    set1=set(words)
    length = len(set1)
    count =0
    for i in range(length):
        count = count+1
        i+=1
    return count

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
