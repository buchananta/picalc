import random
from datetime import datetime
from sys import argv

def calculate_pi(points, inside=0, outside=0):
    start = datetime.now()
    initial = inside + outside
    ML = 1_000_000
    BL = 1_000_000_000
    pi = 0
    while points > inside + outside:
        # make a random point, and calculate if it's inside a circle
        # of radius one on the origin
        if random.random()**2 + random.random()**2 < 1:
            inside += 1
        else:
            outside += 1
        if outside >=1 and (inside + outside) % (ML * 10) == 0:
            pi = (inside * 4)/(inside + outside)
            if inside + outside < BL:
                count = f" at {(inside+outside)//ML}M pnts"
            else:
                count = f" at {(inside+outside)/BL:.1F}B pnts"
            print(f"{pi:<25_}{count} i: {inside:12_} o: {outside:12_}")
        if (inside + outside) % BL == 0:
           print(f"This has been running for {start - datetime.now()}")
    print(f"Started at: {start}")
    print(f"Finished at: {datetime.now()}")
    print(f"Calculated: {(inside + outside) - initial:,} points")
    print(f"Started with: {initial:,}")
    print(f"For a total of: {inside + outside:_} points")
    print(f"Resulting in the guess: {(inside*4)/(inside + outside)}")
    print(f"How close am I?")
    print(f"INSIDE:    {inside}")
    print(f"OUTSIDE:   {outside}")

if __name__ == "__main__":
    if len(argv) < 4:
        print("please give 3 arguments: Points to calculate, precalced inside, precalced outside")
        print("For example, 'python3 picalculator.py 100_000_000 0 0'")
    else:
        calculate_pi(int(argv[1]), int(argv[2]), int(argv[3]))
