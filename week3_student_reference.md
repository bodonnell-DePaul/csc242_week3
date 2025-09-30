# Week 3 Student Reference Guide
**CSC 242 - Object-Oriented Programming**  
**Topic:** Iterators, Container ADTs, Custom Exceptions, and Advanced Data Structures

---

## 📚 Table of Contents
1. [Extending Superclass Methods](#1-extending-superclass-methods)
2. [Iterator Protocol](#2-iterator-protocol)
3. [Custom Iterator Classes](#3-custom-iterator-classes)
4. [Container Abstract Data Types](#4-container-abstract-data-types)
5. [Exception Handling Review](#5-exception-handling-review)
6. [Custom Exceptions](#6-custom-exceptions)
7. [Advanced Queue Implementations](#7-advanced-queue-implementations)
8. [Stack Data Structure](#8-stack-data-structure)
9. [Best Practices and Design Patterns](#9-best-practices-and-design-patterns)
10. [Practice Problems](#10-practice-problems)

---

## 1. Extending Superclass Methods

### Method Extension vs Method Replacement
When creating subclasses, you have several options for handling inherited methods:

#### Complete Replacement
```python
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):  # Completely replaces parent method
        return "Hello from Child"
```

#### Method Extension with super()
```python
class Parent:
    def process(self):
        print("Starting parent process")
        return "parent_result"

class Child(Parent):
    def process(self):
        print("Child preprocessing")
        parent_result = super().process()  # Call parent method
        print("Child postprocessing")
        return f"child_enhanced_{parent_result}"

# Usage
child = Child()
result = child.process()
# Output:
# Child preprocessing
# Starting parent process
# Child postprocessing
# Returns: "child_enhanced_parent_result"
```

#### Multiple Extension Patterns
```python
class Logger:
    def log(self, message):
        print(f"LOG: {message}")

class TimestampLogger(Logger):
    def log(self, message):
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        super().log(f"[{timestamp}] {message}")

class FileLogger(TimestampLogger):
    def __init__(self, filename):
        self.filename = filename
    
    def log(self, message):
        super().log(message)  # Still use parent's timestamp logic
        with open(self.filename, 'a') as f:
            f.write(f"{message}\n")
```

### Best Practices for Method Extension
1. **Always call super()** when extending behavior
2. **Place super() call appropriately** (beginning, middle, or end)
3. **Handle return values** from parent methods
4. **Maintain method contracts** (expected parameters and return types)

---

## 2. Iterator Protocol

### Understanding Python's Iterator Protocol
The iterator protocol is what makes `for` loops work with any object:

```python
# Behind the scenes, this:
for item in container:
    print(item)

# Is equivalent to:
iterator = iter(container)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
```

### Making Objects Iterable
To make your class iterable, implement the `__iter__()` method:

```python
class NumberRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1

# Usage
for num in NumberRange(1, 5):
    print(num)  # Prints 1, 2, 3, 4
```

### Simple Iterator with Built-in Collections
```python
class WordContainer:
    def __init__(self):
        self.words = []
    
    def add_word(self, word):
        self.words.append(word)
    
    def __iter__(self):
        return iter(self.words)  # Delegate to list's iterator
    
    def __len__(self):
        return len(self.words)
    
    def __contains__(self, word):
        return word in self.words
```

---

## 3. Custom Iterator Classes

### Creating Custom Iterator Classes
For more control over iteration, create separate iterator classes:

```python
class ReverseIterator:
    """Iterator that traverses a sequence in reverse order"""
    
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = len(sequence)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        self.index -= 1
        return self.sequence[self.index]

class ReversibleList:
    def __init__(self, items=None):
        self.items = items or []
    
    def __iter__(self):
        return iter(self.items)  # Normal iteration
    
    def __reversed__(self):
        return ReverseIterator(self.items)  # Reverse iteration

# Usage
rev_list = ReversibleList([1, 2, 3, 4, 5])

print("Forward:")
for item in rev_list:
    print(item)  # 1, 2, 3, 4, 5

print("Reverse:")
for item in reversed(rev_list):
    print(item)  # 5, 4, 3, 2, 1
```

### Iterator with State Management
```python
class ChunkedIterator:
    """Iterator that returns items in chunks of specified size"""
    
    def __init__(self, sequence, chunk_size):
        self.sequence = sequence
        self.chunk_size = chunk_size
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.sequence):
            raise StopIteration
        
        chunk = self.sequence[self.index:self.index + self.chunk_size]
        self.index += self.chunk_size
        return chunk

# Usage
chunked = ChunkedIterator([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
for chunk in chunked:
    print(chunk)  # [1, 2, 3], [4, 5, 6], [7, 8, 9]
```

### Generator Functions (Simplified Iterators)
```python
def fibonacci_generator(n):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def even_numbers(start, end):
    """Generate even numbers in range"""
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num

# Usage
for fib in fibonacci_generator(10):
    print(fib)  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

evens = list(even_numbers(1, 20))
print(evens)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

---

## 4. Container Abstract Data Types

### Queue (FIFO - First In, First Out)

#### Basic Queue Implementation
```python
class Queue:
    """First-In-First-Out (FIFO) container"""
    
    def __init__(self):
        self._items = []
        self._size = 0
    
    def enqueue(self, item):
        """Add item to rear of queue"""
        self._items.append(item)
        self._size += 1
    
    def dequeue(self):
        """Remove and return item from front of queue"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        
        item = self._items.pop(0)
        self._size -= 1
        return item
    
    def front(self):
        """Return front item without removing it"""
        if self.is_empty():
            raise IndexError("front of empty queue")
        return self._items[0]
    
    def is_empty(self):
        """Check if queue is empty"""
        return self._size == 0
    
    def size(self):
        """Return number of items in queue"""
        return self._size
    
    def __len__(self):
        return self._size
    
    def __iter__(self):
        """Iterate from front to rear"""
        return iter(self._items)
    
    def __repr__(self):
        return f"Queue({self._items})"
    
    def __str__(self):
        if self.is_empty():
            return "Queue(empty)"
        return f"Queue(front={self.front()}, size={self.size()})"
```

#### Alternative Queue Implementation (Reverse Order)
```python
class ReverseQueue:
    """Queue implemented with rear at index 0"""
    
    def __init__(self):
        self._items = []
    
    def enqueue(self, item):
        """Add item to rear (index 0)"""
        self._items.insert(0, item)
    
    def dequeue(self):
        """Remove item from front (last index)"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop()
    
    def is_empty(self):
        return len(self._items) == 0
    
    def __iter__(self):
        """Custom iterator: front to rear"""
        return reversed(self._items)
```

### Queue as List Subclass
```python
class ListQueue(list):
    """Queue implemented as list subclass"""
    
    def enqueue(self, item):
        self.append(item)
    
    def dequeue(self):
        if not self:
            raise IndexError("dequeue from empty queue")
        return self.pop(0)
    
    def front(self):
        if not self:
            raise IndexError("front of empty queue")
        return self[0]
    
    def is_empty(self):
        return len(self) == 0

# Note: This exposes all list methods, which may not be desired
# Users can call queue.insert(), queue.remove(), etc.
```

---

## 5. Exception Handling Review

### Basic Exception Handling
```python
# Single exception type
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exception types
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid number format!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions in one clause
try:
    # risky operation
    pass
except (ValueError, TypeError, KeyError) as e:
    print(f"Multiple possible errors: {e}")
```

### Exception Information
```python
try:
    # risky operation
    result = int("not_a_number")
except ValueError as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
    print(f"Error args: {e.args}")
```

### Finally and Else Clauses
```python
def safe_file_operation(filename):
    try:
        file = open(filename, 'r')
        data = file.read()
        return data
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except PermissionError:
        print(f"Permission denied for {filename}")
        return None
    else:
        print("File read successfully")
    finally:
        try:
            file.close()
            print("File closed")
        except:
            pass  # File was never opened
```

### Re-raising Exceptions
```python
def process_data(data):
    try:
        # Process the data
        result = complex_operation(data)
        return result
    except ValueError as e:
        print(f"Logging error: {e}")
        raise  # Re-raise the same exception
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise RuntimeError("Data processing failed") from e
```

---

## 6. Custom Exceptions

### Creating Custom Exception Classes
```python
# Basic custom exception
class EmptyQueueError(Exception):
    """Raised when attempting to dequeue from empty queue"""
    pass

# Custom exception with additional information
class QueueFullError(Exception):
    """Raised when attempting to enqueue to full queue"""
    
    def __init__(self, message, capacity=None):
        super().__init__(message)
        self.capacity = capacity

# Exception with custom behavior
class InvalidOperationError(Exception):
    """Raised for invalid operations on data structures"""
    
    def __init__(self, operation, container_type, reason=None):
        self.operation = operation
        self.container_type = container_type
        self.reason = reason
        
        message = f"Invalid operation '{operation}' on {container_type}"
        if reason:
            message += f": {reason}"
        
        super().__init__(message)
    
    def __str__(self):
        return f"{self.args[0]} (operation: {self.operation})"
```

### Exception Hierarchy
```python
class DataStructureError(Exception):
    """Base exception for all data structure errors"""
    pass

class EmptyStructureError(DataStructureError):
    """Raised when operating on empty data structure"""
    pass

class FullStructureError(DataStructureError):
    """Raised when adding to full data structure"""
    pass

class InvalidIndexError(DataStructureError):
    """Raised for invalid index operations"""
    pass

# Usage in queue class
class SafeQueue:
    def __init__(self, max_size=None):
        self._items = []
        self._max_size = max_size
    
    def enqueue(self, item):
        if self._max_size and len(self._items) >= self._max_size:
            raise FullStructureError(
                f"Queue is full (capacity: {self._max_size})"
            )
        self._items.append(item)
    
    def dequeue(self):
        if not self._items:
            raise EmptyStructureError("Cannot dequeue from empty queue")
        return self._items.pop(0)
```

### Exception Context and Chaining
```python
class DataProcessingError(Exception):
    """Raised when data processing fails"""
    
    def __init__(self, message, original_error=None):
        super().__init__(message)
        self.original_error = original_error

def process_queue_item(item):
    try:
        # Some complex processing
        result = complex_calculation(item)
        return result
    except ValueError as e:
        raise DataProcessingError(
            f"Failed to process item {item}"
        ) from e  # Exception chaining
    except Exception as e:
        raise DataProcessingError(
            f"Unexpected error processing {item}",
            original_error=e
        )
```

---

## 7. Advanced Queue Implementations

### Bounded Queue with Custom Exceptions
```python
class BoundedQueue:
    """Queue with maximum capacity and custom exceptions"""
    
    def __init__(self, max_size):
        if max_size <= 0:
            raise ValueError("Queue size must be positive")
        
        self._items = []
        self._max_size = max_size
    
    def enqueue(self, item):
        """Add item to queue, raise exception if full"""
        if len(self._items) >= self._max_size:
            raise QueueFullError(
                f"Queue is full (capacity: {self._max_size})",
                capacity=self._max_size
            )
        self._items.append(item)
    
    def dequeue(self):
        """Remove item from queue, raise exception if empty"""
        if not self._items:
            raise EmptyQueueError("Cannot dequeue from empty queue")
        return self._items.pop(0)
    
    def is_full(self):
        return len(self._items) >= self._max_size
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
    
    def capacity(self):
        return self._max_size
    
    def remaining_capacity(self):
        return self._max_size - len(self._items)
```

### Circular Buffer Queue
```python
class CircularQueue:
    """Efficient queue using circular buffer"""
    
    def __init__(self, capacity):
        self._buffer = [None] * capacity
        self._capacity = capacity
        self._size = 0
        self._front = 0
        self._rear = 0
    
    def enqueue(self, item):
        if self._size >= self._capacity:
            raise QueueFullError("Circular queue is full")
        
        self._buffer[self._rear] = item
        self._rear = (self._rear + 1) % self._capacity
        self._size += 1
    
    def dequeue(self):
        if self._size == 0:
            raise EmptyQueueError("Circular queue is empty")
        
        item = self._buffer[self._front]
        self._buffer[self._front] = None  # Help garbage collection
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return item
    
    def __iter__(self):
        """Iterate from front to rear"""
        index = self._front
        for _ in range(self._size):
            yield self._buffer[index]
            index = (index + 1) % self._capacity
```

### Priority Queue
```python
import heapq

class PriorityQueue:
    """Queue where items are processed by priority"""
    
    def __init__(self):
        self._heap = []
        self._index = 0  # For stable sorting
    
    def enqueue(self, item, priority=0):
        """Add item with priority (lower number = higher priority)"""
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1
    
    def dequeue(self):
        """Remove highest priority item"""
        if not self._heap:
            raise EmptyQueueError("Priority queue is empty")
        
        priority, index, item = heapq.heappop(self._heap)
        return item
    
    def peek(self):
        """Return highest priority item without removing"""
        if not self._heap:
            raise EmptyQueueError("Priority queue is empty")
        return self._heap[0][2]
    
    def is_empty(self):
        return len(self._heap) == 0
```

---

## 8. Stack Data Structure

### Basic Stack Implementation
```python
class Stack:
    """Last-In-First-Out (LIFO) container"""
    
    def __init__(self):
        self._items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self._items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if self.is_empty():
            raise EmptyStructureError("Cannot pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        """Return top item without removing"""
        if self.is_empty():
            raise EmptyStructureError("Cannot peek at empty stack")
        return self._items[-1]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        """Iterate from top to bottom"""
        return reversed(self._items)
    
    def __repr__(self):
        return f"Stack({self._items})"
    
    def __str__(self):
        if self.is_empty():
            return "Stack(empty)"
        return f"Stack(top={self.peek()}, size={self.size()})"
```

### Stack with Iterator
```python
class IterableStack:
    """Stack with custom iterator"""
    
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        if not self._items:
            raise EmptyStructureError("Empty stack")
        return self._items.pop()
    
    def __iter__(self):
        return StackIterator(self._items)

class StackIterator:
    """Iterator for stack (top to bottom)"""
    
    def __init__(self, items):
        self._items = items
        self._index = len(items)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index <= 0:
            raise StopIteration
        self._index -= 1
        return self._items[self._index]
```

---

## 9. Best Practices and Design Patterns

### Container Design Principles
1. **Consistent Interface**: Use standard method names (push/pop, enqueue/dequeue)
2. **Error Handling**: Provide meaningful exceptions
3. **Iterator Support**: Make containers iterable
4. **Memory Efficiency**: Consider space complexity
5. **Type Safety**: Consider type hints and validation

### Exception Design Guidelines
```python
# Good: Specific, informative exceptions
class StackUnderflowError(Exception):
    """Raised when popping from empty stack"""
    
    def __init__(self, operation="pop"):
        self.operation = operation
        super().__init__(f"Cannot {operation} from empty stack")

# Better: Exception with context
class ContainerError(Exception):
    """Base exception for container operations"""
    
    def __init__(self, message, container_type=None, operation=None):
        super().__init__(message)
        self.container_type = container_type
        self.operation = operation
        
    def __str__(self):
        base_msg = super().__str__()
        if self.container_type and self.operation:
            return f"{base_msg} ({self.container_type}.{self.operation})"
        return base_msg
```

### Iterator Best Practices
```python
class WellDesignedContainer:
    """Example of good container design"""
    
    def __init__(self):
        self._items = []
    
    def __iter__(self):
        """Return iterator - don't modify during iteration"""
        return iter(self._items.copy())  # Safe iteration
    
    def __len__(self):
        return len(self._items)
    
    def __contains__(self, item):
        return item in self._items
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __bool__(self):
        return bool(self._items)
```

---

## 10. Practice Problems

### Problem 1: Deque Implementation
Create a double-ended queue (deque) that supports:
- `add_front(item)` and `add_rear(item)`
- `remove_front()` and `remove_rear()`
- Iterator support
- Custom exceptions

### Problem 2: Undo/Redo System
Implement an undo/redo system using stacks:
- `execute(command)` - execute and store command
- `undo()` - undo last command
- `redo()` - redo last undone command
- Support for command objects

### Problem 3: Expression Evaluator
Create a stack-based expression evaluator:
- Parse infix expressions
- Convert to postfix
- Evaluate postfix expressions
- Handle parentheses and operator precedence

### Problem 4: Custom Exception Hierarchy
Design a complete exception hierarchy for:
- File processing errors
- Network communication errors
- Data validation errors
- Include error codes and recovery suggestions

### Problem 5: Iterator Patterns
Implement various iterator patterns:
- Filtered iterator (skip certain items)
- Transformed iterator (apply function to items)
- Batched iterator (return items in groups)
- Infinite iterator (generate endless sequence)

---

## 🎯 Key Takeaways

1. **Method Extension**: Use `super()` to extend rather than replace parent functionality
2. **Iterator Protocol**: Implement `__iter__()` and `__next__()` for custom iteration
3. **Container Design**: Focus on clear interfaces and appropriate error handling
4. **Custom Exceptions**: Create specific, informative exception types
5. **Performance Considerations**: Choose appropriate data structures for your use case
6. **Code Reuse**: Leverage inheritance and composition effectively

---

## 📚 Additional Resources

- **Python Documentation**: Iterator Protocol and Exception Handling
- **Design Patterns**: Iterator, Command, and Template Method patterns
- **Data Structures**: "Python Data Structures and Algorithms" by Kent Lee
- **Best Practices**: PEP 8 for coding style, PEP 257 for documentation

Remember: Good container design makes code more readable, maintainable, and efficient. Always consider your users' needs when designing interfaces!
