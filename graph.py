
class Graph:
    def __init__(self):
        self.graph = dict()
        self.length = dict()


    def insert_node(self,a,b,c = 0):
        if (a in self.graph) :
            if b not in self.graph[a]:  
                self.graph[a].append(b)
                self.length[a].append(int(c))
        else:
            self.graph[a] = []
            self.length[a] = []
            self.insert_node(a,b,c)


    def lengthf(self,a,b):
        ind = 0
        for i in self.graph[a]:
            if i==b:
                return self.length[a][ind]
            ind+=1


    def short(self,start,end,flag = False):
        self.leng = dict()
        self.spath(start,end)
        index = min(self.leng)
        if flag:
            self.all_length(self.leng,start,end)
        else:
            print('shortest path is : ',end = '')
            print(*self.leng[index],sep = '->')
            print('distance = ',index)


    def all_length(self,leng,a,b):
            print('all paths from %s to %s are: ' % (a,b))
            for i in leng:
                print(*leng[i],sep = '->')
                print('distance = ',i)


    def spath(self,start,end,visited = None):
        if visited is None:
            visited = []

        if start in visited:
            return visited
        else:
            visited.append(start)

        if start == end:
            su = []
            for i in range(1,len(visited)):
                su.append(self.lengthf(visited[i-1],visited[i]))
            self.leng[sum(su)]=[]
            for i in visited:
                self.leng[sum(su)].append(i)

        if start not in self.graph:
            visited = visited[:-1]
            return visited
    
        for next in self.graph[start]:
            visited = self.spath(next,end,visited)
        return visited[:-1]
    

    def all_Traversal(self):
        for i in self.graph:
            print('\n',i,':',sep = '')
            self.Traversal(i)


    def path(self):
        for i in self.graph:
            for j in range(len(self.graph[i])):
                print(i,self.graph[i][j],self.length[i][j],sep = '->')
            

    def Traversal(self,start,visited = None):
        if visited is None:
            visited = []

        if start in visited:
            print(*visited,sep = '->')
            return visited
        else:
            visited.append(start)

        if start not in self.graph:
            print(*visited,sep = '->')
            visited = visited[:-1]
            return visited
       
        for next in self.graph[start]:
            visited = self.Traversal(next,visited)
        return visited[:-1]
