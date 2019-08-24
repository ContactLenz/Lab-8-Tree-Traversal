## Part 1
class BinaryTree:
    def __init__(self, spec):
        if type(spec) is tuple or type(spec) is list:
            self.data = spec[0]
            if len(spec) == 1:
                self.leftChild, self.rightChild = None, None
            else:
                self.leftChild = BinaryTree(spec[1])
                self.rightChild = BinaryTree(spec[2])
        else:
            self.data = spec
            self.leftChild = None
            self.rightChild = None

    def printpreorder(self):
        print(self.data)
        if self.leftChild:
            self.leftChild.printpreorder()
        if self.rightChild:
            self.rightChild.printpreorder()

class Tree:
    def __init__(self, spec):
        if type(spec) is tuple or type(spec) is list:
            self.data = spec[0]
            self.children = [Tree(subSpec) for subSpec in spec[1:]]
        else:
            self.data = spec
            self.children = []

    def printpreorder(self):
        print(self.data)
        for child in self.children:
            child.printpreorder()

    ## Part 2
    def printbookcontent(self, gate = True, counter = 0):
        if gate:
            print("Book title:", self.data[0])
        for x in self.children:
            if x.children != []:
                counter += 1
            elif x.data[0] == 'References' or x.data[0] == 'Contents':
                counter += 1
            else:
                counter += 0.1
            str1 = str(counter)[:3]+' '+x.data[0] + ', Page ' + str(x.data[1])
            print(str1)
            x.printbookcontent(False, counter)

    def getDepth(self):
        if self.children == []:
            return 0
        else:
            return 1+max(child.getDepth() for child in self.children)

    ## Part 3
    def computespace(self):
        if self.data[1]: #True for files, False for folders
            # print(self.data)
            return self.data[1]
        else:
            sum = 0
            for x in self.children:
                sum += x.computespace()
            # print((self.data[0], sum)) #replace tuple
            self.data = (self.data[0], sum)
            return sum
            # print(self.data)
        # counter = 0
        # sum = 0
        # # self.computespace()
        # for x in self.children:
        #     x.computespace()
        #     if x.data[1] != None:
        #         counter += x.data[1]
        #         # sum += x.data[1]
        #         print(counter)
        #         # return size, print file
        #     else:
        #         print("_________________")
        #         # print files, then print folder, then return sum
        #     # x.computespace()
        # #

    def printExpr(self):
        sOut = ""
        if len(self.children) > 0:
            sOut += '(' + self.children[0].printExpr() + ')'
        sOut += str(self.data)
        if len(self.children) > 1:
            sOut += '(' + self.children[1].printExpr() + ')'
        return sOut

    def computeValue(self):
        childValues = [x.computeValue() for x in self.children]
        return value(self.data, childValues)

    def compute(self, evalFunc):
        childValues = [x.compute(evalFunc) for x in self.children]
        return evalFunc(self.data, childValues)


## Part 4
def value(data, values):
    if type(data) is int and values == []:
        return float(data)
    elif data == 'sum':
        return sum(values)
    elif data == '+':
        return values[0] + values[1]
    elif data == '-':
        return values[0] - values[1]
    elif data == '*':
        return values[0] * values[1]
    elif data == '/':
        return values[0] / values[1]
    elif data == 'max':
        return eval('max')(values)
    elif data == 'min':
        return eval('min')(values)
    elif data == 'avg':
        return sum(values)/len(values)
    # add your code here

## Part 5
def spaceusage(data, values):
    if data[1]: #leaf node / file
        return data[1]
    else: #internal node / folder
        sum = 0
        for x in values:
            sum += x
        return sum



# Tfile = [('CSE1010/', None), [('Section 1', None), [('HWs/', None),
# [('hw1.doc', 5)], [('hw2.doc', 15)]], [('LABs/', None), [('lab1.py', 7)],
# [('lab2.py', 10)], [('lab3.py', 10)]]], [('Section 2', None),
# [('HWs/', None), [('hw1.doc', 5)], [('hw2.doc', 18)]], [('LABs/', None),
# [('lab1.py', 6)], [('lab2.py', 10)], [('lab3.py', 14)]]],
# [('ToDoList.txt', 20)]]
# #
# treeFile = Tree(Tfile)
# # print(treeFile.children[0].children[1].data)
# #
# # # print(treeFile.children[2].data)
# # # print("Original File System Tree:")
# # # treeFile.printpreorder()
# #
# print("\nComputing Space...\n")
# treeFile.computespace()
# print("File System Tree After Computing Space")
# treeFile.printpreorder()
