text = "The quick brown fox jumps over a lazy dog".casefold()

alpahabets = "abcdefghijklmnopqrstuvwxyz"

alpha_count = 0

for i in alpahabets:

    if i in text:

        alpha_count += 1

if alpha_count == 26:

    print("it is pangram")

else:
    print("it is not a pangram")