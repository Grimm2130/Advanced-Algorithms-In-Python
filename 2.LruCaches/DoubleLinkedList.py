from __future__ import annotations
from random import shuffle

class DllNode:

    def __init__(self, data):
        self.mData = data
        self.mLeft = None
        self.mRight = None

    def Detach( self ):
        left : DllNode = self.mLeft
        right : DllNode = self.mRight

        self.mLeft = self.mRight = None

        if left is not None:
            left.mRight = right

        if right is not None:
            right.mLeft = left

    def __str__(self):
        return f"({self.mData})"

    @staticmethod
    def Connect( left: DllNode, right: DllNode ):
        left.mRight = right
        right.mLeft = left


class Dll:

    def __init__(self):
        self.mCount = 0
        self.mHead = None
        self.mTail = None

    def Prepend( self, data ):
        
        newNode = DllNode( data )

        if self.mHead is None:
            self.mHead = self.mTail = newNode
        else:
            DllNode.Connect( newNode, self.mHead )
            self.mHead = newNode

        self.mCount += 1

        return newNode

    def Append( self, data ):
        
        newNode = DllNode( data )

        if self.mHead is None:
            self.mHead = self.mTail = newNode
        else:
            DllNode.Connect( self.mTail, newNode )
            self.mTail = newNode

        self.mCount += 1
        
        return newNode

    def RemoveTail( self ):

        toRemove = None
        
        if self.mTail is not None:
            if self.mHead == self.mTail:
                self.mHead = None
            toRemove = self.mTail
            self.mTail = self.mTail.mLeft
            toRemove.Detach()
            self.mCount -= 1

        return toRemove

    def RemoveHead( self ):

        toRemove = None

        if self.mHead is not None:
            # Dereference tail
            if self.mTail == self.mHead:
                self.mTail = None
            toRemove = self.mHead
            self.mHead = self.mHead.mRight
            toRemove.Detach()
            self.mCount -= 1

        return toRemove
    
    def Find( self, key ):

        node = self.mHead

        while node:
            if node.mData == key:
                break
            node = node.mRight
        
        return node

    def Remove( self, node : DllNode ):

        if node == self.mHead:
            return self.RemoveHead()
        elif node == self.mTail:
            return self.RemoveTail()
        else:
            node.Detach()
            self.mCount -= 1
            return node
    
    def __str__( self ):
        res = ""
        node = self.mHead

        while node is not None:
            res += f"{str(node)} ---> "
            node = node.mRight

        return res
    

class DllTester:

    TESTER_RANGE = 100
    
    def __init__(self):
        self.dll : Dll = None

    def TestInit( self ):
        self.dll = Dll()
        assert self.dll.mCount == 0
        assert self.dll.mHead == self.dll.mTail == None
        return True

    def TestAppend( self ):

        res : bool = True
        
        for i in range( self.TESTER_RANGE ):
            self.dll.Append( i )
            if self.dll.mTail.mData == i:
                if self.dll.mCount == (i + 1):
                    pass
                else:
                    res = False
                    print(f"Invalid count: Expected {i + 1}, Actual {self.dll.mCount}")
            else:
                res = False
                print(f"Invalid Data entry: Expected {i}, Actual {self.dll.mTail.mData}")

        print( self.dll, end = "\n\n" )

        return res

    def TestPrepend( self ):
        
        res : bool = True
        
        for i in range( self.TESTER_RANGE ):
            self.dll.Prepend( i )
            if self.dll.mHead.mData == i:
                if self.dll.mCount == (i + 1):
                    pass
                else:
                    res = False
                    print(f"Invalid count: Expected {i + 1}, Actual {self.dll.mCount}")
                    break
            else:
                res = False
                print(f"Invalid Data entry: Expected {i}, Actual {self.dll.mHead.mData}")
                break

        print( self.dll, end = "\n\n" )
    
        return res


    def TestRemove( self ):

        res:bool = False

        elements = [ i for i in range(self.TESTER_RANGE) ]
        shuffle( elements )

        for i in elements:

            node = self.dll.Find( i )
    
            if node is not None:
                element = self.dll.Remove( node )
                if element.mData == i:
                    pass
                else:
                    print(f"Data mismatch: {i} != {element.mData}")
                    break
            else:
                print("Node not found")
                break

        if self.dll.mCount > 0:
            print(f"Not all elements deleted {self.dll.mCount}")

        if len(str(self.dll)) > 0:
            print(f"Note contains elements: {(self.dll)}")

        if self.dll.mHead is not None:
            print(f"Head is not none")
        
        if self.dll.mTail is not None:
            print(f"Tail is not none")
        
        return True

    @staticmethod
    def RunTests():
        tester = DllTester()
        if tester.TestInit():
            if tester.TestAppend():
                if tester.TestRemove():
                    if tester.TestPrepend():
                        if tester.TestRemove():
                            print("All tests passed")
                        else:
                            print("Failed Remove 1")
                    else:
                        print("Failed Prepend")
                else:
                    print("Failed Remove 2")
            else:
                print("Failed Append")
        else:
            print("Failed Init")
