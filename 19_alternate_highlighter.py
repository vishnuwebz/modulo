# 4 alternate highlighter

names = ["Kamal", "Rajini", "Ajith", "Vijay"]

for i in range(len(names)):
    if i % 2 == 0:
        print(f"{names[i]} <- Highlighted")
    else:
        print(names[i])

"""
Kamal <- Highlighted
Rajini
Ajith <- Highlighted
Vijay
"""