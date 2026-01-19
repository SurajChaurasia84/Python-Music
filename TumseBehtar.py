import time
import sys

lyrics = [
    "Tum jo hans do, roothi raatein saari mann jaayengi",
    "Tumse behtar, tumse pyaara, yaara, koi nahi",
    "Aasmaan pe tumse roshan taara koi nahi",
    "Tumse behtar, tumse pyaara, yaara, koi nahi",
    "Aasmaan pe tumse roshan taara koi nahi"
]

letter_delay = 0.05   # delay between letters
line_delay = 1.5      # delay after each line

print("🎧 Now Playing - Tumse Behtar ❤️\n")

for line in lyrics:
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(letter_delay)
    print()  # new line
    time.sleep(line_delay)
