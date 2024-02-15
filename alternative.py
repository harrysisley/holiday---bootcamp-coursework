def alternate_case_characters(input_str):
  # Initialize an empty string to store the result
  result_str = ""

  # Iterate through each character in the input string
  for i, char in enumerate(input_str):
      # Check if the index is even (alternating characters)
      if i % 2 == 0:
          # Convert the character to uppercase and add to the result string
          result_str += char.upper()
      else:
          # Convert the character to lowercase and add to the result string
          result_str += char.lower()

  # Print the final result
  print(result_str)


def alternate_case_words(input_str):
  # Split the input string into a list of words
  words = input_str.split()

  # Initialize an empty list to store the modified words
  modified_words = []

  # Iterate through each word in the list
  for i, word in enumerate(words):
      # Check if the index is even (alternating words)
      if i % 2 == 0:
          # Convert the word to lowercase and add to the modified words list
          modified_words.append(word.lower())
      else:
          # Convert the word to uppercase and add to the modified words list
          modified_words.append(word.upper())

  # Join the modified words into a single string with spaces
  result_str = ' '.join(modified_words)

  # Print the final result
  print(result_str)


# Test the functions with examples
input_str_1 = "Hello World"
input_str_2 = "I am learning to code"

print("Original String 1:", input_str_1)
alternate_case_characters(input_str_1)

print("\nOriginal String 2:", input_str_2)
alternate_case_words(input_str_2)
