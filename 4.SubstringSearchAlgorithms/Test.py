from NaiveSearch import NaiveSearch
from RobinKarp import RabinKarpSearch

if __name__ == "__main__":
    haystack, needle = "hello world", "world" 
    print(f"[Naive] Searching for {needle} in {haystack}. Found @ {NaiveSearch(haystack, needle)}")
    print(f"[Robin Karp] Searching for {needle} in {haystack}. Found @ {RabinKarpSearch(haystack, needle)}")
    
    haystack, needle = "This is a test", "test" 
    print(f"[Naive] Searching for {needle} in {haystack}. Found @ {NaiveSearch(haystack, needle)}")
    print(f"[Robin Karp] Searching for {needle} in {haystack}. Found @ {RabinKarpSearch(haystack, needle)}")
    
    haystack, needle = "This is a test", "fest" 
    print(f"[Naive] Searching for {needle} in {haystack}. Found @ {NaiveSearch(haystack, needle)}")
    print(f"[Robin Karp] Searching for {needle} in {haystack}. Found @ {RabinKarpSearch(haystack, needle)}")