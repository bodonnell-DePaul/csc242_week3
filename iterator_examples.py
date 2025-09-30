"""
Iterator Examples - Week 3
CSC 242 - Object-Oriented Programming

This file demonstrates various iterator patterns and implementations:
- Basic iterator protocol
- Custom iterator classes
- Generator functions
- Iterator with state management
- Reverse iterators
- Filtered and transformed iterators

Author: CSC 242 Teaching Team
"""


# ============================================================================
# BASIC ITERATOR PROTOCOL
# ============================================================================

print("📋 ITERATOR PROTOCOL FUNDAMENTALS")
print("=" * 60)

class NumberRange:
    """Simple iterable that generates numbers in a range"""
    
    def __init__(self, start, end, step=1):
        """Initialize number range"""
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        """Return iterator object"""
        current = self.start
        while current < self.end:
            yield current
            current += self.step
    
    def __str__(self):
        return f"NumberRange({self.start}, {self.end}, {self.step})"


def demonstrate_basic_iteration():
    """Show basic iteration concepts"""
    print("\n🔄 Basic Iteration:")
    
    # Create iterable object
    numbers = NumberRange(1, 10, 2)
    print(f"Created: {numbers}")
    
    # Iterate using for loop
    print("Using for loop:")
    for num in numbers:
        print(f"  {num}")
    
    # Manual iteration (what for loop does internally)
    print("\nManual iteration:")
    iterator = iter(numbers)
    try:
        while True:
            item = next(iterator)
            print(f"  next() returned: {item}")
    except StopIteration:
        print("  StopIteration raised - iteration complete")
    
    # Demonstrate that iterables can be used multiple times
    print("\nSecond iteration (reusable):")
    for num in numbers:
        print(f"  {num}")


# ============================================================================
# CUSTOM ITERATOR CLASSES
# ============================================================================

class ReverseListIterator:
    """Iterator that traverses a list in reverse order"""
    
    def __init__(self, sequence):
        """Initialize with sequence to iterate over"""
        self.sequence = sequence
        self.index = len(sequence)
    
    def __iter__(self):
        """Return self as iterator"""
        return self
    
    def __next__(self):
        """Return next item in reverse order"""
        if self.index <= 0:
            raise StopIteration
        
        self.index -= 1
        return self.sequence[self.index]


class ChunkedIterator:
    """Iterator that returns items in chunks of specified size"""
    
    def __init__(self, sequence, chunk_size):
        """Initialize chunked iterator"""
        if chunk_size <= 0:
            raise ValueError("Chunk size must be positive")
        
        self.sequence = sequence
        self.chunk_size = chunk_size
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        """Return next chunk"""
        if self.index >= len(self.sequence):
            raise StopIteration
        
        # Get chunk from current index
        chunk = self.sequence[self.index:self.index + self.chunk_size]
        self.index += self.chunk_size
        
        return chunk


class FilteredIterator:
    """Iterator that only returns items matching a predicate"""
    
    def __init__(self, sequence, predicate):
        """Initialize with sequence and filter function"""
        self.sequence = sequence
        self.predicate = predicate
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        """Return next item that matches predicate"""
        while self.index < len(self.sequence):
            item = self.sequence[self.index]
            self.index += 1
            
            if self.predicate(item):
                return item
        
        raise StopIteration


def demonstrate_custom_iterators():
    """Show custom iterator implementations"""
    print("\n" + "=" * 60)
    print("🔧 CUSTOM ITERATOR CLASSES")
    print("=" * 60)
    
    # Test data
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Reverse iterator
    print("\n🔄 Reverse Iterator:")
    reverse_iter = ReverseListIterator(test_list)
    for item in reverse_iter:
        print(f"  {item}")
    
    # Chunked iterator
    print(f"\n📦 Chunked Iterator (chunks of 3):")
    chunked_iter = ChunkedIterator(test_list, 3)
    for chunk in chunked_iter:
        print(f"  {chunk}")
    
    # Filtered iterator
    print(f"\n🎯 Filtered Iterator (even numbers only):")
    even_filter = lambda x: x % 2 == 0
    filtered_iter = FilteredIterator(test_list, even_filter)
    for item in filtered_iter:
        print(f"  {item}")


