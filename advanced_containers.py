"""
Advanced Container ADTs - Week 3
CSC 242 - Object-Oriented Programming

This file demonstrates advanced Abstract Data Type implementations:
- Multiple queue implementations with trade-offs
- Stack variations and applications
- Deque (double-ended queue) implementation
- Circular buffers and ring queues
- Container protocol compliance

Author: CSC 242 Teaching Team
"""

from collections import deque as collections_deque
import time


# ============================================================================
# QUEUE IMPLEMENTATIONS COMPARISON
# ============================================================================

print("📦 ADVANCED CONTAINER ADTs")
print("=" * 60)

class ListQueue:
    """Queue using list with front at index 0 (inefficient dequeue)"""
    
    def __init__(self):
        """Initialize empty queue"""
        self._items = []
        self._enqueue_count = 0
        self._dequeue_count = 0
    
    def enqueue(self, item):
        """Add item to rear (efficient - O(1))"""
        self._items.append(item)
        self._enqueue_count += 1
    
    def dequeue(self):
        """Remove item from front (inefficient - O(n))"""
        if not self._items:
            raise IndexError("dequeue from empty queue")
        
        item = self._items.pop(0)  # O(n) operation!
        self._dequeue_count += 1
        return item
    
    def front(self):
        """Peek at front item"""
        if not self._items:
            raise IndexError("front of empty queue")
        return self._items[0]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
    
    def get_stats(self):
        """Return performance statistics"""
        return {
            'type': 'ListQueue',
            'size': len(self._items),
            'enqueue_count': self._enqueue_count,
            'dequeue_count': self._dequeue_count,
            'efficiency': 'O(1) enqueue, O(n) dequeue'
        }
    
    def __str__(self):
        return f"ListQueue({self._items})"


class ReverseListQueue:
    """Queue using list with front at end (inefficient enqueue)"""
    
    def __init__(self):
        """Initialize empty queue"""
        self._items = []
        self._enqueue_count = 0
        self._dequeue_count = 0
    
    def enqueue(self, item):
        """Add item to rear at index 0 (inefficient - O(n))"""
        self._items.insert(0, item)  # O(n) operation!
        self._enqueue_count += 1
    
    def dequeue(self):
        """Remove item from front at end (efficient - O(1))"""
        if not self._items:
            raise IndexError("dequeue from empty queue")
        
        item = self._items.pop()  # O(1) operation
        self._dequeue_count += 1
        return item
    
    def front(self):
        """Peek at front item (at end of list)"""
        if not self._items:
            raise IndexError("front of empty queue")
        return self._items[-1]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
    
    def get_stats(self):
        """Return performance statistics"""
        return {
            'type': 'ReverseListQueue',
            'size': len(self._items),
            'enqueue_count': self._enqueue_count,
            'dequeue_count': self._dequeue_count,
            'efficiency': 'O(n) enqueue, O(1) dequeue'
        }
    
    def __str__(self):
        # Show in logical order (front to rear)
        return f"ReverseListQueue({list(reversed(self._items))})"


