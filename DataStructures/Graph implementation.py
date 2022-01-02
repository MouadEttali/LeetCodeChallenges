class Graph:
  def __init__(self,edges):
    self.edges = edges
    self.graph_dict = {}
    for start , end in self.edges:
      if start in self.graph_dict:
        self.graph_dict[start].append(end)
      else:
        self.graph_dict[start]=[end]

  def get_paths(self,start,end,path=[]):
    path = path + [start]
    if start == end:
      return [path]

    if start not in self.graph_dict:
      return []

    paths = []
    for node in self.graph_dict[start]:    # dubai and new york 
      if node not in path:     # if dubai not in path ,  get_paths from dubai to new york 
        new_paths = self.get_paths(node,end,path)  # adds node  dubai to path ( that has already the paris start ) and puts it in new variable new_paths
        for p in new_paths:
          paths.append(p)
    return paths
  
  def get_shortest_path(self,start,end,path=[]):
    path = path + [start]
    if start not in self.graph_dict:
      return None

    if start == end:
      return path

    shortest_path = None
    for node in self.graph_dict[start]:    # dubai and new york 
      if node not in path:     # if dubai not in path ,  get_paths from dubai to new york 
        sp = self.get_shortest_path(node,end,path)
        if sp:
          if shortest_path is None or len(sp) < len(shortest_path):
            shortest_path = sp
    return sp 