# ============================================================================
# ENHANCED CONTAINER WITH MULTIPLE ITERATORS
# ============================================================================

class SmartList:
    """List-like container with multiple iteration methods"""
    
    def __init__(self, items=None):
        """Initialize with optional items"""
        self._items = items or []
    
    def append(self, item):
        """Add item to end"""
        self._items.append(item)
    
    def extend(self, items):
        """Add multiple items"""
        self._items.extend(items)
    
    def __len__(self):
        """Return length"""
        return len(self._items)
    
    def __getitem__(self, index):
        """Support indexing"""
        return self._items[index]
    
    def __setitem__(self, index, value):
        """Support item assignment"""
        self._items[index] = value
    
    def __iter__(self):
        """Default iteration (forward)"""
        return iter(self._items)
    
    def __reversed__(self):
        """Support reversed() built-in"""
        return ReverseListIterator(self._items)
    
    def chunks(self, size):
        """Return chunked iterator"""
        return ChunkedIterator(self._items, size)
    
    def filter(self, predicate):
        """Return filtered iterator"""
        return FilteredIterator(self._items, predicate)
    
    def enumerate_items(self, start=0):
        """Return enumerated iterator"""
        return enumerate(self._items, start)
    
    def __repr__(self):
        """Developer representation"""
        return f"SmartList({self._items})"
    
    def __str__(self):
        """User-friendly representation"""
        return f"SmartList with {len(self._items)} items"


def demonstrate_smart_list():
    """Show SmartList with multiple iterator types"""
    print("\n" + "=" * 60)
    print("🧠 SMART LIST WITH MULTIPLE ITERATORS")
    print("=" * 60)
    
    # Create and populate SmartList
    smart_list = SmartList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"Created: {smart_list}")
    
    # Forward iteration
    print(f"\n➡️ Forward iteration:")
    for item in smart_list:
        print(f"  {item}")
    
    # Reverse iteration
    print(f"\n⬅️ Reverse iteration:")
    for item in reversed(smart_list):
        print(f"  {item}")
    
    # Chunked iteration
    print(f"\n📦 Chunked iteration (size 3):")
    for chunk in smart_list.chunks(3):
        print(f"  {chunk}")
    
    # Filtered iteration
    print(f"\n🎯 Filtered iteration (odd numbers):")
    for item in smart_list.filter(lambda x: x % 2 == 1):
        print(f"  {item}")
    
    # Enumerated iteration
    print(f"\n🔢 Enumerated iteration:")
    for index, item in smart_list.enumerate_items():
        print(f"  [{index}]: {item}")


# ============================================================================
# GENERATOR FUNCTIONS (SIMPLIFIED ITERATORS)
# ============================================================================

def fibonacci_generator(n):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(limit):
    """Generate prime numbers up to limit"""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num


def permutation_generator(items):
    """Generate all permutations of items"""
    if len(items) <= 1:
        yield items
    else:
        for i, item in enumerate(items):
            remaining = items[:i] + items[i+1:]
            for permutation in permutation_generator(remaining):
                yield [item] + permutation


def infinite_counter(start=0, step=1):
    """Generate infinite sequence of numbers"""
    current = start
    while True:
        yield current
        current += step