class TwoStackQueue:
    """Queue implemented using two stacks (amortized O(1))"""
    
    def __init__(self):
        """Initialize with two stacks"""
        self._enqueue_stack = []  # For new items
        self._dequeue_stack = []  # For removing items
        self._enqueue_count = 0
        self._dequeue_count = 0
        self._transfer_count = 0
    
    def enqueue(self, item):
        """Add item to enqueue stack (O(1))"""
        self._enqueue_stack.append(item)
        self._enqueue_count += 1
    
    def dequeue(self):
        """Remove item, transferring if needed (amortized O(1))"""
        if not self._dequeue_stack and not self._enqueue_stack:
            raise IndexError("dequeue from empty queue")
        
        # Transfer items if dequeue stack is empty
        if not self._dequeue_stack:
            while self._enqueue_stack:
                self._dequeue_stack.append(self._enqueue_stack.pop())
                self._transfer_count += 1
        
        item = self._dequeue_stack.pop()
        self._dequeue_count += 1
        return item
    
    def front(self):
        """Peek at front item"""
        if not self._dequeue_stack and not self._enqueue_stack:
            raise IndexError("front of empty queue")
        
        # Transfer if needed to see front item
        if not self._dequeue_stack:
            while self._enqueue_stack:
                self._dequeue_stack.append(self._enqueue_stack.pop())
                self._transfer_count += 1
        
        return self._dequeue_stack[-1]
    
    def is_empty(self):
        return len(self._enqueue_stack) == 0 and len(self._dequeue_stack) == 0
    
    def size(self):
        return len(self._enqueue_stack) + len(self._dequeue_stack)
    
    def get_stats(self):
        """Return performance statistics"""
        return {
            'type': 'TwoStackQueue',
            'size': self.size(),
            'enqueue_count': self._enqueue_count,
            'dequeue_count': self._dequeue_count,
            'transfer_count': self._transfer_count,
            'efficiency': 'Amortized O(1) both operations'
        }
    
    def __str__(self):
        # Reconstruct logical order
        items = list(reversed(self._dequeue_stack)) + self._enqueue_stack
        return f"TwoStackQueue({items})"


# ============================================================================
# CIRCULAR BUFFER QUEUE
# ============================================================================

class CircularQueue:
    """Queue using circular buffer for maximum efficiency"""
    
    def __init__(self, capacity):
        """Initialize with fixed capacity"""
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        
        self._buffer = [None] * capacity
        self._capacity = capacity
        self._size = 0
        self._front = 0
        self._rear = 0
        self._enqueue_count = 0
        self._dequeue_count = 0
    
    def enqueue(self, item):
        """Add item to rear (O(1))"""
        if self._size >= self._capacity:
            raise OverflowError(f"Queue is full (capacity: {self._capacity})")
        
        self._buffer[self._rear] = item
        self._rear = (self._rear + 1) % self._capacity
        self._size += 1
        self._enqueue_count += 1
    
    def dequeue(self):
        """Remove item from front (O(1))"""
        if self._size == 0:
            raise IndexError("dequeue from empty queue")
        
        item = self._buffer[self._front]
        self._buffer[self._front] = None  # Help garbage collection
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        self._dequeue_count += 1
        return item
    
    def front(self):
        """Peek at front item"""
        if self._size == 0:
            raise IndexError("front of empty queue")
        return self._buffer[self._front]
    
    def is_empty(self):
        return self._size == 0
    
    def is_full(self):
        return self._size >= self._capacity
    
    def size(self):
        return self._size
    
    def capacity(self):
        return self._capacity
    
    def get_stats(self):
        """Return performance statistics"""
        return {
            'type': 'CircularQueue',
            'size': self._size,
            'capacity': self._capacity,
            'utilization': f"{(self._size/self._capacity)*100:.1f}%",
            'enqueue_count': self._enqueue_count,
            'dequeue_count': self._dequeue_count,
            'efficiency': 'O(1) both operations'
        }
    
    def to_list(self):
        """Convert to list in logical order"""
        if self._size == 0:
            return []
        
        result = []
        index = self._front
        for _ in range(self._size):
            result.append(self._buffer[index])
            index = (index + 1) % self._capacity
        return result
    
    def __iter__(self):
        """Iterate in logical order (front to rear)"""
        index = self._front
        for _ in range(self._size):
            yield self._buffer[index]
            index = (index + 1) % self._capacity
    
    def __str__(self):
        return f"CircularQueue({self.to_list()}, capacity={self._capacity})"


# ============================================================================
# DEQUE IMPLEMENTATION
# ============================================================================

