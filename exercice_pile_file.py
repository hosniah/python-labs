class Pile():
    def __init__(self, size):
        assert isinstance(size, int) and size > 0
        self.size=size
        self.pointer=size
        self.tab=[0]*size

    def pop(self):
        if not self.empty():
            res=self.tab[self.pointer]
            self.pointer=self.pointer+1
            return res
        else:
            raise Exception

    def push(self, obj):
        if not self.full():
            self.pointer=self.pointer-1
            self.tab[self.pointer]=obj
        else:
            raise Exception

    def empty(self):
        return(self.pointer==self.size)
    
    def full(self):
        return(self.pointer==0)

class File:
    def __init__(self, size)
        self.p1=Pile(size)
        self.p2=Pile(size)

        def empty(self):
            return self.p1.empty()
        
        def full(self):
            return self.p1.full()

        def add(self, obj):
            return self.p1.push(obj)
        
        def get(self):
            while not self.p1.empty():
                self.p2.push(self.p1.pop())
            res=self.p2.pop()
            while not self.p2.empty():
                self.p1.push(self.p2.pop())
            return res
