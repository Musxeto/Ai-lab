def is_palindrome(word):
    for i in range(int(len(word)/2)):
        if(word[i] != word[len(word)-i-1]):
            return False
    return True

def is_odd_length(word):
    return int(len(word))%2 == 1


words = []
count = 0

while True:
    word = input("Enter a word (or 'exit' to finish): ")
    if word.lower() == 'exit':
        break
    words.append(word)

for word in words:
    if is_palindrome(word) and is_odd_length(word):
        count+=1
print("List of Words:   ",words)
print("Number of odd-length palindromes:", count)

