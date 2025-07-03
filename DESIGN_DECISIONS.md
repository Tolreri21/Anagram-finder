# Design Decisions – Anagram Finder

## Approach

We use a dictionary (`dict`) where the key is the sorted version of a word, and the value is a list of all words that share that sorted key (i.e., they are anagrams).
This ensures:
- Efficient lookup and grouping
- Easy scalability and readability

## Why Sorted Keys?

Sorting the characters in a word means that all anagrams will yield the same key. For example:
- `race` → `acer`
- `care` → `acer`
- `acre` → `acer`

These will be grouped under the same key.

## Performance Considerations

- For **10 million words**:
  - The current solution handles it efficiently with Python dictionaries.
  - It has a time complexity of ~O(N * K log K), where:
    - N = number of words
    - K = average word length

- For **100 billion words**:
  - The script should be reimplemented using distributed computing (e.g., Hadoop MapReduce or Spark)
  - Or store and process data in a streaming or chunked fashion

## External Libraries
None used – only standard Python 3 built-in functions and types.

## Maintainability
The script is short and modular with clearly named functions and minimal code repetition.
