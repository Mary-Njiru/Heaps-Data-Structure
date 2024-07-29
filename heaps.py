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