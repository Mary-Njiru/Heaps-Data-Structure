class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, element):
        self.heap.append(element)
        self._bubble_up()

    def _bubble_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def remove_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return root

    def _bubble_down(self, index):
        length = len(self.heap)
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < length and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index
            if right_child_index < length and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest == index:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

# Example usage
min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(1)
min_heap.insert(2)
print(min_heap.remove_min())


# 1. Implement a Min-Heap
# Question: Write a class to implement a min-heap with methods for insertion, deletion of the minimum element, 
# and getting the minimum element.

import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def get_min(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def delete_min(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return heapq.heappop(self.heap)

# Example usage:
heap = MinHeap()
heap.insert(10)
heap.insert(4)
heap.insert(15)
print(heap.get_min())  # Output: 4
print(heap.delete_min())  # Output: 4
print(heap.get_min())  # Output: 10



# 2. Heap Sort
# Question: Implement heap sort using a max-heap to sort an array of integers.

import heapq

def heap_sort(array):
    max_heap = [-x for x in array]
    heapq.heapify(max_heap)
    sorted_array = [-heapq.heappop(max_heap) for _ in range(len(array))]
    return sorted_array

# Example usage:
array = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_array = heap_sort(array)
print(sorted_array)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]



# 3. Build a Heap from an Unsorted Array
# Question: Write a function to build a min-heap from an unsorted array.

import heapq

def build_heap(array):
    heapq.heapify(array)
    return array

# Example usage:
array = [3, 1, 4, 1, 5, 9, 2, 6]
heap = build_heap(array)
print(heap)  # Output: [1, 1, 2, 3, 5, 9, 4, 6]



# 4. Find Kth Smallest Element Using a Min-Heap
# Question: Write a function to find the kth smallest element in an unsorted array using a min-heap.

import heapq

def kth_smallest_element(array, k):
    if k > len(array):
        raise ValueError("k is larger than the size of the array")
    heapq.heapify(array)
    smallest = None
    for _ in range(k):
        smallest = heapq.heappop(array)
    return smallest

# Example usage:
array = [3, 1, 4, 1, 5, 9, 2, 6]
k = 4
print(kth_smallest_element(array, k))  # Output: 4


# 5. Dijkstra’s Algorithm Using a Min-Heap
# Question: Implement Dijkstra’s algorithm to find the shortest path from a source node to all other nodes in a graph using a min-heap.

import heapq

def dijkstra(graph, start):
    # Initialize distances and priority queue
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start = 'A'
distances = dijkstra(graph, start)
print(distances)  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}



