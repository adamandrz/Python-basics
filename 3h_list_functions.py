lucky_numbers = [4, 8, 9, 18, 42, 56]
friends = ["Kevin", "Jack", "Jane", "Oscar", "Toby"]

print(friends)
print(lucky_numbers)

friends.extend(lucky_numbers)
print(friends)

lucky_numbers = [4, 8, 9, 18, 42, 56]
friends = ["Kevin", "Jack", "Jane", "Oscar", "Toby"]

friends.append("Olek")
print(friends)

friends.insert(1, "Aleksander")
print(friends)

friends.remove("Olek")
print(friends)

friends.clear()
print(friends)

lucky_numbers = [4, 9, 8, 18, 42, 56]
friends = ["Kevin", "Jack", "Jane", "Oscar", "Toby"]

friends.pop()
print(friends)

print(friends.index("Jane"))

print(friends.count("Jim"))

friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)

friends.reverse()
lucky_numbers.reverse()
print(friends)
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)