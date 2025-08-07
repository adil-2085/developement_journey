# text = "pseudopseudohypoparathyroidisms  eudopseudohypoparathyroidism".casefold()

text = input("Enter the string:").casefold()


vowels = "aeiou"

vowels_count = 0

consonent_count = 0

for i in text:

    if i in vowels:

        vowels_count += 1
    
    elif i.isalpha():

        consonent_count += 1

print(f"vowel count is:{vowels_count}\nconsonent count is:{consonent_count}")
