from DoubleLinkedList import DllNode, Dll
from dataclasses import dataclass


@dataclass
class CachedData:
    id = None
    data = None
    
    def __init__(self, id, data ):
        self.id = id
        self.data = data

    def __str__(self):
        return f"[{self.id}, {self.data}]"


class lru:

    def __init__(self, mSize ):
        self.mCount = 0
        self.mSize = mSize
        self.mCached = Dll()       # Linked list for data
        self.mLookup = {}                       # reference to node containing the data

    def Get( self, id ):
        data = None
        # Find reference if it exists in the dictionary
        if id in self.mLookup:
            # Get the node
            node : DllNode = self.mLookup[id]

            self.mCached.Remove( node )

            # Move node to the front of the cache
            node = self.mCached.Prepend( node.mData )

            # Update node referenced in lookup table
            self.mLookup.pop( id )
            self.mLookup[id] = node

            data = node.mData

        return data

    def Put( self, id, data ):

        if id in self.mLookup:
            self.Update( id, data )
        else:
            newData = CachedData( id, data )

            if self.mCount >= self.mSize:
                rmNode : DllNode = self.mCached.RemoveTail()
                rmData : CachedData = rmNode.mData
                self.mLookup.pop( rmData.id )
                del rmNode
            else:
                self.mCount += 1

            node = self.mCached.Prepend( newData )
            self.mLookup[id] = node

        pass

    def Update( self, id, data ):

        if id in self.mLookup:

            node : DllNode = self.mLookup[id]

            # remove the node from the cache list
            self.mCached.Remove( node ) 

            # Update value of new data
            node.mData = CachedData( id, data )

            # Move node to the front of the cache
            node = self.mCached.Prepend( node.mData )

            # Update the node reference in the lookup table
            self.mLookup.pop( id )
            self.mLookup[id] = node


    def Show( self ):
        return str(self.mCached)