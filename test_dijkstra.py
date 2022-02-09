from collections import defaultdict
from heapq import heappush, heappop
import math

def dijkstra(adjacency_list, source_id, target_id):
    """ To be implemented by students (optional exercise). `adjacency_list` is a dictionary with structure: 
    {node_id: [...(neighbor_id, weight)]}.
    Function should return (distance, path). Path should be a list of the nodes in the shortest path
    **including** the source_id and target_id. If no shortest path is found, it should return (float('inf'), []) """
    return float('inf'), []


if __name__ == '__main__':
    file = open('data/dijkstra.test') # Feel free to add your own test cases to the file!
    testcase = 0
    try:
        while True:
            num_nodes = file.readline()
            if num_nodes[0] == '#':
                continue 
            testcase += 1
            num_nodes = int(num_nodes)
            source, target = map(int, file.readline().split())
            nodes = []
            for n in range(num_nodes):
                x, y = map(float, file.readline().split())
                nodes.append((x, y))
            adjacency_list = defaultdict(list)
            num_edges = int(file.readline())
            for m in range(num_edges):
                v1, v2 = map(int, file.readline().split())
                x1, y1 = nodes[v1]
                x2, y2 = nodes[v2]
                weight = math.hypot(x2-x1, y2-y1) # Get distance between the nodes
                adjacency_list[v1].append((v2, weight))
                adjacency_list[v2].append((v1, weight))
            correct_dist = float(file.readline())
            correct_path = [int(v) for v in file.readline().split()]
            dist, path = dijkstra(adjacency_list, source, target)
            assert abs(correct_dist-dist) < 1e-3
            assert correct_path == path
            print("Passed test case {}".format(testcase))
    except AssertionError:
        print("Failed test case {}".format(testcase))
    except IndexError:
        print('Passed all test cases')
    except EOFError:
        print('Passed all test cases')
    
