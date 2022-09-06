class DawgNode:
    NextID = 0
    def __init__(self):
        self.id  = DawgNode.NextID
        DawgNode.NextID += 1
        self.EndOfWord = False
        self.children={}





class Dawg:
    def __init__(self):
        self.root = DawgNode()
        self.previousWord= ""
        self.uncheckedNodes=[]
        self.minimisedNodes={}
    
    def insert(self, word):

        CurrentNode = self.root

        LengthOfCommonPrefix = 0
        length = min(len(word),len(self.previousWord))
        for i in range(length):
            if word[i] == self.previousWord[i]:
                LengthOfCommonPrefix += 1
            else:
                break

        if self.uncheckedNodes: 
            CurrentNode = self.minimize(LengthOfCommonPrefix,CurrentNode)

        for l in word[LengthOfCommonPrefix:]:
            NextNode= DawgNode()
            CurrentNode.children[l] = NextNode
            self.uncheckedNodes.append( (CurrentNode,l,NextNode) )
            CurrentNode =NextNode
        
        CurrentNode.EndOfWord=True
        self.previousWord=word



    def minimize(self, min, CurrentNode):
        for i in range(len(self.uncheckedNodes)-1,min,-1):
            parent, letter, child = self.uncheckedNodes.pop()
            if child in self.minimisedNodes:
                parent.children[letter]= self.minimisedNodes[child]
            else:
                self.minimisedNodes[child]= child
            CurrentNode = parent
        return CurrentNode

    def search(self,word):
        node = self.root
        for l in word:
            if l in node.children:
                node = node.children[l]
            else:
                return False
        if node.EndOfWord == True:
            return True
        else:
            return False
            
            
            