def demonstrate_generators():
    """Show generator function examples"""
    print("\n" + "=" * 60)
    print("⚡ GENERATOR FUNCTIONS")
    print("=" * 60)
    
    # Fibonacci sequence
    print(f"\n🔄 Fibonacci sequence (first 10):")
    for fib in fibonacci_generator(10):
        print(f"  {fib}")
    
    # Prime numbers
    print(f"\n🔢 Prime numbers up to 30:")
    primes = list(prime_generator(30))
    print(f"  {primes}")
    
    # Permutations
    print(f"\n🔀 Permutations of [1, 2, 3]:")
    for perm in permutation_generator([1, 2, 3]):
        print(f"  {perm}")
    
    # Infinite counter (show first 5)
    print(f"\n♾️ Infinite counter (first 5):")
    counter = infinite_counter(10, 2)
    for i, value in enumerate(counter):
        if i >= 5:
            break
        print(f"  {value}")


# ============================================================================
# ITERATOR WITH STATE MANAGEMENT
# ============================================================================

class StatefulIterator:
    """Iterator that maintains complex state during iteration"""
    
    def __init__(self, data):
        """Initialize with data and state"""
        self.data = data
        self.index = 0
        self.visited_indices = set()
        self.cycle_count = 0
        self.max_cycles = 2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        """Complex iteration with state tracking"""
        if self.cycle_count >= self.max_cycles:
            raise StopIteration
        
        if self.index >= len(self.data):
            # Reset for next cycle
            self.index = 0
            self.cycle_count += 1
            
            if self.cycle_count >= self.max_cycles:
                raise StopIteration
        
        # Get current item
        item = self.data[self.index]
        
        # Update state
        self.visited_indices.add(self.index)
        self.index += 1
        
        # Return item with metadata
        return {
            'item': item,
            'index': self.index - 1,
            'cycle': self.cycle_count,
            'visit_count': len(self.visited_indices)
        }


class PeekableIterator:
    """Iterator that allows peeking at next item without consuming it"""
    
    def __init__(self, iterable):
        """Initialize with any iterable"""
        self._iterator = iter(iterable)
        self._next_item = None
        self._has_next = True
        self._advance()
    
    def _advance(self):
        """Get next item from underlying iterator"""
        try:
            self._next_item = next(self._iterator)
        except StopIteration:
            self._has_next = False
            self._next_item = None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        """Return next item"""
        if not self._has_next:
            raise StopIteration
        
        item = self._next_item
        self._advance()
        return item
    
    def peek(self):
        """Return next item without consuming it"""
        if not self._has_next:
            raise StopIteration("No more items to peek")
        return self._next_item
    
    def has_next(self):
        """Check if there are more items"""
        return self._has_next


def demonstrate_stateful_iterators():
    """Show iterators with complex state management"""
    print("\n" + "=" * 60)
    print("🎯 STATEFUL ITERATORS")
    print("=" * 60)
    
    # Stateful iterator with cycles
    print(f"\n🔄 Stateful Iterator (2 cycles):")
    stateful = StatefulIterator(['A', 'B', 'C'])
    for state in stateful:
        print(f"  {state}")
    
    # Peekable iterator
    print(f"\n👀 Peekable Iterator:")
    peekable = PeekableIterator([1, 2, 3, 4, 5])
    
    while peekable.has_next():
        current = next(peekable)
        if peekable.has_next():
            next_item = peekable.peek()
            print(f"  Current: {current}, Next will be: {next_item}")
        else:
            print(f"  Current: {current}, No more items")


# ============================================================================
# PRACTICAL ITERATOR APPLICATIONS
# ============================================================================

