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


        LengthOfCommonPrefix = 0
        length = min(len(word),len(self.previousWord))
        for i in range(length):
            if word[i] == self.previousWord[i]:
                LengthOfCommonPrefix += 1
            else:
                break

        self.minimize(LengthOfCommonPrefix)
        if len(self.uncheckedNodes) == 0:
            CurrentNode = self.root
        else:
            CurrentNode = self.uncheckedNodes[-1][2]



        for l in word[LengthOfCommonPrefix:]:
            NextNode= DawgNode()
            CurrentNode.children[l] = NextNode
            self.uncheckedNodes.append( (CurrentNode,l,NextNode) )
            CurrentNode =NextNode
        
        CurrentNode.EndOfWord=True
        self.previousWord=word



    def minimize(self, min):
        for i in range(len(self.uncheckedNodes)-1,min-1,-1):
            parent, letter, child = self.uncheckedNodes.pop()
            if child in self.minimisedNodes:
                parent.children[letter]= self.minimisedNodes[child]
            else:
                self.minimisedNodes[child]= child


    
    def finish(self):
        self.minimize(0)

    def search(self,word):
        node=self.root
        for l in word:
            if l not in node.children:
                return False
            node = node.children[l]
        return node.EndOfWord

    




            
            
            
