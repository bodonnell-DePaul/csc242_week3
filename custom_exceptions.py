"""
Custom Exceptions - Week 3
CSC 242 - Object-Oriented Programming

This file demonstrates comprehensive exception handling:
- Built-in exception review
- Custom exception classes
- Exception hierarchies
- Exception chaining and context
- Best practices for exception design

Author: CSC 242 Teaching Team
"""

import sys
import traceback
from datetime import datetime


# ============================================================================
# BUILT-IN EXCEPTIONS REVIEW
# ============================================================================

print("⚠️ EXCEPTION HANDLING FUNDAMENTALS")
print("=" * 60)

def demonstrate_builtin_exceptions():
    """Review common built-in exceptions"""
    print("\n📋 Built-in Exception Examples:")
    
    # Common exceptions with examples
    exceptions_demo = [
        ("ValueError", lambda: int("not_a_number")),
        ("TypeError", lambda: "string" + 5),
        ("IndexError", lambda: [1, 2, 3][10]),
        ("KeyError", lambda: {"a": 1}["b"]),
        ("AttributeError", lambda: "string".nonexistent_method()),
        ("ZeroDivisionError", lambda: 10 / 0),
        ("FileNotFoundError", lambda: open("nonexistent_file.txt")),
    ]
    
    for exc_name, operation in exceptions_demo:
        try:
            print(f"\n  Testing {exc_name}:")
            result = operation()
            print(f"    Unexpected success: {result}")
        except Exception as e:
            print(f"    ✓ Caught {type(e).__name__}: {e}")


def demonstrate_exception_handling_patterns():
    """Show different exception handling patterns"""
    print("\n🔧 Exception Handling Patterns:")
    
    # Multiple specific exceptions
    def handle_multiple_exceptions():
        try:
            choice = input("Enter 1 for ValueError, 2 for ZeroDivisionError: ")
            if choice == "1":
                int("not_a_number")
            elif choice == "2":
                10 / 0
            else:
                raise KeyError("Invalid choice")
        except ValueError as e:
            print(f"    ValueError handled: {e}")
        except ZeroDivisionError as e:
            print(f"    ZeroDivisionError handled: {e}")
        except KeyError as e:
            print(f"    KeyError handled: {e}")
        except Exception as e:
            print(f"    Unexpected error: {e}")
    
    # Exception with finally
    def demonstrate_finally():
        resource = None
        try:
            print("    Opening resource...")
            resource = "Important Resource"
            # Simulate operation that might fail
            if True:  # Change to test different paths
                result = 10 / 2
                print(f"    Operation successful: {result}")
        except ZeroDivisionError as e:
            print(f"    Error during operation: {e}")
        finally:
            if resource:
                print(f"    Cleaning up: {resource}")
                resource = None
    
    # Exception chaining
    def demonstrate_chaining():
        try:
            try:
                int("invalid")
            except ValueError as original_error:
                raise RuntimeError("Processing failed") from original_error
        except RuntimeError as e:
            print(f"    Main error: {e}")
            print(f"    Caused by: {e.__cause__}")
    
    print(f"\n  🎯 Multiple Exception Handling:")
    # handle_multiple_exceptions()  # Commented out to avoid input in demo
    
    print(f"\n  🧹 Finally Block:")
    demonstrate_finally()
    
    print(f"\n  🔗 Exception Chaining:")
    demonstrate_chaining()


# ============================================================================
# CUSTOM EXCEPTION CLASSES
# ============================================================================

class DataStructureError(Exception):
    """Base exception for all data structure errors"""
    
    def __init__(self, message, error_code=None, timestamp=None):
        """Initialize with message and optional metadata"""
        super().__init__(message)
        self.error_code = error_code
        self.timestamp = timestamp or datetime.now()
        self.context = {}
    
    def add_context(self, key, value):
        """Add context information to the exception"""
        self.context[key] = value
        return self
    
    def __str__(self):
        """Enhanced string representation"""
        base_msg = super().__str__()
        if self.error_code:
            base_msg = f"[{self.error_code}] {base_msg}"
        if self.context:
            context_str = ", ".join(f"{k}={v}" for k, v in self.context.items())
            base_msg = f"{base_msg} (Context: {context_str})"
        return base_msg


class EmptyContainerError(DataStructureError):
    """Raised when operating on empty containers"""
    
    def __init__(self, container_type, operation):
        """Initialize with container type and operation"""
        message = f"Cannot {operation} from empty {container_type}"
        super().__init__(message, error_code="EMPTY_CONTAINER")
        self.container_type = container_type
        self.operation = operation


