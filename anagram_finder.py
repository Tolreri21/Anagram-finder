# Anagram Finder

# Reads words from a file and removes any empty lines or newline characters
def read_words(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]  

# Groups words that are anagrams of each other
def group_anagrams(words):
    anagram_groups = {}
    for word in words:
        # Sort the letters in the word to use as a key
        key = ''.join(sorted(word))
        # If the key doesn't exist yet, make a new list for it
        if key not in anagram_groups:
            anagram_groups[key] = []
        # Add the word to its anagram group
        anagram_groups[key].append(word)
    # Return only the grouped anagram lists
    return anagram_groups.values()

if __name__ == '__main__':
    filename = 'sample.txt' 
    words = read_words(filename)  
    grouped = group_anagrams(words) 
    for group in grouped:
        print(' '.join(group)) 
