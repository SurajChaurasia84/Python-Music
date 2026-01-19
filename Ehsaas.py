
import time
import sys

def type_line(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

lyrics = [
    "Teri nazron ka dil pe hua asar,",
    "Tu mera mehboob hai jaana,",
    "Teri ulfat mein jeeta har pal,",
    "Tu ik tohfa hai khuda ka."
]

print("🎧 Now Playing - Ehsas ❤️\n")

for line in lyrics:
    type_line(line)
    time.sleep(1.5)