class FullContainerError(DataStructureError):
    """Raised when adding to full containers"""
    
    def __init__(self, container_type, capacity, operation="add"):
        """Initialize with container info"""
        message = f"Cannot {operation} to full {container_type} (capacity: {capacity})"
        super().__init__(message, error_code="FULL_CONTAINER")
        self.container_type = container_type
        self.capacity = capacity
        self.operation = operation


class InvalidIndexError(DataStructureError):
    """Raised for invalid index operations"""
    
    def __init__(self, index, container_size, container_type="container"):
        """Initialize with index information"""
        message = f"Invalid index {index} for {container_type} of size {container_size}"
        super().__init__(message, error_code="INVALID_INDEX")
        self.index = index
        self.container_size = container_size
        self.container_type = container_type


class ConfigurationError(DataStructureError):
    """Raised for invalid configuration"""
    
    def __init__(self, parameter, value, expected=None):
        """Initialize with configuration details"""
        message = f"Invalid configuration: {parameter}={value}"
        if expected:
            message += f" (expected: {expected})"
        super().__init__(message, error_code="INVALID_CONFIG")
        self.parameter = parameter
        self.value = value
        self.expected = expected


# ============================================================================
# APPLICATION-SPECIFIC EXCEPTIONS
# ============================================================================

class QueueError(DataStructureError):
    """Base exception for queue operations"""
    pass


class EmptyQueueError(QueueError, EmptyContainerError):
    """Raised when dequeuing from empty queue"""
    
    def __init__(self, operation="dequeue"):
        EmptyContainerError.__init__(self, "queue", operation)


class FullQueueError(QueueError, FullContainerError):
    """Raised when enqueueing to full queue"""
    
    def __init__(self, capacity, operation="enqueue"):
        FullContainerError.__init__(self, "queue", capacity, operation)


class StackError(DataStructureError):
    """Base exception for stack operations"""
    pass


class EmptyStackError(StackError, EmptyContainerError):
    """Raised when popping from empty stack"""
    
    def __init__(self, operation="pop"):
        EmptyContainerError.__init__(self, "stack", operation)


class StackOverflowError(StackError, FullContainerError):
    """Raised when pushing to full stack"""
    
    def __init__(self, capacity, operation="push"):
        FullContainerError.__init__(self, "stack", capacity, operation)


# ============================================================================
# CONTAINER CLASSES WITH CUSTOM EXCEPTIONS
# ============================================================================

class SafeQueue:
    """Queue implementation with comprehensive exception handling"""
    
    def __init__(self, max_size=None):
        """Initialize queue with optional capacity limit"""
        if max_size is not None and max_size <= 0:
            raise ConfigurationError("max_size", max_size, "positive integer or None")
        
        self._items = []
        self._max_size = max_size
    
    def enqueue(self, item):
        """Add item to rear of queue"""
        if self._max_size and len(self._items) >= self._max_size:
            exc = FullQueueError(self._max_size)
            exc.add_context("current_size", len(self._items))
            exc.add_context("attempted_item", repr(item))
            raise exc
        
        self._items.append(item)
    
    def dequeue(self):
        """Remove and return item from front of queue"""
        if not self._items:
            exc = EmptyQueueError()
            exc.add_context("queue_type", "SafeQueue")
            exc.add_context("capacity", self._max_size)
            raise exc
        
        return self._items.pop(0)
    
    def front(self):
        """Return front item without removing it"""
        if not self._items:
            raise EmptyQueueError("peek at front")
        return self._items[0]
    
    def size(self):
        """Return current size"""
        return len(self._items)
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self._items) == 0
    
    def is_full(self):
        """Check if queue is full"""
        return self._max_size and len(self._items) >= self._max_size
    
    def capacity(self):
        """Return maximum capacity"""
        return self._max_size
    
    def __len__(self):
        return len(self._items)
    
    def __str__(self):
        size_info = f"size={len(self._items)}"
        if self._max_size:
            size_info += f"/{self._max_size}"
        
        if self.is_empty():
            return f"SafeQueue(empty, {size_info})"
        return f"SafeQueue(front={self.front()}, {size_info})"


