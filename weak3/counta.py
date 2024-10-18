li = []
total_count = 0
length = int(input("Enter the size of the list: "))
print(f"Enter {length} first names:")
for i in range(length):
    name = input()
    li.append(name)
for name in li:
    count = name.count('a') + name.count('A')
    print(f"{count} 'a'/'A' in {name}")
    total_count += count
print(f"Total number of 'a'/'A' in the list = {total_count}")
