# Program to count the occurrences of each element in a list using a dictionary

def count_occurrences(input_list):
    counts = {}
    for item in input_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

my_list = [1, 2, 1, 3, 4, 2, 1]

occurrences = count_occurrences(my_list)

print("Occurrences of each element:")
for item, count in occurrences.items():
    print(f"{item}: {count}")