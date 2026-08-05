from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    pass
    length = len(my_list)
    if length >=3:
        for i in range(length):
            reverse_list = my_list[::-1]
            my_list = reverse_list[:3]
        return my_list[::-1]



# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
