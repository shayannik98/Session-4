#donbale_ shayan nikpour
import random

print("Hello welcome")
n=int(input("tedad adad morede nazaretuno vared konid: "))

def fill_list_without_repeats(n):
    original_list = list(range(1, n+10))
    random.shuffle(original_list)
    new_list = original_list[:n]
    return new_list


result = fill_list_without_repeats(n)
print("liste mored nazare shoma:" , result)