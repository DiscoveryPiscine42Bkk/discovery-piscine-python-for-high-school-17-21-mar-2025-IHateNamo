#!/usr/bin/env python3

origin_array = [2,8,9,48,8,22,-12,2]
new_array = [i+2 for i in origin_array]
greater_than = [i for i in new_array if i>5]

print(origin_array)
print(greater_than)
