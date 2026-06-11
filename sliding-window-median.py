class LazyHeap:
    def __init__(self, is_min_heap):
        self.heap = []
        self.is_min_heap = is_min_heap
        self.delayed_removals = {}
        self.actual_size = 0

    def _should_swap(self, a, b):
        return a < b if self.is_min_heap else a > b

    def push(self, value):
        self.heap.append(value)
        self.actual_size += 1
        self._sift_up(len(self.heap) - 1)

    def peek(self):
        self._clean_top()
        return self.heap[0] if self.heap else None

    def pop(self):
        self._clean_top()
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        value = self.heap.pop()
        self._sift_down(0)
        self.actual_size -= 1
        return value

    def remove_later(self, value):
        self.delayed_removals[value] = self.delayed_removals.get(value, 0) + 1
        self.actual_size -= 1
        self._clean_top()

    def _clean_top(self):
        while self.heap and self.delayed_removals.get(self.heap[0], 0):
            value = self.heap[0]
            self._swap(0, len(self.heap) - 1)
            self.heap.pop()
            self._sift_down(0)
            self.delayed_removals[value] -= 1
            if self.delayed_removals[value] == 0:
                del self.delayed_removals[value]

    def size(self):
        return self.actual_size

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self._should_swap(self.heap[index], self.heap[parent]):
                self._swap(index, parent)
                index = parent
            else:
                break

    def _sift_down(self, index):
        size = len(self.heap)
        while 2 * index + 1 < size:
            child = 2 * index + 1
            if child + 1 < size and self._should_swap(self.heap[child + 1], self.heap[child]):
                child += 1
            if self._should_swap(self.heap[child], self.heap[index]):
                self._swap(child, index)
                index = child
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def balance_heaps(lower_half, upper_half):
    while lower_half.size() > upper_half.size() + 1:
        upper_half.push(lower_half.pop())
    while upper_half.size() > lower_half.size():
        lower_half.push(upper_half.pop())


def calculate_median(lower_half, upper_half, window_size):
    if window_size % 2 == 1:
        return f"{float(lower_half.peek()):.1f}"
    else:
        return f"{(lower_half.peek() + upper_half.peek()) / 2.0:.1f}"


def get_sliding_medians(window_size, numbers):
    lower_half = LazyHeap(False)  
    upper_half = LazyHeap(True)   
    medians = []

    for i in range(len(numbers)):
        num = numbers[i]
        if lower_half.size() == 0 or num <= lower_half.peek():
            lower_half.push(num)
        else:
            upper_half.push(num)

        if i >= window_size:
            old_num = numbers[i - window_size]
            if old_num <= lower_half.peek():
                lower_half.remove_later(old_num)
            else:
                upper_half.remove_later(old_num)

        balance_heaps(lower_half, upper_half)

        if i >= window_size - 1:
            medians.append(calculate_median(lower_half, upper_half, window_size))

    return medians


def main():
    k = int(input())  
    nums = list(map(int, input().split())) 
    medians = get_sliding_medians(k, nums)
    print(' '.join(medians))


if __name__ == "__main__":
    main()