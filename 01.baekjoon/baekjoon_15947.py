"""
백준 15947번 : 아기 석환 뚜루루 뚜루
"""

import sys
default_song = [
    "baby", "sukhwan", "tururu", "turu",
    "very", "cute", "tururu", "turu",
    "in", "bed", "tururu", "turu",
    "baby", "sukhwan"
]
n = int(sys.stdin.readline()) - 1
quotient = n // 14
reminder = n % 14
if default_song[reminder] in "tururu":
    if quotient < 3:
        print(default_song[reminder]+"ru"*quotient)
    else:
        if reminder % 2 == 0:
            print("{}+{}*{}".format("tu", "ru", (quotient+2)))
        else:
            if quotient == 3:
                print(default_song[reminder] + "ru"*quotient)
            else:
                print("{}+{}*{}".format("tu", "ru", (quotient+1)))
else:
    print(default_song[reminder])
