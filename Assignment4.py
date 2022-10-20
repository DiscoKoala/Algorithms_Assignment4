import math
from LinkedList import *
# Import from LinkedList object file
def hashFunc(k):
    hashResult = math.floor(((math.floor(k)+6)**3)/(17+k)%13)
    return hashResult

def main():
    # Write a hash function that takes as input a key k and computes the value
    L = [ LinkedList(Node(0)) for _ in range(13)]
    keys = [43, 22, 1 ,0, 15, 31, 99, 218, 4, 7, 11, 3, 9]
    for x in range(13):
        slot = hashFunc(keys[x])
        if(LinkedList(Node(keys[x])).list_empty() == True ):
            L[slot].add_front(Node(keys[x]))
            #L[slot].listprint()
        else:
            L[slot] = LinkedList(Node(keys[x]))

    for i in range(13):
        LL = L[i]
        LL.listprint()
        if(LL.list_empty() == False):
            print(0)

if __name__ == "__main__":
    main()
