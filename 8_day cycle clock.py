# 2 day cycle clock

hour = int(input("Enter current hour (1-12): "))
add = int(input("Add how many hours: "))

new_time = (hour + add) % 12
print("New hour:", new_time if new_time else 12)

