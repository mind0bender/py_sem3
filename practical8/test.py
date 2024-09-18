names = ["Yash", "Avisekh"]
uids = [11317, 11536]

names619 = ["Abhishek", "Nakul"]
uids619 = [11338, 11342]


def showAll():
    print("\nnames:", *[name.ljust(10) for name in names], sep="\t")
    print("uids :", *[str(uid).ljust(10) for uid in uids], sep="\t")


# access using index
print(names[1], "has uid:", uids[1])

showAll()

# append an element
names.append("Salim")
uids.append(10589)

showAll()

# insert an elepent at index
names.insert(0, "Kartik")
uids.insert(0, 10796)

showAll()

# extent the list
names.extend(names619)
uids.extend(uids619)

showAll()

# remove a value
names.remove("Yash")
uids.remove(11317)

showAll()

# remove the last ele
names.pop()
uids.pop()

showAll()


def getFriend(name, uid):
    return {"name": name, "uid": uid}


friends = [getFriend(names[i], uids[i]) for i in range(len(names))]

# sort the list with a key fn
friends.sort(key=lambda friend: friend["uid"])

print(*friends, sep="\n")
