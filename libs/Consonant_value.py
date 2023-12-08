def Consonant_value(word):
  
    # Check for spaces or numbers in the input string
    if any(char.isspace() or char.isdigit() for char in word):
        raise ValueError(f"Invalid character in the word '{word}'. Input should only contain alphabetic characters without spaces or numbers.")

    vowels = set('aeiou')
    #use it to store char after being verified its not a vowel
    consonant_substring = ""
    #use it to store char value after being calculated
    max_value = 0

    for char in word:
        #use to check if there is a vowel in the word and if it not a vowel it is stored in the consonant_substring
        if char not in vowels:
            consonant_substring += char
            
        else:
            if consonant_substring:
                #calculate the value of the consonant
                current_value = sum(ord(c) - ord('a') + 1 for c in consonant_substring)
               
                max_value = max(max_value, current_value)
                
                consonant_substring = ""

    # Check for the last consonant substring in case the word ends with a consonant
    else:
      if consonant_substring:
        current_value = sum(ord(c) - ord('a') + 1 for c in consonant_substring)
       
        max_value = max(max_value, current_value)
        

    return max_value

words_to_check = ["zodiacs","strength","strength strength" ,"strength123"]

for word in words_to_check:
    try:
        print(f"{word}:{Consonant_value(word)}")
    except ValueError as e:
        print(f"Error: {e}")