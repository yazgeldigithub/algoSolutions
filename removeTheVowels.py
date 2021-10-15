def removeTheVowels(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for i in input_str:
        # if a character is in the vowels
        if i in vowels:
            # replace the vowel in the string with and empty space
            input_str = input_str.replace(i, "")
    return input_str


print(removeTheVowels("today is friday"))  # tdy s frdy
