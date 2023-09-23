from collections import Counter

def my_hash(k):
    ek = k.encode()
    b = bytearray(ek)
    h = bytearray(0xd3)
    for i in range(len(b)):
        h[0] = h[0] ^ b[i]

    return h[0]


# Open the text file for reading
file_path = "./project7/namelist.txt"
nameList = list()
with open(file_path, "r") as input_file:
    # Read each line from the input file, strip the newline character, and append to the list
    for line in input_file:
        line = line.rstrip("\n")  # Remove the trailing newline character
        nameList.append(line)  # Append the modified line to the list

nameHash = dict()
for name in nameList:
    nameHash[name] = my_hash(name)

hashList = nameHash.values()
item_counts = Counter(hashList)

# Find the most common item
most_common_item = item_counts.most_common(1)[0]

# The most_common_item is a tuple with the item and its count
most_common_value, most_common_count = most_common_item
print(f"The most common item is {most_common_value} with {most_common_count} occurrences.")

for key, value in nameHash.items():
    if value == most_common_value:
        print("{0}:{1}".format(key, value))
