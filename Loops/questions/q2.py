# write a programm to greet all elemnt in list name start with "p"
lis = ["Prakash", "Akash", "vikash", "arihant", "anuragh", "Ansu", "verma"]
LisStartwithP = []
ListStartWithNotP = []
for ele in lis:
    if ele.lower().startswith("a"):
        LisStartwithP.append(ele)
    else:
        ListStartWithNotP.append(ele)

else:
    pass


print("LisStartwithP:::==>", LisStartwithP)
print("ListStartWithNotP:::->", ListStartWithNotP)
