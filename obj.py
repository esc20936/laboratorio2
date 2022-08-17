
class Obj(object):
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.lines = file.read().splitlines()

        self.vertices = []
        self.texcoords = []
        self.normals = []
        self.faces = []

        for line in self.lines:
            try:
                line = line.strip()
                prefix, value = line.split(' ', 1)
            except:
                continue

            if prefix == 'v': # Vertices
                self.vertices.append( list(map(float,value.split(' '))))
            elif prefix == 'vt':
                self.texcoords.append( list(map(float, value.split(' '))))
            elif prefix == 'vn':
                self.normals.append( list(map(float, value.split(' '))))
            elif prefix == 'f':
                vertList = []
                for vert in value.split(' '):
                   indices = vert.split('/')
                   for x in range(0,len(indices)):
                        if indices[x] == '':
                            indices[x]=0
                   indices = map(int, indices)
                   indices = list(indices)
                   vertList.append(indices)
                self.faces.append(vertList)

       


            




        
