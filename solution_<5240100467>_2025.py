#1. Using string slicing
original_string="Programming"
reversed_string=original_string[::-1]
print(reversed_string)



#2.
full_name=input("Enter your full name: ")
name_parts=full_name.split()
initials=[part[0].upper() for part in name_parts]
initials_str='.'.join(initials) + '.'
print(initials_str)



#3.
def is_palindrome(s):
    s=''.join(char.lower() for char in s if char.isalnum())
    return s ==s[::-1]
input_string=input("Enter a string to check: ")
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")


#4.
sentence=input("Enter a sentence: ")
words=sentence.split()
word_count=len(words)
print(f"Number of words in the sentence is {word_count}")


#5.
original__string="This is a string and it is an example."
words_=original__string.split()
modified_words=[word if word !="is" else "was" for word in words_]
modified_words= " ".join(modified_words)
print(modified_words)
