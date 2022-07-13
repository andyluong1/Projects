# Andy Luong 1525166
# Zylabs 8.10

def palindrome():
    sentence = input()
    word = sentence.replace(' ','')
    if word == word[::-1]:
        return sentence +" is a palindrome"
    else:
        return sentence +" is not a palindrome"
    # for index in range(len(word)):
    #     if word[index] != word[::-1]:
    #         return word + " is not a palindrome"
    #     else:
    #         return word + " is a palindrome"

print(palindrome())