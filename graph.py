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
                return ind
            ind+=1

    def shrtPath(self,start,end,visited):
        l = []
        if end in self.graph[start]:
            return self.lengthf(start,end)
        elif start in visited:
            return 0
        else:
            for i in self.graph[start]:
                su = self.lengthf(start,i)
                x = self.shrtPath(i,end)
                su +=x 
                l.append(su)

    def path(self):
        for i in self.graph:
            for j in range(len(self.graph[i])):
                print(i,self.graph[i][j],self.length[i][j],sep = '->')
            
    def all_paths(self,start,visited = None,value = 0):
        # print(visited)
        if visited is None:
            visited = []
        if start in visited:
            print(*visited,sep = '->')
            print('length =',value)

            # print('','start in visited condition','',sep ='\n')
            return visited
        else:
            visited.append(start)
        if start not in self.graph:
            print(*visited,sep = '->')
            print('length =',value)
            # print('start not in graph condition')
            visited = visited[:-1]
            return visited
        for next in self.graph[start]:
            visited = self.all_paths(next,visited)
        return visited[:-1]
