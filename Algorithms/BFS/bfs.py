def breadth_first_search(graph, start):
  # create an empty queue
  queue = []
  # create an empty set to store visited nodes
  visited = set()
  # enqueue the starting node
  queue.append(start)
  # while the queue is not empty
  while queue:
    # dequeue a node
    node = queue.pop(0)
    # if the node has not been visited
    if node not in visited:
      # mark it as visited
      visited.add(node)
      # enqueue all of its neighbors
      for neighbor in graph[node]:
        queue.append(neighbor)
  # return the visited set
  return visited