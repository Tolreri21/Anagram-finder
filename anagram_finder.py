# Anagram Finder
# Reads words from a file and prints groups of anagrams

def read_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def group_anagrams(words):
    anagram_groups = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups[key].append(word)
    return anagram_groups.values()

if __name__ == '__main__':
    filename = 'sample.txt'
    words = read_words(filename)
    grouped = group_anagrams(words)
    for group in grouped:
        print(' '.join(group))
