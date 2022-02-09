import math
from heapq import heapify, heappop, heappush
from collections import defaultdict
import math


def length_haversine(p1, p2):
    lat1 = p1.lat
    lng1 = p1.lng
    lat2 = p2.lat
    lng2 = p2.lng
    lat1, lng1, lat2, lng2 = map(math.radians, [lat1, lng1, lat2, lng2])
    dlat = lat2 - lat1
    dlng = lng2 - lng1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))

    return 6372797.560856 * c  # return the distance in meters


def group_closest_node_id(nodes):
    """ group all nodes in grids to make it easier for "get_closest_node_id"
    through grids instead of all nodes"""
    grid_dict = defaultdict(list)
    for node in nodes.values():
        k_for_dict = (round(node.lat, 3), round(node.lng, 3))
        grid_dict[k_for_dict].append(node)
    return grid_dict

def get_closest_node_id_old(nodes, source_node):
    """ Search through all nodes and return the id of the node
    that is closest to 'source_node'. """
    mindist = float("inf")
    closest = None
    for node in nodes.values():
        if length_haversine(node, source_node) < mindist:
            mindist = length_haversine(node, source_node)
            closest = node
    return closest.id
def get_closest_node_id(grid_dict, source_node):
    """ Search through all nodes and return the id of the node
    that is closest to 'source_node'. """

    closest_node = None
    closest = float('inf')
    key = (round(source_node.lat, 3), round(source_node.lng, 3))
    for node in grid_dict[key]:
        if length_haversine(source_node, node) < closest:
            closest_node = node
            closest = length_haversine(source_node, node)

    return closest_node.id


def find_shortest_path(nodes, source_id, target_id):
    """ Return the shortest path using Dijkstra's algortihm. """
    for node in nodes.values():
        node.distance = float('inf')
        node.path = []

    source_node = nodes[source_id]
    target_node = nodes[target_id]
    queue = [source_node]
    source_node.distance = 0
    source_node.path = [source_node.id]

    heapify(queue)
    visited = set()
    while queue:
        node = heappop(queue)
        if node not in visited:
            visited.add(node)
            if node.id == target_id:
                break
            else:
                for neighbor in node.neighbors:
                    neighbor_node = nodes[neighbor]
                    if node.distance + length_haversine(node, neighbor_node) < neighbor_node.distance:
                        neighbor_node.distance = node.distance + length_haversine(node, neighbor_node)
                        cp = node.path.copy()

                        neighbor_node.path = cp
                        neighbor_node.path.append(neighbor_node.id)
                        if neighbor_node in queue:
                            heapify(queue)
                        else:
                            heappush(queue, neighbor_node)

    return target_node.path
