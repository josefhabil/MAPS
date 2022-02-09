from lib import run_server, get, post
from lib import read_html
from store import Node, extract_osm_nodes, add_neighbors
from algorithms import get_closest_node_id, find_shortest_path, group_closest_node_id, get_closest_node_id_old
import store
from algorithms import get_closest_node_id, find_shortest_path
import hashlib
import json
import time

nodes = extract_osm_nodes("linkoping.osm")
add_neighbors(nodes)
grid_dict = group_closest_node_id(nodes)


@get('/hello')
def hello():
    return 'Hello World'

@get('/')
def index():
    return read_html('templates/index.html')

@get('/register')
def register():

    username = ""
    password = ""
    dict = {}
    dict.update({username:password})


@get('login')
def login():
    pass



@get ('/favicon.ico')
def favicon():
    with open("data/favicon.ico", "rb") as f:
        icon = b""
        byte = f.read(1)
        while byte != b"":
            icon += byte
            byte = f.read(1)
        return icon

#@get('/show-area')
#def show_area():
    #all = dict()
    #for node in store.select_nodes_in_rectangle(store.extract_osm_nodes("map"), 58.3984, 58.3990, 15.5733, 15.576):
     #   all[node.id] = node.coord_tuple()
   # return json.dumps(all)


@post('/shortest-path')
def shortest_path(body):
    body = json.loads(body)

    start = time.time()
    source_id = get_closest_node_id_old(nodes, Node('-1', body['lat1'], body['lng1']))

    target_id = get_closest_node_id_old(nodes, Node('-1', body['lat2'], body['lng2']))

    end = time.time()
    print("old: " + str(end - start))


    start = time.time()
    source_id = get_closest_node_id(grid_dict, Node('-1', body['lat1'], body['lng1']))

    target_id = get_closest_node_id(grid_dict, Node('-1', body['lat2'], body['lng2']))

    end = time.time()
    print("new: " + str(end - start))

    path = find_shortest_path(nodes, source_id, target_id)

    for i in range(len(path)):
        node_id = path[i]
        path[i] = (nodes[node_id].lat, nodes[node_id].lng)
        # path[i] = (nodes[source_id].lat, nodes[target_id].lng)
    response = {'path': path}

    return json.dumps(response)


@get('/favicon.ico')
def favicon():
    with open("data/favicon.ico", "rb") as f:
        bytes = f.read()
        return bytes  # get can return bytes


run_server()
