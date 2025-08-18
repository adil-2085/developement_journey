# - Pattern Search in a String: Count how many times a given pattern appears in a string without
#  using string methods.


# take inputs

string = input("Enter a string:")

pattern = input("Enter a pattern:")

# find length of pattern and string without using methords

pattern_length = 0

for i in pattern:

    pattern_length += 1

string_length = 0

for i in string:
    
    string_length += 1

# find pattern occurance

occurance = 0

for j in range( string_length):

    if string[j:pattern_length+j] == pattern:

        occurance += 1

# print output

print( f"{pattern} appears {occurance} time in {string}")
