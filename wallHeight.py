import math 

def wallHeight(length, angle): 
    return length * math.sin(math.radians(angle))

data = [
    (16, 75),
    (20, 0),
    (24, 45),
    (24, 80),
]

for l, a in data: 
    print(f"length: {l}, Angle: {a} degrees, so the wall height is {wallHeight(l, a):.2f} ft ")