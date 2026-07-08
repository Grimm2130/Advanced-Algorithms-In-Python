
class Trie:

    class Node:

        def __init__(self, val):
            self.val = val
            self.key = None
            self.isLeaf = False
            self.children = [ None for _ in range(128) ]

        def __iter__(self):
            pass

        def Dfs(self, elements : list[str], match = "" ):
            
            if self.isLeaf:
                elements.append(match + self.val)
            else:
                for child in self.children:
                    if child is not None:
                        child.Dfs( elements, match + self.val )

    def __init__(self):
        self.count = 0
        self.root = self.Node('*')
    
    def Insert(self, sequence : str )->None:
        curr = self.root

        for entry in sequence:
            c = ord(entry)
            next = curr.children[c]
            
            if next is None:
                curr.children[c] = self.Node(entry)
                next = curr.children[c]

            curr = next

        curr.isLeaf = True

    def Search( self, sequence : str )-> bool:
        found = True
        curr = self.root

        for entry in sequence:
            
            c = ord(entry)

            if curr.children[c] is None:
                found = False
                break
            curr = curr.children[c]
        
        if found == True:
            found = curr.isLeaf

        return found
    
    def PrefixMatchAll( self, prefix )-> list[str]:
        
        matches = []
        curr = self.root
        
        for entry in prefix:
            c = ord(entry)
            
            if curr.children[c] is None:
                curr = None
                break
            
            curr = curr.children[c]
        
        if curr is not None:
            for child in curr.children:
                if child is not None:
                    child.Dfs( matches, prefix )

        return matches

