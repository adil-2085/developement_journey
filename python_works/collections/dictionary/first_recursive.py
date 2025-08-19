# first recursive character

word = 'helloworld'

repeat = {}

for i in word:

    if i in repeat:

        print(f"first recursive word is:{i}")

        break

    else:

        repeat[i] = 1

