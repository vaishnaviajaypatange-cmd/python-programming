
def VowelConsonant(char):
     vowels = "aeiouAEIOU"
     if char in vowels:
         return "vowel"
     else:
         return "consonant"
    #  for i in vowels:
    #     if i == char :
    #         print("vowel")

def main():
    char = "a"
    
    result = VowelConsonant(char)
    print(result)
    

if __name__ == "__main__":
    main()