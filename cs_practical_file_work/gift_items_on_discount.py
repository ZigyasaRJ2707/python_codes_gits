import pickle
f = open("GIFT.DAT", "wb")
items = [
    [101, "Watch", "ON DISCOUNT", 1500],
    [102, "Teddy bear","NO DISCOUNT",  4000],
    [103, "Toy car", "ON DISCOUNT", 1000],
    [104, "Grandfather clock", "NO DISCOUNT", 6000]
        ]

pickle.dump(items, f)
f.close()

f = open("GIFT.DAT", "rb")
items = pickle.load(f)
for i in items:
    if i[2] == "ON DISCOUNT":
        print(i)
f.close()
