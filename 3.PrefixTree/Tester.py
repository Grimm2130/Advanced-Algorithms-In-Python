from PrefixTrie import Trie

if __name__ == "__main__":

    words = [
        "Adams",
        "Ben",
        "Charles",
        "David",
        "Earl",
        "Francis",
        "Leon",
        "James",
        "Jane",
        "Jacob",
    ]

    trie = Trie()
    
    for word in words:
        trie.Insert(word)

    for word in words:
        assert( trie.Search(word) == True )

    print("Done!!")
    
    matches = trie.PrefixMatchAll("Ja")
    print(len(matches))

    print(f"Prefixes: {matches}")