class FileLineIterator:
    """Iterator for processing file lines with additional features"""
    
    def __init__(self, filename, strip_whitespace=True, skip_empty=True):
        """Initialize file iterator with options"""
        self.filename = filename
        self.strip_whitespace = strip_whitespace
        self.skip_empty = skip_empty
        self.line_number = 0
        self.file = None
    
    def __iter__(self):
        """Open file and return iterator"""
        try:
            self.file = open(self.filename, 'r')
            return self
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not open file: {self.filename}")
    
    def __next__(self):
        """Return next valid line"""
        while True:
            line = self.file.readline()
            
            if not line:  # End of file
                self.file.close()
                raise StopIteration
            
            self.line_number += 1
            
            if self.strip_whitespace:
                line = line.strip()
            
            if self.skip_empty and not line:
                continue  # Skip empty lines
            
            return {
                'content': line,
                'line_number': self.line_number,
                'length': len(line)
            }
    
    def __enter__(self):
        """Context manager support"""
        return self.__iter__()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Clean up file handle"""
        if self.file:
            self.file.close()


class DataProcessor:
    """Demonstrate practical iterator usage"""
    
    @staticmethod
    def process_numbers(numbers, operations):
        """Apply operations to numbers using iterators"""
        # Start with numbers iterator
        result = iter(numbers)
        
        # Apply each operation
        for operation in operations:
            result = map(operation, result)
        
        return list(result)
    
    @staticmethod
    def batch_process(items, batch_size, processor):
        """Process items in batches"""
        batch_iter = ChunkedIterator(items, batch_size)
        
        results = []
        for batch in batch_iter:
            batch_result = processor(batch)
            results.append(batch_result)
        
        return results
    
    @staticmethod
    def pipeline_process(data, *processors):
        """Create processing pipeline with iterators"""
        result = data
        
        for processor in processors:
            if hasattr(processor, '__call__'):
                result = map(processor, result)
            else:
                result = processor(result)
        
        return result


def demonstrate_practical_applications():
    """Show practical iterator applications"""
    print("\n" + "=" * 60)
    print("🏭 PRACTICAL ITERATOR APPLICATIONS")
    print("=" * 60)
    
    # Data processing pipeline
    print(f"\n🔄 Data Processing Pipeline:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    operations = [
        lambda x: x * 2,     # Double
        lambda x: x + 1,     # Add 1
        lambda x: x ** 2     # Square
    ]
    
    result = DataProcessor.process_numbers(numbers, operations)
    print(f"  Original: {numbers}")
    print(f"  After pipeline: {result}")
    
    # Batch processing
    print(f"\n📦 Batch Processing:")
    items = list(range(1, 21))  # 1 to 20
    
    def sum_batch(batch):
        return sum(batch)
    
    batch_results = DataProcessor.batch_process(items, 5, sum_batch)
    print(f"  Items: {items}")
    print(f"  Batch sums (size 5): {batch_results}")
    
    # Complex pipeline
    print(f"\n🔧 Complex Pipeline:")
    data = range(1, 11)
    
    # Pipeline: filter evens -> square -> take first 3
    pipeline_result = list(
        DataProcessor.pipeline_process(
            data,
            lambda x: x % 2 == 0,  # This won't work as expected
        )
    )
    
    # Better approach
    evens = filter(lambda x: x % 2 == 0, data)
    squared = map(lambda x: x ** 2, evens)
    first_three = list(ChunkedIterator(list(squared), 3))[0]
    
    print(f"  Original: {list(data)}")
    print(f"  Evens squared (first 3): {first_three}")


# ============================================================================
# MAIN DEMONSTRATION FUNCTION
# ============================================================================

def main():
    """Run all iterator demonstrations"""
    print("🔄 ITERATOR EXAMPLES - CSC 242 Week 3")
    print("=" * 60)
    
    demonstrate_basic_iteration()
    demonstrate_custom_iterators()
    demonstrate_smart_list()
    demonstrate_generators()
    demonstrate_stateful_iterators()
    demonstrate_practical_applications()
    
    print(f"\n" + "=" * 60)
    print("✅ All iterator demonstrations complete!")
    
    print(f"\n💡 Key Iterator Concepts:")
    print(f"   1. __iter__() and __next__() protocol")
    print(f"   2. StopIteration exception handling")
    print(f"   3. Generator functions with yield")
    print(f"   4. Custom iterator classes for complex logic")
    print(f"   5. Stateful iteration with memory")
    print(f"   6. Practical applications in data processing")


if __name__ == "__main__":
    main()
