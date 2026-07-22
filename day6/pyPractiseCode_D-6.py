# find and print the character that occurs most frequently ?

# For input:
# miiisiiisssion# frequent char 
# Output:
# i

# i = input()
# freq = {}
# for char in i:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# max_freq = max(freq.values())
# for char in i:
#     if freq[char] == max_freq:
#         print(char)
#         break
# #output:miiisiiisssion
# #       i

# Count vowels in a string
# Hint: Loop through the string and check whether each character is in "aeiouAEIOU".
# Input:  Hello World
# Output: 3

# s = input()
# vowels = "aeiouAEIOU"
# count = 0

# for char in s:
#     if char in vowels:
#         count += 1

# print(count)

# Find the first non-repeating character
# Hint: First store each character’s frequency in a dictionary. Then loop through the string again.
# Input:  aabbcdde
# Output: c

# s= input()
# freq = {}
# for char in s:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# print(freq)
# min_freq = min(freq.values())
# for char in s:
#     if freq[char] == min_freq:
#         print(char)
#         break


# Count the frequency of every word
# Hint: Use split() to convert the sentence into words, then use a dictionary.
# Input:  cat dog cat bird dog cat
# Output: {'cat': 3, 'dog': 2, 'bird': 1}

# s = input().split( )
# freq = {}
# for str in s:
#     if str in freq:
#         freq[str] += 1
#     else:
#         freq[str] = 1
# print(freq)

# Find the least frequent character
# Hint: Find the minimum value using min(freq.values()), then locate its character.
# Input:  programming
# Output: p

# s = input()
# freq = {}
# for char in s:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# min_ = min(freq.values())
# for char in s:
#     if freq[char] == min_:
#         print(char)
#         break

# Remove duplicate characters
# Hint: Keep a result string. Add a character only if it is not already in the result.
# Input:  programming
# Output: progamin

# s = input()
# result = ""

# for char in s:
#     if char not in result:
#         result += char

# print(result)

# Check whether two strings are anagrams
# Hint: Two strings are anagrams if their character-frequency dictionaries are equal.
# Input:  listen
#         silent
# Output: Anagram

# s = input()
# t = input()

# if sorted(s) == sorted(t):
#     print("Anagram")
# else:
#     print("Not Anagram")

# Find the second most frequent character
# Hint: Store frequencies, find the highest frequency, then find the next lower frequency.
# Input:  aabbbccccdd
# Output: b

# s = input()
# freq = {}
# for char in s:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# max_freq = max(freq.values())
# for char in s:
#     if freq[char] == max_freq - 1:
#         print(char)
#         break

# Count uppercase, lowercase, digits, and spaces
# Hint: Use isupper(), islower(), isdigit(), and isspace().
# Input:  Hello 123 World
# Output:
# Uppercase: 2
# Lowercase: 8
# Digits: 3
# Spaces: 2

# s = input()
# u_case = 0
# l_case = 0
# digit = 0
# space = 0
# for char in s:
#     if char.isupper():
#         u_case +=1
#     elif char.islower():
#         l_case += 1
#     elif char.isdigit():
#         digit += 1
#     else:
#         space += 1 
# print('Upper case :',u_case)
# print('Lower case :',l_case)
# print('Digits:',digit)
# print('Spaces :',space)
        

# Find all characters that occur more than once
# Hint: Create a frequency dictionary and print characters whose count is greater than 1.
# Input:  success
# Output: s c

# s = input()
# freq = {}

# for char in s:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# result = []
# for char in s:
#     if freq[char] > 1 and char not in result:
#         result.append(char)
# print(' '.join(result))

# Replace the most frequent character with *
# Hint: First find the most frequent character, then use replace().
# Input:  banana
# Output: b*n*n*

# s= input()
# freq = {}
# for char in s:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# m_freq_char = max(freq, key=freq.get)
# result = []
# for char in s:
#     if char != m_freq_char:
#         result.append(char)
#     else:
#         result.append('*')
# print(''.join(result))