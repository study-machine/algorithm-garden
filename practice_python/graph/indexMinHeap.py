def swap(arr,a,b):
    arr[a],arr[b]=arr[b],arr[a]
class IndexMinHeap(object):
    def __init__(self,n):
        self.capacity=n
        self.data=[None for _ in xrange(n)]
        self.indexs=[-1 for _ in xrange(n)]
        self.reverse=[-1 for _ in xrange(n)]
        self.__count = 0

    def insert(self,index,item):
        self.data[index]=item
        self.indexs[self.__count]=index
        self.reverse[index]=self.__count
        self.__count+=1
        self.__shift_up(self.__count-1)

    def __shift_up(self,k):
        while k>0 and self.data[self.indexs[k]]<self.data[self.indexs[(k-1)/2]]:
            swap(self.indexs,k,(k-1)/2)
            self.reverse[self.indexs[k]]=k
            self.reverse[self.indexs[(k-1)/2]]=(k-1)/2
            k=(k-1)/2

    def extract_min(self):
        ret = self.data[self.indexs[0]]
        swap(self.indexs,0,self.__count-1)
        self.reverse[self.indexs[0]]=0
        self.reverse[self.indexs[self.__count-1]]=-1
        self.__count-=1
        self.__shift_down(0)
        return ret
    def extract_min_index(self):
        ret = self.indexs[0]
        swap(self.indexs,0,self.__count-1)
        self.reverse[self.indexs[0]]=0
        self.reverse[self.indexs[self.__count-1]]=-1
        self.__count-=1
        self.__shift_down(0)
        return ret

    def __shift_down(self,k):
        while k*2+1<self.__count:
            j = k*2+1
            if j+1<self.__count and self.data[self.indexs[j]]>self.data[self.indexs[j+1]]:
                j+=1
            if self.data[self.indexs[k]]<self.data[self.indexs[j]]:
                break
            swap(self.indexs,k,j)
            self.reverse[self.indexs[k]]=k
            self.reverse[self.indexs[j]]=j
            k=j

    def is_empty(self):
        return self.__count==0
    @property
    def size(self):
        return self.__count
    def get_item(self,index):
        return self.data[index]
    def contain(self,index):
        return self.reverse[index]!=-1

    def change(self,index,item):
        self.data[index]=item
        self.__shift_up(self.reverse[index])
        self.__shift_down(self.reverse[index])

if __name__ == '__main__':
    from random import randint
    n=8
    # arr = [randint(0,100) for _ in xrange(n)]
    # print arr
    # mh=MinIndexHeap(n)
    # for i,v in enumerate(arr):
    #     mh.insert(i,v)
    # print '1:',mh.indexs
    # mh.change(0,999)

    # for x in xrange(n):
    #     print mh.extract_min(),
    # print ''
    # print mh.data

    # print mh.indexs
    # print mh.reverse

