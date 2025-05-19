class Bst:
    class Node:
        def __init__(self) -> None:
            self.pos = None
            self.way = []
            self.key = None
            self.right = None
            self.left = None
            self.parent = None

    def __init__(self):
        self.n = 1
        self.parents = []
        self.root = None
        self.ways = {}

    def insert(self, key):
        new_node = self.Node()
        new_node.key = key
        new_node.pos = self.n
        temp = self.root
        temp_parent = None
        while temp != None :
            temp_parent = temp
            if new_node.key < temp.key :
                new_node.way.append(temp_parent.pos)
                temp = temp.left
            else :
                new_node.way.append(temp_parent.pos)
                temp = temp.right
        new_node.parent = temp_parent
        
        if temp_parent == None :
            self.root = new_node
        elif new_node.key < temp_parent.key :
            temp_parent.left = new_node
            self.parents.append(new_node.parent.key)
        else :
            temp_parent.right = new_node
            self.parents.append(new_node.parent.key)
        new_node.way.append(new_node.pos)
        self.n += 1
        
        self.ways[new_node.pos] = new_node.way

def get_input():
    output = []
    
    input()
    output.append([int(i) for i in input().split()])
    output.append([int(i) for i in input().split()])
    
    return output

def main():        
    bst = Bst()

    inp = get_input()
    for i in inp[0] :
        bst.insert(i)

    for i in bst.parents :
        print(i , end=' ')
    print() 
    way1 = bst.ways[inp[1][0]]
    way2 = bst.ways[inp[1][1]]
    while True :
        if way1[-1] > way2[-1] :
            way1.pop()
        elif way2[-1] > way1[-1] :
            way2.pop()
        elif way1[-1] == way2[-1] :
            print(way1[-1])
            break
    
if __name__ == "__main__":
    main()