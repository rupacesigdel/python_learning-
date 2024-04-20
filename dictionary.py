dic = {
    1: "rajan",
    2: "shivam",
    3: "sujan",
    4: "prabin"
}
print(dic[2], dic[3])

info = { "name":"saroj", "age":20, "eligible":True}
print(info)
# print(info["name2"]) #getting error through it if not aviable in dict
print(info.get("name2")) # no error getting but None is get if not aviable in dict
print(info["name"])
print(info["eligible"])

print(info.keys())
print(info.values())

##

for key in info.keys():
    # print(info[key]) or,
    print(f"the value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"the value corresponding to the {key} is {value}")


ep = {122: 45, 123:89, 567:69, 670:69}
ep2 = {222: 67, 566:90}
# ep.update(ep2)
# ep.clear()
# ep.pop(122)
ep.popitem()
del ep[122]
print(ep)
