import random
import copy
from LRUCache import lru
from DoubleLinkedList import DllTester

class TesterData:
    def __init__(self, call, args ):
        self.call = call
        self.args = args

    def __str__(self):
        return f"{self.call}({','.join(self.args)})"

cache = lru( 5 )

def extractCommands( line : str ):
    res = ""
    inArgs = False
    for char in line:

        if char == '(':
           inArgs = True
        elif char == ")":
            inArgs = False
        elif char  == ',':
            if inArgs is False:
                yield res #copy.deepcopy(res)
                res = ""
                continue
        res += char


def TestLruCache():

    testFile = "Inputs.txt"
    testerData : list[TesterData] = []
    
    with open( testFile, "r" ) as fp:

        for line in fp.readlines():
            # print(line)
            if( len(line) > 0 ):

                start, end = 0, 0

                for command in extractCommands(line):

                    if command.find("Get") == 0:
                        start = 3
                    elif command.find("Put") == 0:
                        start = 3
                    elif command.find("Update") == 0:
                        start = 6
                        pass

                    if start > 0:
                        end = command.find(')', start)
                        call = command[:start]
                        args = command[start + 1 : end ].split(",")
                        testerData.append(TesterData( call, args))
                        # print(f"Call {call}; Args {args}")

                for data in testerData:
                    
                    if data.call == "Get":
                        cache.Get( int(data.args[0]) )
                    elif data.call == "Put":
                        cache.Put( int(data.args[0]), data.args[1] )
                    elif data.call == "Update":
                        cache.Update( int(data.args[0]), data.args[1] )
                        pass
                    pass
                    
                    print(f"{str(data)} {cache.Show()}", end="\n")

                # Clear test data
                testerData.clear()

                print("\n\n")
        fp.close()

def TestDll():
    DllTester.RunTests()

if __name__ == "__main__":
    TestDll()
    TestLruCache()
