def is_palindrome(word):
    for i in range(int(len(word)/2)):
        if word[i] !=  word[-(i+1)]:
            print("Word:", word[i]," and ",word[-(i+1)] )
            print(f"{word} Not a palindrome")
            return False
        print(f"{word} Is a palindrome")
        return True

is_palindrome("racecar")