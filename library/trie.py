"""
    Author: Sujayyendhiren Ramarao Srinivasamurthi
    Description: Test TRIE datastructure
"""

class TrieNode(object):

    def __init__(self, lastelem=False):
        """
            Initialize a single node
        """
        self.wordend = lastelem
        self.children = {}

    def add_element(self, elem, bLastelem=False):
        """
            Add a node into TRIE
        """
        if elem not in self.children:
            self.children[elem] = TrieNode(bLastelem) 

        ## Check update is required for shorter word endings
        if self.children[elem] != bLastelem and bLastelem:
            self.children[elem].wordend = bLastelem

        return self.children[elem]

    def search_element(self, elem): 
        """
            Search for an element in TRIE
        """
        if elem in self.children:
            return self.children[elem]
        return None

class TrieDT(object):
    """
        Trie Datstructure built using TrieNode
        as building block.
    """
    def __init__(self, words):
        self.root = TrieNode()
        for aword in words:
            print(f"DEBUG: Adding [{aword}]")
            node = self.root 
            wrdlen = len(aword)
            setbool = lambda x : True if (x == wrdlen) else False
            for idx, achar in enumerate(aword, start=1):
                node = node.add_element(achar, setbool(idx))

    def search(self, searchword): 
        """
            Basic whole word search
        """
        node = self.root; wordlen = len(searchword)
        for idx, elem in enumerate(searchword, start=1): 
            node = node.search_element(elem)
            if not node: return False
            if node.wordend and wordlen == idx: return True

        return False
            
