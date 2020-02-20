import math
from Persistent_seg_tree import Pers_Seg_tree
from Persistent_seg_tree import Node 
# version array for storing multiple versions of tree
version=[Node()]*100

if __name__=='__main__':
    print("Enter the size of input array: ")
    n=int(input())
    print("Enter the elements of input array: ")
    inp_arr=list(map(int,input().split()))
    obj=Pers_Seg_tree()
    root=Node()
    root.val=0
    print("Building version 0 .............................")
    obj.construct_seg_tree(inp_arr,0,n-1,root)
    version[0]=root
    print("Completed................................")
    print(version[0].val)
    i=1
    flag=0
    while flag!=1:
        print("Do you wish to upgrade version......")
        ch=input()
        if ch=='YES' or ch=='yes':
            curr_ver=Node()
            curr_ver.val=0
            print("Enter index of update........")
            indx=int(input())
            print("Enter value to update.........")
            value=int(input())
            obj.upgrade_version(version[i-1],curr_ver,0,n-1,indx,value)
            version[i]=curr_ver
            print("Upgradation completed...........")
            obj.printLevelOrder(version[i])
            print("Leaf Nodes:- ")
            obj.printLeafNodes(version[i])
            print('')
            i+=1   
            if i==4:
                print("It was the last upgradation of this series.Further upgradation will replace the existing one........")
                i=1
        else:
            flag=1
    pri=0
    while pri!=1:
        print("Which version to print............")
        ver=int(input())
        print("Level order structure of tree......")
        obj.printLevelOrder(version[ver])
        print("Leaf Nodes: ")
        obj.printLeafNodes(version[ver])
        print('')
        print("Do you still wish to print.........")
        pref=input()
        if pref=='no' or pref=='NO':
            pri=1