class Deque:
    """Double-ended queue implementation"""
    
    def __init__(self):
        """Initialize empty deque"""
        self._items = []
        self._operations = {
            'add_front': 0,
            'add_rear': 0,
            'remove_front': 0,
            'remove_rear': 0
        }
    
    def add_front(self, item):
        """Add item to front"""
        self._items.insert(0, item)
        self._operations['add_front'] += 1
    
    def add_rear(self, item):
        """Add item to rear"""
        self._items.append(item)
        self._operations['add_rear'] += 1
    
    def remove_front(self):
        """Remove and return item from front"""
        if not self._items:
            raise IndexError("remove_front from empty deque")
        
        item = self._items.pop(0)
        self._operations['remove_front'] += 1
        return item
    
    def remove_rear(self):
        """Remove and return item from rear"""
        if not self._items:
            raise IndexError("remove_rear from empty deque")
        
        item = self._items.pop()
        self._operations['remove_rear'] += 1
        return item
    
    def front(self):
        """Peek at front item"""
        if not self._items:
            raise IndexError("front of empty deque")
        return self._items[0]
    
    def rear(self):
        """Peek at rear item"""
        if not self._items:
            raise IndexError("rear of empty deque")
        return self._items[-1]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
    
    def clear(self):
        """Remove all items"""
        self._items.clear()
    
    def get_stats(self):
        """Return operation statistics"""
        return {
            'type': 'Deque',
            'size': len(self._items),
            'operations': self._operations.copy(),
            'total_operations': sum(self._operations.values())
        }
    
    # Support queue interface
    def enqueue(self, item):
        """Alias for add_rear (queue compatibility)"""
        self.add_rear(item)
    
    def dequeue(self):
        """Alias for remove_front (queue compatibility)"""
        return self.remove_front()
    
    # Support stack interface
    def push(self, item):
        """Alias for add_rear (stack compatibility)"""
        self.add_rear(item)
    
    def pop(self):
        """Alias for remove_rear (stack compatibility)"""
        return self.remove_rear()
    
    def peek(self):
        """Alias for rear (stack compatibility)"""
        return self.rear()
    
    def __iter__(self):
        """Iterate from front to rear"""
        return iter(self._items)
    
    def __len__(self):
        return len(self._items)
    
    def __contains__(self, item):
        return item in self._items
    
    def __str__(self):
        return f"Deque({self._items})"
    
    def __repr__(self):
        return f"Deque({self._items!r})"


# ============================================================================
# STACK VARIATIONS
# ============================================================================

class MonitoredStack:
    """Stack with operation monitoring and statistics"""
    
    def __init__(self, max_size=None):
        """Initialize stack with optional size limit"""
        self._items = []
        self._max_size = max_size
        self._stats = {
            'push_count': 0,
            'pop_count': 0,
            'peek_count': 0,
            'max_size_reached': 0
        }
        self._peak_size = 0
    
    def push(self, item):
        """Push item onto stack"""
        if self._max_size and len(self._items) >= self._max_size:
            self._stats['max_size_reached'] += 1
            raise OverflowError(f"Stack overflow (max size: {self._max_size})")
        
        self._items.append(item)
        self._stats['push_count'] += 1
        
        # Update peak size
        if len(self._items) > self._peak_size:
            self._peak_size = len(self._items)
    
    def pop(self):
        """Pop item from stack"""
        if not self._items:
            raise IndexError("pop from empty stack")
        
        item = self._items.pop()
        self._stats['pop_count'] += 1
        return item
    
    def peek(self):
        """Peek at top item"""
        if not self._items:
            raise IndexError("peek at empty stack")
        
        self._stats['peek_count'] += 1
        return self._items[-1]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def is_full(self):
        return self._max_size and len(self._items) >= self._max_size
    
    def size(self):
        return len(self._items)
    
    def capacity(self):
        return self._max_size
    
    def get_stats(self):
        """Get comprehensive statistics"""
        return {
            'type': 'MonitoredStack',
            'current_size': len(self._items),
            'peak_size': self._peak_size,
            'max_size': self._max_size,
            'operations': self._stats.copy(),
            'utilization': f"{(len(self._items)/(self._max_size or len(self._items) or 1))*100:.1f}%"
        }
    
    def reset_stats(self):
        """Reset all statistics"""
        self._stats = {
            'push_count': 0,
            'pop_count': 0,
            'peek_count': 0,
            'max_size_reached': 0
        }
        self._peak_size = len(self._items)
    
    def __iter__(self):
        """Iterate from top to bottom"""
        return reversed(self._items)
    
    def __len__(self):
        return len(self._items)
    
    def __str__(self):
        if self.is_empty():
            return "MonitoredStack(empty)"
        return f"MonitoredStack(top={self.peek()}, size={len(self._items)})"


