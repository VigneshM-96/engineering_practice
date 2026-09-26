my_list = [10, 5, 1, 3, 9, 13]
element = 3

found_index = -1

for i in range(len(my_list)):

    if my_list[i] == element:

        found_index = i

print(f"Element {element} found at index {found_index}")
