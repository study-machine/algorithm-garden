def swap(arr,a,b):
    arr[a],arr[b]=arr[b],arr[a]
class MinHeap(object):
    def __init__(self):
        self.data=[]

    @property
    def count(self):
        return len(self.data)

    def insert(self,item):
        self.data.append(item)
        self.__shift_up(self.count-1)

    def __shift_up(self,k):
        while k>0 and self.data[k]<self.data[(k-1)/2]:
            swap(self.data,k,(k-1)/2)
            k=(k-1)/2

    def extract_min(self):
        ret = self.data[0]
        swap(self.data,0,self.count-1)
        self.data.pop()
        self.__shift_down(0)
        return ret

    def __shift_down(self,k):
        while k*2+1<self.count:
            j = k*2+1
            if j+1<self.count and self.data[j]>self.data[j+1]:
                j+=1
            if self.data[k]<self.data[j]:
                break
            swap(self.data,k,j)
            k=j

    def is_empty(self):
        return self.count==0