# ============================================================================
# PERFORMANCE COMPARISON
# ============================================================================

def performance_comparison():
    """Compare performance of different queue implementations"""
    print("\n" + "=" * 60)
    print("⚡ PERFORMANCE COMPARISON")
    print("=" * 60)
    
    # Create different queue implementations
    queues = [
        ("ListQueue", ListQueue()),
        ("ReverseListQueue", ReverseListQueue()),
        ("TwoStackQueue", TwoStackQueue()),
        ("CircularQueue", CircularQueue(1000)),  # Large capacity
        ("collections.deque", collections_deque())
    ]
    
    # Performance test parameters
    num_operations = 1000
    
    print(f"\nPerformance test with {num_operations} operations each:")
    print(f"{'Queue Type':<20} {'Enqueue Time':<15} {'Dequeue Time':<15} {'Total Time':<12}")
    print("-" * 65)
    
    results = []
    
    for name, queue in queues:
        # Test enqueue performance
        start_time = time.time()
        for i in range(num_operations):
            if name == "CircularQueue" and hasattr(queue, 'is_full') and queue.is_full():
                break
            if hasattr(queue, 'enqueue'):
                queue.enqueue(f"item_{i}")
            else:  # collections.deque
                queue.append(f"item_{i}")
        enqueue_time = time.time() - start_time
        
        # Test dequeue performance
        start_time = time.time()
        dequeued_count = 0
        while dequeued_count < num_operations:
            try:
                if hasattr(queue, 'dequeue'):
                    queue.dequeue()
                else:  # collections.deque
                    queue.popleft()
                dequeued_count += 1
            except (IndexError, OverflowError):
                break
        dequeue_time = time.time() - start_time
        
        total_time = enqueue_time + dequeue_time
        
        print(f"{name:<20} {enqueue_time:.6f}s      {dequeue_time:.6f}s      {total_time:.6f}s")
        
        results.append((name, enqueue_time, dequeue_time, total_time))
    
    # Show efficiency analysis
    print(f"\n📊 Efficiency Analysis:")
    fastest = min(results, key=lambda x: x[3])
    slowest = max(results, key=lambda x: x[3])
    
    print(f"  Fastest: {fastest[0]} ({fastest[3]:.6f}s)")
    print(f"  Slowest: {slowest[0]} ({slowest[3]:.6f}s)")
    print(f"  Speed difference: {slowest[3]/fastest[3]:.1f}x")


def demonstrate_queue_implementations():
    """Show different queue implementations in action"""
    print("\n🔄 Queue Implementation Comparison:")
    
    # Test all queue types with same operations
    queue_types = [
        ("ListQueue", ListQueue()),
        ("ReverseListQueue", ReverseListQueue()),
        ("TwoStackQueue", TwoStackQueue()),
        ("CircularQueue", CircularQueue(5))
    ]
    
    operations = ["A", "B", "C"]
    
    for name, queue in queue_types:
        print(f"\n  {name}:")
        
        # Enqueue operations
        for item in operations:
            queue.enqueue(item)
            print(f"    Enqueued {item}: {queue}")
        
        # Dequeue operations
        while not queue.is_empty():
            item = queue.dequeue()
            print(f"    Dequeued {item}: {queue}")
        
        # Show statistics
        if hasattr(queue, 'get_stats'):
            stats = queue.get_stats()
            print(f"    Stats: {stats['efficiency']}")


