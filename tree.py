from stack import Stack

class Node:
    def __init__(self, key, right=None, left=None):
        self.key = key
        self.left = left
        self.right = right


            
def is_operator(char): 
    if char in ['^','*','/','%','+','-']: 
        return True
    else: 
        return False
  

def construct_tree(postfix): 
    stack = Stack()
  
    for char in postfix : 
        if not is_operator(char): 
            node = Node(char) 
            stack.push(node) 

        else: 
            node = Node(char) 
            node1 = stack.pop() 
            node2 = stack.pop() 
                
            node.right = node1
            node.left = node2 

            stack.push(node) 
  
    tree = stack.pop()
    return print_tree(tree) 
  

def print_tree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1  
    nlevels = height(root)
    width =  pow(2,nlevels+1)

    q=[(root,0,width,'c')]
    levels=[]

    while(q):
        node,level,x,align= q.pop(0)
        if node:            
            if len(levels)<=level:
                levels.append([])
        
            levels[level].append([node,level,x,align])
            seg= width//(pow(2,level+1))
            q.append((node.left,level+1,x-seg,'l'))
            q.append((node.right,level+1,x+seg,'r'))

    for i,l in enumerate(levels):
        pre=0
        preline=0
        linestr=''
        pstr=''
        seg= width//(pow(2,i+1))
        for n in l:
            valstr= str(n[0].key)
            if n[3]=='r':
                linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                preline = n[2] 
            if n[3]=='l':
               linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
               preline = n[2] + seg + seg//2
            pstr+=' '*(n[2]-pre-len(valstr))+valstr #correct the potition acording to the number size
            pre = n[2]
        print(linestr)
        print(pstr) 