L = [
    "doublemint,1.5,10",
    "mentos,0.7,20",
    "oreo,2.8,5",
    "chupachups,0.2,30",
    "oreo,2.8,15",
]
# D là {'doublemint': 10, 'mentos': 20, 'oreo': 5, 'chupachups': 30}
D = {}
for item in L:
    arr = item.split(",")
    # print(arr)
    D[arr[0]] = D.get(arr[0], 0) + int(arr[2])
    print(D)
    
print(D)