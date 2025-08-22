def count_vowels_consonants(text):
    # Define vowels
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    # Loop through each character
    for char in text:
        if char.isalpha():  # Check if it's a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


# Input from user
string = input("Enter a string: ")

# Count vowels and consonants
vowels, consonants = count_vowels_consonants(string)

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
