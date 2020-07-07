"""
    Description: Create TRIE and search for words
"""

from library.trie import TrieDT

if __name__ == '__main__':

    triewords = ['ComplexMatches', 'abcdefghi', 'pqrstuvwx', 
                'lmnop', 'pqtv', 'sujayyendhiren', 
                'sujayy', 'sujayy1983']

    #---------------------------#
    # Create TRIE datastructure #
    #---------------------------#
    triedt = TrieDT(triewords)

    #--------------------------------------------#
    # Test - Search TRIE  for exact word matches #
    #--------------------------------------------#

    print("\n\n\n-------- Search results (case sensitive exact match) --------------")
    searchwords = ["Complexmatches", "sujayy1983", "pqrstuvwx", "pqrstuvw"]
    for word in searchwords:
        if triedt.search(word):
            print(f"Word: {word} - Found")
        else:
            print(f"Word: {word} - Not found")

    print("------------------------------------------------------------------------")
