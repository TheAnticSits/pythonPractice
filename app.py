
lucky_numbers = [4, 8, 15, 6, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.pop()
friends.clear()
print(friends)