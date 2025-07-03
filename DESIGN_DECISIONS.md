Design Decisions – Anagram Finder

Approach

To find anagrams, I used a Python dictionary. The idea is simple: for each word, I sort its letters alphabetically and use that sorted version as a key. Then I store the original word in a list under that key. This way, all anagrams (which have the same sorted letters) end up grouped together.

Example:

"race" becomes "acer"
"care" also becomes "acer"
So does "acre"
So in the dictionary, "acer" maps to ["race", "care", "acre"].

Why Sort the Letters?

Sorting is the easiest way to make sure that anagrams look the same. Even if the original words are different, once sorted, they all become identical if they're anagrams. That makes it super easy to group them.

Performance

If we have about 10 million words, this method works fast because Python dictionaries are very efficient.
The time complexity is about O(N × K log K), where:
N is the number of words
K is the average length of a word (because sorting takes time)
For very large datasets like 100 billion words, this script would be too slow and use too much memory. In that case, it would be better to:
Use tools like Hadoop or Apache Spark to split the work across many machines
Or process the words in smaller chunks or streams
External Libraries

I didn’t use any extra libraries—just built-in Python stuff. That makes the code simple and easy to run anywhere with Python 3.

Maintainability

The code is clean and short. I used functions with clear names, and I avoided repeating code, so it should be easy to understand or update later.