class SafeStack:
    """Stack implementation with comprehensive exception handling"""
    
    def __init__(self, max_size=None):
        """Initialize stack with optional capacity limit"""
        if max_size is not None and max_size <= 0:
            raise ConfigurationError("max_size", max_size, "positive integer or None")
        
        self._items = []
        self._max_size = max_size
    
    def push(self, item):
        """Add item to top of stack"""
        if self._max_size and len(self._items) >= self._max_size:
            exc = StackOverflowError(self._max_size)
            exc.add_context("current_size", len(self._items))
            exc.add_context("attempted_item", repr(item))
            raise exc
        
        self._items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if not self._items:
            exc = EmptyStackError()
            exc.add_context("stack_type", "SafeStack")
            exc.add_context("capacity", self._max_size)
            raise exc
        
        return self._items.pop()
    
    def peek(self):
        """Return top item without removing it"""
        if not self._items:
            raise EmptyStackError("peek at top")
        return self._items[-1]
    
    def size(self):
        """Return current size"""
        return len(self._items)
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self._items) == 0
    
    def is_full(self):
        """Check if stack is full"""
        return self._max_size and len(self._items) >= self._max_size
    
    def __len__(self):
        return len(self._items)
    
    def __str__(self):
        size_info = f"size={len(self._items)}"
        if self._max_size:
            size_info += f"/{self._max_size}"
        
        if self.is_empty():
            return f"SafeStack(empty, {size_info})"
        return f"SafeStack(top={self.peek()}, {size_info})"


# ============================================================================
# EXCEPTION CONTEXT AND DEBUGGING
# ============================================================================

class DebuggingQueue(SafeQueue):
    """Queue with enhanced debugging capabilities"""
    
    def __init__(self, max_size=None, debug_mode=False):
        """Initialize with debugging options"""
        super().__init__(max_size)
        self.debug_mode = debug_mode
        self.operation_history = []
        self.error_history = []
    
    def _log_operation(self, operation, *args, **kwargs):
        """Log operation for debugging"""
        if self.debug_mode:
            entry = {
                'timestamp': datetime.now(),
                'operation': operation,
                'args': args,
                'kwargs': kwargs,
                'state_before': len(self._items)
            }
            self.operation_history.append(entry)
    
    def _log_error(self, error, operation, *args):
        """Log error for debugging"""
        error_entry = {
            'timestamp': datetime.now(),
            'error_type': type(error).__name__,
            'error_message': str(error),
            'operation': operation,
            'args': args,
            'queue_state': len(self._items)
        }
        self.error_history.append(error_entry)
    
    def enqueue(self, item):
        """Enqueue with debugging"""
        self._log_operation('enqueue', item)
        try:
            super().enqueue(item)
        except Exception as e:
            self._log_error(e, 'enqueue', item)
            raise
    
    def dequeue(self):
        """Dequeue with debugging"""
        self._log_operation('dequeue')
        try:
            return super().dequeue()
        except Exception as e:
            self._log_error(e, 'dequeue')
            raise
    
    def get_debug_info(self):
        """Return debugging information"""
        return {
            'operation_count': len(self.operation_history),
            'error_count': len(self.error_history),
            'recent_operations': self.operation_history[-5:],
            'recent_errors': self.error_history[-3:],
            'current_state': {
                'size': len(self._items),
                'capacity': self._max_size,
                'is_empty': self.is_empty(),
                'is_full': self.is_full()
            }
        }


# ============================================================================
# DEMONSTRATION FUNCTIONS
# ============================================================================

def demonstrate_custom_exceptions():
    """Show custom exception usage"""
    print("\n" + "=" * 60)
    print("🔧 CUSTOM EXCEPTION CLASSES")
    print("=" * 60)
    
    # Test SafeQueue exceptions
    print(f"\n📋 SafeQueue Exception Handling:")
    
    # Empty queue operations
    empty_queue = SafeQueue()
    print(f"  Created empty queue: {empty_queue}")
    
    try:
        empty_queue.dequeue()
    except EmptyQueueError as e:
        print(f"  ✓ Caught EmptyQueueError: {e}")
        print(f"    Error code: {e.error_code}")
        print(f"    Context: {e.context}")
    
    # Full queue operations
    full_queue = SafeQueue(max_size=2)
    full_queue.enqueue("item1")
    full_queue.enqueue("item2")
    print(f"  Created full queue: {full_queue}")
    
    try:
        full_queue.enqueue("item3")
    except FullQueueError as e:
        print(f"  ✓ Caught FullQueueError: {e}")
        print(f"    Error code: {e.error_code}")
        print(f"    Context: {e.context}")
    
    # Test SafeStack exceptions
    print(f"\n📚 SafeStack Exception Handling:")
    
    empty_stack = SafeStack(max_size=3)
    print(f"  Created empty stack: {empty_stack}")
    
    try:
        empty_stack.pop()
    except EmptyStackError as e:
        print(f"  ✓ Caught EmptyStackError: {e}")
    
    # Fill stack and test overflow
    full_stack = SafeStack(max_size=2)
    full_stack.push("A")
    full_stack.push("B")
    print(f"  Created full stack: {full_stack}")
    
    try:
        full_stack.push("C")
    except StackOverflowError as e:
        print(f"  ✓ Caught StackOverflowError: {e}")


