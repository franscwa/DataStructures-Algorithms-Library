implement djikstras in python with descriptive comments


def dijkstras(graph, source):
    # initialize distances dictionary, all nodes start at infinity except the source
    distances = {node: float("inf") for node in graph}
    distances[source] = 0

    # initialize previous dictionary, all nodes start with None except the source
    previous = {node: None for node in graph}

    # initialize nodes to visit, using a min heap with the source node starting at 0
    nodes_to_visit = [(0, source)]

    # while there are still nodes to visit
    while nodes_to_visit:
        # pop the node with the smallest distance from the heap
        current_distance, current_node = heapq.heappop(nodes_to_visit)

        # if we have already visited the node, continue
        if current_distance > distances[current_node]:
            continue

        # for each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            # calculate the distance to the neighbor by adding the edge weight
            new_distance = current_distance + weight

            # if the new distance is less than the current distance recorded for the neighbor
            if new_distance < distances[neighbor]:
                # update the current distance for the neighbor in the distances dictionary
                distances[neighbor] = new_distance

                # update the previous node for the neighbor in the previous dictionary
                previous[neighbor] = current_node

                # add the neighbor to the nodes to visit heap with the new distance
                heapq.heappush(nodes_to_visit, (new_distance, neighbor))

    # return the distances and previous dictionaries
    return distances, previous