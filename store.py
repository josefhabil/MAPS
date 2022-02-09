# from osm_parser import get_default_parser
# from store import Node


import json
from osm_parser import get_default_parser
from algorithms import length_haversine


class Node:
    def __init__(self, id, lat, lng):
        self.id = id
        self.lat = float(lat)
        self.lng = float(lng)
        self.neighbors = []  # list of nodes: ['4224', '3141592, ...]
        self.distance = float('inf')
        self.path = []

    def __lt__(self, other_heap_item):
        return self.distance < other_heap_item.distance # We want to rank by distance

    def coord_tuple(self):
        return self.lat, self.lng


parser = None  # Have a global reusable parser object


def extract_osm_nodes(f_name):
    global parser
    parser = get_default_parser(f_name)
    nodes = dict()

    for node in parser.iter_nodes():
        nodes[node['id']] = Node(node['id'], node['lat'], node['lon'])

    return nodes


def select_nodes_in_rectangle(nodes, minlat, maxlat, minlng, maxlng):
    lst = []
    for (k, node) in nodes.items():
        if minlat < node.lat < maxlat:
            if minlng < node.lng < maxlng:
                lst.append(node)
    return lst


def add_neighbors(nodes):
    for way in parser.iter_ways():
        road = way['road']
        for i in range(len(road) - 1):
            node1 = road[i]
            node2 = road[i + 1]
            if node1 and node2:
                nodes[node1].neighbors.append(node2)
                nodes[node2].neighbors.append(node1)
        pass #Dont know why
    return nodes



def get_closest_node_id(nodes, source_node):
    """ Search through all nodes and return the id of the node
    that is closest to 'source_node'. """
    mindist = float('inf')
    closest = None
    for node in nodes.values():
        if length_haversine(node, source_node) < mindist:
            mindist = length_haversine(node, source_node)
            closest = node
    return closest.id