def demonstrate_exception_hierarchy():
    """Show exception hierarchy and inheritance"""
    print(f"\n🌳 Exception Hierarchy:")
    
    # Show inheritance relationships
    exceptions = [
        EmptyQueueError(),
        FullQueueError(5),
        EmptyStackError(),
        StackOverflowError(10),
        InvalidIndexError(5, 3),
        ConfigurationError("max_size", -1, "positive integer")
    ]
    
    for exc in exceptions:
        print(f"  {type(exc).__name__}:")
        print(f"    MRO: {' -> '.join(cls.__name__ for cls in type(exc).__mro__[:-1])}")
        print(f"    Message: {exc}")
        print(f"    Is DataStructureError: {isinstance(exc, DataStructureError)}")
        print()


def demonstrate_debugging_features():
    """Show debugging and error tracking"""
    print(f"\n🐛 Debugging Features:")
    
    debug_queue = DebuggingQueue(max_size=3, debug_mode=True)
    print(f"  Created debugging queue: {debug_queue}")
    
    # Perform operations
    try:
        debug_queue.enqueue("A")
        debug_queue.enqueue("B")
        debug_queue.dequeue()
        debug_queue.enqueue("C")
        debug_queue.enqueue("D")
        debug_queue.enqueue("E")  # This should fail
    except FullQueueError:
        print(f"  Queue became full as expected")
    
    try:
        debug_queue.dequeue()
        debug_queue.dequeue()
        debug_queue.dequeue()  # This should fail
    except EmptyQueueError:
        print(f"  Queue became empty as expected")
    
    # Show debug information
    debug_info = debug_queue.get_debug_info()
    print(f"\n  Debug Information:")
    print(f"    Operations performed: {debug_info['operation_count']}")
    print(f"    Errors encountered: {debug_info['error_count']}")
    print(f"    Current state: {debug_info['current_state']}")
    
    if debug_info['recent_errors']:
        print(f"    Recent errors:")
        for error in debug_info['recent_errors']:
            print(f"      - {error['error_type']}: {error['error_message']}")


def demonstrate_exception_best_practices():
    """Show exception handling best practices"""
    print(f"\n✅ Exception Best Practices:")
    
    # Specific exception handling
    def process_queue_safely(queue, operations):
        """Process queue operations with proper exception handling"""
        results = []
        
        for operation, *args in operations:
            try:
                if operation == "enqueue":
                    queue.enqueue(args[0])
                    results.append(f"✓ Enqueued: {args[0]}")
                elif operation == "dequeue":
                    item = queue.dequeue()
                    results.append(f"✓ Dequeued: {item}")
                elif operation == "peek":
                    item = queue.front()
                    results.append(f"✓ Peeked: {item}")
            
            except EmptyQueueError as e:
                results.append(f"⚠ Empty queue error: {e}")
            except FullQueueError as e:
                results.append(f"⚠ Full queue error: {e}")
            except DataStructureError as e:
                results.append(f"❌ Data structure error: {e}")
            except Exception as e:
                results.append(f"💥 Unexpected error: {e}")
                # In real code, might want to log and re-raise
        
        return results
    
    # Test the safe processing
    test_queue = SafeQueue(max_size=2)
    operations = [
        ("enqueue", "A"),
        ("enqueue", "B"),
        ("enqueue", "C"),  # Should fail - full
        ("peek",),
        ("dequeue",),
        ("dequeue",),
        ("dequeue",),       # Should fail - empty
    ]
    
    results = process_queue_safely(test_queue, operations)
    
    print(f"\n  Safe Queue Processing Results:")
    for result in results:
        print(f"    {result}")


# ============================================================================
# MAIN DEMONSTRATION FUNCTION
# ============================================================================

def main():
    """Run all exception handling demonstrations"""
    print("⚠️ CUSTOM EXCEPTIONS - CSC 242 Week 3")
    print("=" * 60)
    
    demonstrate_builtin_exceptions()
    demonstrate_exception_handling_patterns()
    demonstrate_custom_exceptions()
    demonstrate_exception_hierarchy()
    demonstrate_debugging_features()
    demonstrate_exception_best_practices()
    
    print(f"\n" + "=" * 60)
    print("✅ All exception handling demonstrations complete!")
    
    print(f"\n💡 Key Exception Concepts:")
    print(f"   1. Custom exception classes with meaningful names")
    print(f"   2. Exception hierarchies for organized error handling")
    print(f"   3. Context information in exceptions")
    print(f"   4. Specific exception handling vs generic catches")
    print(f"   5. Exception chaining and debugging information")
    print(f"   6. Error recovery and graceful degradation")


if __name__ == "__main__":
    main()
