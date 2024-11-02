class Heap:
    def __init__(self, lst):
        self.tree = lst 
        self.make_heap(lst)
    def make_heap(self, lst):
        k = 0
        for i in range(len(lst)):
            k += 1
            j = k -1 
            while (j-1) // 2 >= 0 and self.tree[(j-1) //2] < self.tree[j]:
                tmp = self.tree[(j-1) //2]
                self.tree[(j-1) //2] = self.tree[j]
                self.tree[j] = tmp 
                j = (j - 1) // 2
    def get_max(self):
        return self.tree[0]
    def add(self, x):
        self.tree.append(x)
        j = len(self.tree) - 1
        while (j-1) // 2 >= 0 and self.tree[(j-1) //2] < self.tree[j]:
                tmp = self.tree[(j-1) //2]
                self.tree[(j-1) //2] = self.tree[j]
                self.tree[j] = tmp 
                j = (j - 1) // 2
    def delmax(self):
        self.tree[0] = self.tree[-1]
        self.tree.pop()
        i = 0
        while 2*i + 1 < len(self.tree):
            if 2*i + 2 < len(self.tree):
                a = self.tree[2*i+1]
                b = self.tree[2*i+2]
                if self.tree[i] >= max(a, b):
                    break
                elif a == max(a, b):
                    self.tree[2*i+1] = self.tree[i]
                    self.tree[i] = a
                    i = 2*i+1
                else:
                    self.tree[2*i+2] = self.tree[i]
                    self.tree[i] = b
                    i = 2*i+2
            else:
                if self.tree[2*i+1] > self.tree[i]:
                    tmp = self.tree[2*i+1]
                    self.tree[2*i+1] = self.tree[i]
                    self.tree[i] = tmp
                    i = 2*i+1
                else: break
    def __str__(self) -> str:
        return str(self.tree)

def p_s(lst):
    h = Heap(lst)
    print(h)
    l = []
    for i in range(len(lst)):
        l.append(h.get_max())
        h.delmax()
    return l


print(p_s([1,3, 4, 5, 3, 6]))