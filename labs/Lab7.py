floors = int(input("How many floors? "))
floor_safe = int(input("The highest egg-safe floor? "))

my_list = []
for i in range(1,floors + 1):
    my_list.append(i)
    
def bin_s(my_list, floor_safe):
    count = 0
    bottom = 0
    top = len(my_list) - 1
    
    while bottom <= top:
        count += 1
        mid = (bottom + top) // 2
        if my_list[mid] > floor_safe: #break
            return bottom, mid, my_list[mid], count
        else:
            bottom = mid + 1

def seq(my_list, floor_safe, bottom, top):
    count = 0
    for item in my_list[bottom : top]:
        count += 1
        if item > floor_safe:
            return item, count
        if item == my_list[top - 1]:
            return "didn't break", count

bottom, top, floor1, bin_count = bin_s(my_list, floor_safe)
print("The first egg was dropped", bin_count, "times and broke at floor", floor1, ".")
floor2, seq_count = seq(my_list, floor_safe, bottom, top)
if floor2 == "didn't break":
    print("The second egg was dropped", seq_count, "times and", floor2, ".")
else:
    print("The second egg was dropped", seq_count, "times and broke at floor", floor2, ".")