from typing import List

def areDistinct(data: List[int]) -> bool:
    uniqueNums = {x for x in data}
    return len(uniqueNums) == len(data)

data1 = [4, 7, 8, 13, 9]
data2 = [3, 8, 4, 8, 11, 5
         ]

print(areDistinct(data1))
print(areDistinct(data2))
