class Node:
    # Node structure:- |left|Node_value|right
    def __init__(self):
        self.val=None
        self.left=None
        self.right=None
class Pers_Seg_tree:
    # Function for constructing first  version of persistent segment tree
    def construct_seg_tree(self,inp_arr,start,end,node):
        if start==end:
            node.val=inp_arr[start]
            return 
        mid=(start+end)//2
        node.left=Node()
        self.construct_seg_tree(inp_arr,start,mid,node.left)
        node.right=Node()
        self.construct_seg_tree(inp_arr,mid+1,end,node.right)

        node.val=node.left.val+node.right.val
    # Function responsible for further upgradation
    def upgrade_version(self,prev_ver,curr_ver,start,end,indx,value):
        if (indx > end or indx < start or start > end): 
            return 

        if start==end:
            curr_ver.val=value
            return
        
        mid=(start+end)//2
        # Condition for saving left or right subtree as per condition of indx
        if indx<=mid:
            curr_ver.right=prev_ver.right
            curr_ver.left=Node()
            curr_ver.left.val=0
            self.upgrade_version(prev_ver.left,curr_ver.left,start,mid,indx,value)
        else:
            curr_ver.left=prev_ver.left
            curr_ver.right=Node()
            curr_ver.right.val=0
            self.upgrade_version(prev_ver.right,curr_ver.right,mid+1,end,indx,value)
        
        curr_ver.val=curr_ver.left.val+curr_ver.right.val

    def print_query(self,node,start,end,l,r):
        print(node.val)
        if (l > end or r < start or start > end): 
            return 0
        if (l <= start and end <= r):
            print(node.val)
            return node.val 
        mid = (start+end) // 2 
        p1=self.print_query(node.left,start,mid,l,r)
        p2=self.print_query(node.right,mid+1,end,l,r)
        return p1+p2
    
    def printLeafNodes(self,root):
        if root is None:
            return 
        
        if root.left==None and root.right==None:
            print(root.val,end=' ')
        
        self.printLeafNodes(root.left)
        self.printLeafNodes(root.right)

    # Level order traversal of tree
    def printLevelOrder(self,root): 
        if root is None: 
            return

        queue = [] 
        queue.append(root)
        level=0
        while(len(queue) > 0): 
            level=len(queue)
            while level>0:
                print(queue[0].val,end=' ') 
                node = queue.pop(0)  
                if node.left is not None: 
                    queue.append(node.left)  
                if node.right is not None: 
                    queue.append(node.right)
                level-=1
            print('')
