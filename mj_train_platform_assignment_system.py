train_ids = [101, 202, 303, 404, 505]

for train in train_ids:
    platform = (train % 4) + 1
    print(f"Train {train} -> Platform {platform}")


"""
Train 101 -> Platform 2
Train 202 -> Platform 3
Train 303 -> Platform 4
Train 404 -> Platform 1
Train 505 -> Platform 2
"""