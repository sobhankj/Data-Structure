import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    class Node:
        def __init__(self , key) :
            self.key = key

    def __init__(self):
        self.list = []
        self.numberOfKey = 0
        pass

    def bubble_up(self, index):
        if type(index) != int :
            raise Exception('invalid index')
        if self.numberOfKey == 0:
            raise Exception('empty')
        if index < 0 or index >= self.numberOfKey :
            raise Exception('out of range index')
        
        while index > 0 :
            if (((index - 1) // 2) >= 0) and (self.list[(index - 1) // 2].key > self.list[index].key) :
                self.list[(index - 1) // 2].key , self.list[index].key = self.list[index].key , self.list[(index - 1) // 2].key
            else :
                break
            index = (index - 1) // 2

    def bubble_down(self, index):
        if type(index) != int :
            raise Exception('invalid index')
        if self.numberOfKey == 0:
            raise Exception('empty')
        if index < 0 or index >= self.numberOfKey:
            raise Exception('out of range index')

        min_possion = index
        while 2 * index < self.numberOfKey:
            if 2 * index + 1 < self.numberOfKey and self.list[min_possion].key > self.list[2 * index + 1].key:
                min_possion = 2 * index + 1
            if 2 * index + 2 < self.numberOfKey and self.list[min_possion].key > self.list[2 * index + 2].key:
                min_possion = 2 * index + 2
            if min_possion != index:
                self.list[min_possion].key , self.list[index].key = self.list[index].key , self.list[min_possion].key
                index = min_possion
            else:
                break

    def heap_push(self, value):
        new_node = self.Node(value)
        self.list.append(new_node)
        self.numberOfKey = self.numberOfKey + 1
        self.bubble_up(self.numberOfKey - 1)

    def heap_pop(self):
        if self.numberOfKey == 0 :
            raise Exception('empty')
        root = self.list[0].key
        self.list[0].key = self.list[self.numberOfKey - 1].key
        self.numberOfKey = self.numberOfKey - 1
        self.list.pop()
        if self.numberOfKey != 0 :
            self.bubble_down(0)
        return root

    def find_min_child(self, index):
        if type(index) != int :
            raise Exception('invalid index')
        if index < 0 or index >= self.numberOfKey:
            raise Exception('out of range index')
        if self.numberOfKey == 0:
            raise Exception('empty')
        
        if index * 2 < self.numberOfKey :
            min_possision = index * 2 + 1
            if self.list[index * 2 + 1].key > self.list[index * 2 + 2].key :
                min_possision = index * 2 + 2
        return min_possision

    def heapify(self, *args):
        for new_node in args:
            self.heap_push(new_node)

# class HuffmanTree:
#     class Node:
#         def __init__(self, value, char=None, p=None, l=None, r=None) -> None:
#             self.value = value
#             self.char = char
#             self.parent = p
#             self.L = l
#             self.R = r

#     def __init__(self):
#         self.letters = list()
#         self.repetitions = list()

#     def set_letters(self, *args):
#         self.letters.extend(list(args))

#     def set_repetitions(self, *args):
#         self.repetitions.extend(list(args))

#     def build_huffman_tree(self):
#         chars = list(zip(self.letters, self.repetitions))
#         chars.sort(key = lambda key : key[1],reverse=True)
#         nodes = [self.Node(val, c) for c, val in chars]
#         while len(nodes) >= 2:
#             l = nodes.pop()
#             r = nodes.pop()
#             new_node = self.Node(l.value + r.value, l=l, r=r)
#             l.parent = r.parent = new_node
            
#             for i in range(len(nodes)):
#                 if nodes[i].value < new_node.value:
#                     nodes = nodes[:i] + [new_node] + nodes[i:]
#                     break
#                 if i >= len(nodes) - 1:
#                     nodes += [new_node]
#             if len(nodes) == 0:
#                 nodes = [new_node]
        
#         self.code = dict()
#         self.save_code(nodes[0])

#     def save_code(self, tree, pre_str = ''):
#         if tree == None:
#             return
#         if tree.char != None:
#             self.code[tree.char] = pre_str
#             return

#         self.save_code(tree.L, pre_str + "0")
#         self.save_code(tree.R, pre_str + "1")
        

#     def get_huffman_code_cost(self):
#         chars = dict(zip(self.letters, self.repetitions))
#         output = 0
#         for i in chars.keys():
#             output += chars[i] * len(self.code[i])
#         return output

#     def text_encoding(self, text):
#         # ! time
#         letter_count = {}

#         for letter in text:
#             if letter in letter_count:
#                 letter_count[letter] += 1
#             else:
#                 letter_count[letter] = 1
        
#         self.letters = list(letter_count.keys())
#         self.repetitions = list(letter_count.values())
#         self.build_huffman_tree()

# class HuffmanTree:
#     def __init__(self):
#         self.letters= []
#         self.freqs=[]
#         self.head = None
#         self.encoded = None
  
#     def set_letters(self,*args):
#         self.letters=args
#         self.encoded = {i:None for i in self.letters }

#     def set_repetitions(self,*args):
#         self.freqs=args

#     class Node:
#         def __init__(self,lett,freq,left=None,right=None):
#             self.letter = lett
#             self.freq = freq
#             self.left = left
#             self.right = right
#             self.dir=""
#             #for 1 or 0

#     def build_huffman_tree(self):
#         nodes = list(zip(self.freqs,self.letters))
        
#         nodes = [self.Node(i,j) for j,i in nodes]
#         nodes.sort(key = lambda x : (x.freq,x.letter),reverse=True)
#         while len(nodes)>1:
#            nodes.sort(key = lambda x : (x.freq),reverse=True)
#            r = nodes[-1]
#            l = nodes[-2]
#            nodes = nodes[:-2]
#            r.dir="0"
#            l.dir="1"
#            new_head= self.Node("",r.freq+l.freq,l,r)
#            nodes = [new_head] + nodes
#            self.head = new_head
#         self.encoding(node = self.head)

#     def encoding(self,node,huff =""):
        
#         n = huff + node.dir
#         if node.right:
#             self.encoding(node.right,n)
#         if node.left:
#             self.encoding(node.left,n)
        
#         if not node.right and not node.left:
#             self.encoded[node.letter] = n

        
#     def get_huffman_code_cost(self):
#         res =0
#         index =0
#         for i in self.encoded:
#             res += self.freqs[index]*len(self.encoded[i])
#             index+=1
#         return res
        

#     def text_encoding(self, text):
#         let = {}
#         for i in text:
#             let[i] = let[i]+1 if i in let else 1
#         self.letters= list(let.keys())
#         self.freqs = list(let.values())
#         self.encoded = {i:None for i in self.letters }
#         self.build_huffman_tree()
class HuffmanTree:
    class Node:
        def __init__(self , letter , repetition) -> None:
            self.letter = letter
            self.repetition = repetition
            self.left = None
            self.right = None
            self.way = ''

    def __init__(self):
        self.letters = []
        self.repetitions = []
        self.head = None
        self.encoded = None

    def set_letters(self, *args):
        self.letters = args
        self.encoded = {}
        for i in self.letters :
            self.encoded[i] = None

    def set_repetitions(self, *args):
        self.repetitions = args

    def build_huffman_tree(self):
        new_nodes = list(zip(self.repetitions , self.letters))
        new_nodes = [self.Node(letter , repetition) for repetition , letter , in new_nodes]
        new_nodes.sort(key = lambda x : (x.repetition) , reverse = True)
        while len(new_nodes) > 1:
            new_nodes.sort(key = lambda x : (x.repetition) , reverse=True)
            right = new_nodes[-1]
            left = new_nodes[-2]
            new_nodes = new_nodes[:-2]
            right.way = '0'
            left.way = '1'
            new_head = self.Node('' , right.repetition+left.repetition)
            new_head.left = left
            new_head.right = right
            new_nodes = [new_head] + new_nodes
            self.head = new_head
        self.encoding(node = self.head)
        
    def encoding(self,node,w =""):
        way = w + node.way
        if node.right:
            self.encoding(node.right,way)
        if node.left:
            self.encoding(node.left,way)

        if not node.right and not node.left:
            self.encoded[node.letter] = way
        
    def get_huffman_code_cost(self):
        cost = 0
        index = 0
        for i in self.encoded:
            cost += self.repetitions[index] * len(self.encoded[i])
            index += 1
        return cost

    def text_encoding(self, text):
        letters = {}
        for i in text:
            if letters.get(i) != None :
                letters[i] += 1
            else :
                letters[i] = 1
        self.letters= list(letters.keys())
        self.repetitions = list(letters.values())
        self.encoded = {}
        for i in self.letters :
            self.encoded[i] = None
        self.build_huffman_tree()


class Bst:
    class Node:
        def __init__(self) -> None:
            self.key = None
            self.right = None
            self.left = None
            self.parent = None

    def __init__(self):
        self.parents = []
        self.root = None

    def insert(self, key):
        new_node = self.Node()
        new_node.key = key
        temp = self.root
        temp_parent = None
        while temp != None :
            temp_parent = temp
            if new_node.key < temp.key :
                temp = temp.left
            else :
                temp = temp.right
        new_node.parent = temp_parent
        
        if temp_parent == None :
            self.root = new_node
        elif new_node.key < temp_parent.key :
            temp_parent.left = new_node
        else :
            temp_parent.right = new_node
        self.parents.append(new_node.parent)
    def my_inorder(self , x) :
        if x != None :
            self.my_inorder(x.left)
            self.list.append(x.key)
            self.my_inorder(x.right)
            
    def inorder(self):
        self.list = []
        self.my_inorder(self.root)
        print(*self.list)
        


class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
