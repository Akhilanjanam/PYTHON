#Write A Python Program To Check Alpha Character, Whether Vowel Or Consonant

l=input('enter the letter : ')
l=l.lower()
if l in ('a','e','i','o','u'):
    print('vowel')
else:
    print('consonant')
    