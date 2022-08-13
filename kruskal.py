def kruskal(graph):
  vertices = graph[0].copy()
  edges = graph[1].copy()
  forest = []
  for vertex in vertices:
    forest.append([vertex])
  total = 0
  
  spanning = []
  flag = False
  edges.sort(key = lambda x: x[2])

  for i in range(len(edges)):
    if len(edges) < 1:
      break
    else:
      inside = []
      for tree in forest:
        for item in tree:
          inside.append(item)
        status = set(vertices) == set(inside)
        if status:
          break
        else:
          u = edges[0][0]
          v = edges[0][1]
          ui = None
          vi = None
        for j in range(len(forest)):
          if u in forest[j]:
            ui = j
          if v in forest[j]:
            vi = j
        if ui != vi:
          try:
            new_tree = forest[ui].copy() + forest[vi].copy()
            x = forest[ui].copy()
            y = forest[vi].copy()
            forest.append(list(set(new_tree)))
            forest.remove(x)
            forest.remove(y)
            total += edges[0][2]
            spanning.append(edges[0])
          except:
            pass

        del edges[0]
  return((spanning, total))