def demonstrate_deque_functionality():
    """Show deque as both queue and stack"""
    print(f"\n📦 Deque Multi-Purpose Usage:")
    
    dq = Deque()
    
    # Use as queue (FIFO)
    print(f"\n  Using as Queue (FIFO):")
    dq.enqueue("first")
    dq.enqueue("second")
    dq.enqueue("third")
    print(f"    After enqueuing: {dq}")
    
    print(f"    Dequeuing: {dq.dequeue()}")  # Should be "first"
    print(f"    After dequeue: {dq}")
    
    # Use as stack (LIFO)
    print(f"\n  Using as Stack (LIFO):")
    dq.push("fourth")
    dq.push("fifth")
    print(f"    After pushing: {dq}")
    
    print(f"    Popping: {dq.pop()}")  # Should be "fifth"
    print(f"    After pop: {dq}")
    
    # Use deque-specific operations
    print(f"\n  Using Deque-specific operations:")
    dq.add_front("new_first")
    dq.add_rear("new_last")
    print(f"    After add_front and add_rear: {dq}")
    
    print(f"    Front: {dq.front()}, Rear: {dq.rear()}")
    
    # Show statistics
    stats = dq.get_stats()
    print(f"    Operation stats: {stats['operations']}")


def demonstrate_stack_monitoring():
    """Show monitored stack capabilities"""
    print(f"\n📊 Stack Monitoring:")
    
    stack = MonitoredStack(max_size=5)
    
    # Perform various operations
    operations = [
        ("push", "A"),
        ("push", "B"),
        ("push", "C"),
        ("peek", None),
        ("pop", None),
        ("push", "D"),
        ("push", "E"),
        ("push", "F"),
        ("push", "G"),  # Should reach max size
    ]
    
    for operation, value in operations:
        try:
            if operation == "push":
                stack.push(value)
                print(f"    Pushed {value}: {stack}")
            elif operation == "pop":
                item = stack.pop()
                print(f"    Popped {item}: {stack}")
            elif operation == "peek":
                item = stack.peek()
                print(f"    Peeked {item}: {stack}")
        except (IndexError, OverflowError) as e:
            print(f"    Error: {e}")
    
    # Show comprehensive statistics
    stats = stack.get_stats()
    print(f"\n    Final Statistics:")
    for key, value in stats.items():
        print(f"      {key}: {value}")


# ============================================================================
# MAIN DEMONSTRATION FUNCTION
# ============================================================================

def main():
    """Run all container ADT demonstrations"""
    print("📦 ADVANCED CONTAINER ADTs - CSC 242 Week 3")
    print("=" * 60)
    
    demonstrate_queue_implementations()
    demonstrate_deque_functionality()
    demonstrate_stack_monitoring()
    performance_comparison()
    
    print(f"\n" + "=" * 60)
    print("✅ All container ADT demonstrations complete!")
    
    print(f"\n💡 Key Container Concepts:")
    print(f"   1. Algorithm efficiency matters (O(1) vs O(n))")
    print(f"   2. Different implementations have different trade-offs")
    print(f"   3. Circular buffers provide optimal performance")
    print(f"   4. Deques offer maximum flexibility")
    print(f"   5. Monitoring helps optimize usage patterns")
    print(f"   6. Choose the right tool for your specific needs")
    
    print(f"\n🎯 Performance Insights:")
    print(f"   • ListQueue: Simple but inefficient dequeue")
    print(f"   • TwoStackQueue: Complex but amortized efficiency")
    print(f"   • CircularQueue: Best performance with fixed size")
    print(f"   • collections.deque: Built-in optimized solution")


if __name__ == "__main__":
    main()
