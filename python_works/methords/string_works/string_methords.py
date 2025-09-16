# class str:
    # def capilalize() - uppercase first latter
    # def casefold() - lowercase all latters
    # def index(str) - find index position
    # def isalpha() - check a string is full alphabet
    # def isdigit() - check a string is full digit
    # def isalnum() - check a string is full alphanumeric
    # def strip(str) - remove specific charectors from left and right
    # def lstrip(str) - remove specific charectors from left
    # def rstrip(str) - remove specific charectors from right
    # def split(str) - split a sentence by splitting it using given value


# creation of string class

    # name='hello'
    # name="hello"
    # name='''hello'''
    # name="""hello"""
    # name=str("hello")
    
# eg of methords

str1="/nhello/n"

strip=str1.strip("/n")

print(strip)

str2="hello,world.is good"

coma=str2.split(",")

space=str2.split()

dot=str2.split(".")

print(coma,space,dot)