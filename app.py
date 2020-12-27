
lucky_numbers = [4, 8, 15, 6, 100, 123, 2, 311, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

lucky_numbers.sort()

friends2 = friends.copy()
friends2.sort()

print(lucky_numbers)
print(friends.count("Jim"))
print(friends2)
print(friends)
lucky_numbers.reverse()
print(lucky_numbers)