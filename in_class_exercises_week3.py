"""
In-Class Exercises - Week 3
CSC 242 - Object-Oriented Programming

Interactive exercises for 180-minute class period covering:
- Iterator protocol implementation
- Custom exception design
- Advanced container ADTs
- Queue vs Stack trade-offs
- Performance analysis

Author: CSC 242 Teaching Team
"""


# ============================================================================
# EXERCISE 1: CUSTOM ITERATOR IMPLEMENTATION (35 minutes)
# ============================================================================

print("🔄 EXERCISE 1: Custom Iterator Implementation")
print("=" * 60)
print("Goal: Create iterators with different traversal patterns")
print()

class NumberSequence:
    """Container for a sequence of numbers with custom iteration patterns"""
    
    def __init__(self, numbers):
        """Initialize with list of numbers"""
        # TODO: Store the numbers
        pass
    
    def __iter__(self):
        """Default forward iteration"""
        # TODO: Return iterator over numbers in forward order
        pass
    
    def __len__(self):
        """Return length of sequence"""
        # TODO: Implement length
        pass
    
    def __getitem__(self, index):
        """Support indexing"""
        # TODO: Return item at index
        pass
    
    def reverse_iter(self):
        """Return reverse iterator"""
        # TODO: Return ReverseIterator instance
        pass
    
    def filter_iter(self, predicate):
        """Return filtered iterator"""
        # TODO: Return FilteredIterator instance
        pass
    
    def skip_iter(self, n):
        """Return iterator that skips every n items"""
        # TODO: Return SkipIterator instance
        pass


class ReverseIterator:
    """Iterator that traverses sequence in reverse order"""
    
    def __init__(self, sequence):
        """Initialize with sequence to iterate"""
        # TODO: Store sequence and set starting index
        pass
    
    def __iter__(self):
        """Return self as iterator"""
        # TODO: Return self
        pass
    
    def __next__(self):
        """Return next item in reverse order"""
        # TODO: Implement reverse iteration logic
        # Remember to raise StopIteration when done
        pass


class FilteredIterator:
    """Iterator that only returns items matching a predicate"""
    
    def __init__(self, sequence, predicate):
        """Initialize with sequence and filter function"""
        # TODO: Store sequence, predicate, and index
        pass
    
    def __iter__(self):
        """Return self as iterator"""
        # TODO: Return self
        pass
    
    def __next__(self):
        """Return next item that matches predicate"""
        # TODO: Find and return next matching item
        # Skip items that don't match predicate
        # Raise StopIteration when no more items
        pass


class SkipIterator:
    """Iterator that skips every n items"""
    
    def __init__(self, sequence, skip_count):
        """Initialize with sequence and skip count"""
        # TODO: Store sequence, skip count, and index
        pass
    
    def __iter__(self):
        """Return self as iterator"""
        # TODO: Return self
        pass
    
    def __next__(self):
        """Return next item, skipping n items each time"""
        # TODO: Implement skip logic
        # Advance index by skip_count + 1 each iteration
        pass


# Exercise 1 Instructions:
print("""
EXERCISE 1 TASKS:
1. Complete NumberSequence class:
   - Store numbers in __init__
   - Implement __iter__, __len__, __getitem__
   - Create methods that return custom iterators

2. Complete ReverseIterator:
   - Initialize with sequence and ending index
   - Implement __next__ to iterate backwards
   - Raise StopIteration when reaching beginning

3. Complete FilteredIterator:
   - Skip items that don't match predicate
   - Only return items where predicate(item) is True
   - Handle end of sequence properly

4. Complete SkipIterator:
   - Start at index 0, then skip n items each time
   - Example: skip_count=2 returns indices 0, 3, 6, 9...

5. Test your implementation:
""")

def test_iterators():
    """Test the iterator implementations"""
    print("\n🧪 Testing Custom Iterators:")
    
    try:
        # Create test sequence
        numbers = NumberSequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        
        # Test forward iteration
        print("  Forward iteration:")
        for num in numbers:
            print(f"    {num}")
        
        # Test reverse iteration
        print("  Reverse iteration:")
        for num in numbers.reverse_iter():
            print(f"    {num}")
        
        # Test filtered iteration (even numbers)
        print("  Even numbers only:")
        for num in numbers.filter_iter(lambda x: x % 2 == 0):
            print(f"    {num}")
        
        # Test skip iteration (every 3rd item)
        print("  Every 3rd item:")
        for num in numbers.skip_iter(2):
            print(f"    {num}")
        
        print("✅ All iterator tests passed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("   Complete the implementation above!")

# Uncomment when ready to test:
# test_iterators()


# ============================================================================
# EXERCISE 2: CUSTOM EXCEPTION HIERARCHY (30 minutes)
# ============================================================================

print("\n" + "=" * 60)
print("🔷 EXERCISE 2: Custom Exception Hierarchy")
print("=" * 60)
print("Goal: Design a comprehensive exception system for a banking application")
print()

class BankingError(Exception):
    """Base exception for all banking operations"""
    
    def __init__(self, message, error_code=None, account_id=None):
        """Initialize banking error with details"""
        # TODO: Call parent constructor with message
        # TODO: Store error_code and account_id
        # TODO: Add timestamp
        pass
    
    def get_error_details(self):
        """Return dictionary of error details"""
        # TODO: Return dict with all error information
        pass
    
    def __str__(self):
        """Enhanced string representation"""
        # TODO: Return formatted error message with code and account
        pass


class InsufficientFundsError(BankingError):
    """Raised when account doesn't have enough funds"""
    
    def __init__(self, account_id, requested_amount, available_balance):
        """Initialize with specific fund information"""
        # TODO: Create appropriate error message
        # TODO: Call parent constructor
        # TODO: Store amounts for reference
        pass
    
    def get_shortfall(self):
        """Return how much money is missing"""
        # TODO: Calculate and return shortfall amount
        pass


class AccountNotFoundError(BankingError):
    """Raised when account doesn't exist"""
    
    def __init__(self, account_id):
        """Initialize with account information"""
        # TODO: Create message about missing account
        # TODO: Call parent constructor with appropriate error code
        pass


class InvalidTransactionError(BankingError):
    """Raised for invalid transaction attempts"""
    
    def __init__(self, transaction_type, reason, account_id=None):
        """Initialize with transaction details"""
        # TODO: Create message about invalid transaction
        # TODO: Store transaction_type and reason
        pass


class AccountFrozenError(BankingError):
    """Raised when trying to access frozen account"""
    
    def __init__(self, account_id, freeze_reason=None):
        """Initialize with freeze information"""
        # TODO: Create message about frozen account
        # TODO: Store freeze_reason
        pass


class BankAccount:
    """Simple bank account with exception handling"""
    
    def __init__(self, account_id, initial_balance=0.0, is_frozen=False):
        """Initialize bank account"""
        # TODO: Store account details
        # TODO: Validate initial_balance is not negative
        pass
    
    def deposit(self, amount):
        """Deposit money to account"""
        # TODO: Validate account is not frozen
        # TODO: Validate amount is positive
        # TODO: Add amount to balance
        pass
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        # TODO: Validate account is not frozen
        # TODO: Validate amount is positive
        # TODO: Check sufficient funds
        # TODO: Subtract amount from balance
        pass
    
    def get_balance(self):
        """Get current balance"""
        # TODO: Check if account is frozen
        # TODO: Return current balance
        pass
    
    def freeze_account(self, reason="Security measure"):
        """Freeze the account"""
        # TODO: Set frozen status and reason
        pass
    
    def unfreeze_account(self):
        """Unfreeze the account"""
        # TODO: Clear frozen status and reason
        pass
    
    def __str__(self):
        """String representation"""
        # TODO: Return account information
        pass


class Bank:
    """Bank system that manages multiple accounts"""
    
    def __init__(self, name):
        """Initialize bank"""
        # TODO: Store bank name and create accounts dictionary
        pass
    
    def create_account(self, account_id, initial_balance=0.0):
        """Create new account"""
        # TODO: Check if account already exists
        # TODO: Create new BankAccount
        # TODO: Store in accounts dictionary
        pass
    
    def get_account(self, account_id):
        """Get account by ID"""
        # TODO: Check if account exists
        # TODO: Return account or raise AccountNotFoundError
        pass
    
    def transfer(self, from_account_id, to_account_id, amount):
        """Transfer money between accounts"""
        # TODO: Get both accounts (handle not found)
        # TODO: Perform withdrawal from source
        # TODO: Perform deposit to destination
        # TODO: Handle any exceptions appropriately
        pass


# Exercise 2 Instructions:
print("""
EXERCISE 2 TASKS:
1. Complete BankingError base class:
   - Store error details (code, account_id, timestamp)
   - Implement enhanced __str__ method
   - Add get_error_details() method

2. Complete specific exception classes:
   - InsufficientFundsError: Store amounts, implement get_shortfall()
   - AccountNotFoundError: Handle missing accounts
   - InvalidTransactionError: Store transaction details
   - AccountFrozenError: Handle frozen account access

3. Complete BankAccount class:
   - Implement deposit/withdraw with proper validation
   - Raise appropriate exceptions for each error condition
   - Handle frozen account state

4. Complete Bank class:
   - Manage multiple accounts
   - Implement transfer with proper exception handling
   - Handle account creation and retrieval

5. Test your exception system:
""")

def test_banking_exceptions():
    """Test the banking exception system"""
    print("\n🧪 Testing Banking Exception System:")
    
    try:
        # Create bank and accounts
        bank = Bank("Test Bank")
        bank.create_account("ACC001", 1000.0)
        bank.create_account("ACC002", 500.0)
        
        # Test normal operations
        account1 = bank.get_account("ACC001")
        account1.deposit(200.0)
        print(f"  ✓ Deposited successfully: {account1}")
        
        # Test insufficient funds
        try:
            account1.withdraw(2000.0)
        except InsufficientFundsError as e:
            print(f"  ✓ Caught InsufficientFundsError: {e}")
            print(f"    Shortfall: ${e.get_shortfall():.2f}")
        
        # Test account not found
        try:
            bank.get_account("NONEXISTENT")
        except AccountNotFoundError as e:
            print(f"  ✓ Caught AccountNotFoundError: {e}")
        
        # Test frozen account
        account1.freeze_account("Suspicious activity")
        try:
            account1.withdraw(100.0)
        except AccountFrozenError as e:
            print(f"  ✓ Caught AccountFrozenError: {e}")
        
        print("✅ All exception tests passed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("   Complete the implementation above!")

# Uncomment when ready to test:
# test_banking_exceptions()


# ============================================================================
# EXERCISE 3: QUEUE VS STACK APPLICATIONS (40 minutes)
# ============================================================================

print("\n" + "=" * 60)
print("🔷 EXERCISE 3: Queue vs Stack Applications")
print("=" * 60)
print("Goal: Implement practical applications using appropriate data structures")
print()

class TaskScheduler:
    """Task scheduling system using queues"""
    
    def __init__(self):
        """Initialize scheduler with different priority queues"""
        # TODO: Create separate queues for different priorities
        # high_priority, medium_priority, low_priority
        pass
    
    def add_task(self, task_name, priority="medium"):
        """Add task with specified priority"""
        # TODO: Add task to appropriate priority queue
        # TODO: Validate priority is valid
        pass
    
    def get_next_task(self):
        """Get next task to process (highest priority first)"""
        # TODO: Check high priority queue first
        # TODO: Then medium, then low priority
        # TODO: Return None if no tasks
        pass
    
    def get_task_count(self):
        """Return count of tasks by priority"""
        # TODO: Return dictionary with counts for each priority
        pass
    
    def list_pending_tasks(self):
        """List all pending tasks in priority order"""
        # TODO: Return list of all tasks in processing order
        pass


class UndoRedoSystem:
    """Undo/Redo system using stacks"""
    
    def __init__(self):
        """Initialize with undo and redo stacks"""
        # TODO: Create undo_stack and redo_stack
        pass
    
    def execute_command(self, command_name, data):
        """Execute command and add to undo stack"""
        # TODO: Create command dictionary with name and data
        # TODO: Add to undo stack
        # TODO: Clear redo stack (new action invalidates redo)
        pass
    
    def undo(self):
        """Undo last command"""
        # TODO: Pop from undo stack
        # TODO: Push to redo stack
        # TODO: Return command that was undone
        pass
    
    def redo(self):
        """Redo last undone command"""
        # TODO: Pop from redo stack
        # TODO: Push to undo stack
        # TODO: Return command that was redone
        pass
    
    def can_undo(self):
        """Check if undo is possible"""
        # TODO: Return True if undo stack has items
        pass
    
    def can_redo(self):
        """Check if redo is possible"""
        # TODO: Return True if redo stack has items
        pass
    
    def get_command_history(self):
        """Return current command history"""
        # TODO: Return info about undo/redo stacks
        pass


class BrowserHistory:
    """Web browser history using stack and queue concepts"""
    
    def __init__(self):
        """Initialize browser history"""
        # TODO: Create history stack for back button
        # TODO: Create forward stack for forward button
        # TODO: Set current_page to None
        pass
    
    def visit_page(self, url):
        """Visit a new page"""
        # TODO: Add current page to history if exists
        # TODO: Set new current page
        # TODO: Clear forward stack (new navigation invalidates forward)
        pass
    
    def go_back(self):
        """Go back to previous page"""
        # TODO: Move current page to forward stack
        # TODO: Pop from history stack to get previous page
        # TODO: Return URL of page we went back to
        pass
    
    def go_forward(self):
        """Go forward to next page"""
        # TODO: Move current page to history stack
        # TODO: Pop from forward stack to get next page
        # TODO: Return URL of page we went forward to
        pass
    
    def get_current_page(self):
        """Get current page URL"""
        # TODO: Return current_page
        pass
    
    def can_go_back(self):
        """Check if back navigation is possible"""
        # TODO: Return True if history stack has items
        pass
    
    def can_go_forward(self):
        """Check if forward navigation is possible"""
        # TODO: Return True if forward stack has items
        pass
    
    def get_history_info(self):
        """Return history information"""
        # TODO: Return info about current page and navigation options
        pass


class PrintJobQueue:
    """Print job management system"""
    
    def __init__(self):
        """Initialize print queue"""
        # TODO: Create job queue
        # TODO: Initialize job counter for unique IDs
        pass
    
    def submit_job(self, document_name, pages, priority="normal"):
        """Submit print job"""
        # TODO: Create job dictionary with id, document, pages, priority
        # TODO: Add to appropriate position in queue based on priority
        pass
    
    def process_next_job(self):
        """Process next print job"""
        # TODO: Remove and return next job from queue
        # TODO: Handle empty queue
        pass
    
    def cancel_job(self, job_id):
        """Cancel specific print job"""
        # TODO: Find and remove job with specified ID
        # TODO: Return True if found and cancelled, False otherwise
        pass
    
    def get_queue_status(self):
        """Get current queue status"""
        # TODO: Return info about pending jobs
        pass
    
    def estimate_wait_time(self, job_id):
        """Estimate wait time for specific job"""
        # TODO: Find job position and estimate time based on jobs ahead
        pass


# Exercise 3 Instructions:
print("""
EXERCISE 3 TASKS:
1. Complete TaskScheduler class:
   - Use separate queues for different priorities
   - Process high priority tasks first
   - Implement proper task management

2. Complete UndoRedoSystem class:
   - Use stack for undo operations
   - Use stack for redo operations
   - Handle command execution and reversal

3. Complete BrowserHistory class:
   - Use stack for back navigation
   - Use stack for forward navigation
   - Handle page visits and navigation

4. Complete PrintJobQueue class:
   - Use queue for FIFO job processing
   - Handle priority jobs appropriately
   - Implement job cancellation

5. Test your implementations:
""")

def test_data_structure_applications():
    """Test the practical applications"""
    print("\n🧪 Testing Data Structure Applications:")
    
    try:
        # Test Task Scheduler
        print("  📋 Testing TaskScheduler:")
        scheduler = TaskScheduler()
        scheduler.add_task("Backup database", "high")
        scheduler.add_task("Update documentation", "low")
        scheduler.add_task("Fix bug #123", "medium")
        
        task = scheduler.get_next_task()
        print(f"    Next task: {task}")
        
        # Test Undo/Redo System
        print("  🔄 Testing UndoRedoSystem:")
        undo_redo = UndoRedoSystem()
        undo_redo.execute_command("type", "Hello")
        undo_redo.execute_command("type", " World")
        
        undone = undo_redo.undo()
        print(f"    Undone: {undone}")
        
        redone = undo_redo.redo()
        print(f"    Redone: {redone}")
        
        # Test Browser History
        print("  🌐 Testing BrowserHistory:")
        browser = BrowserHistory()
        browser.visit_page("google.com")
        browser.visit_page("github.com")
        browser.visit_page("stackoverflow.com")
        
        back_page = browser.go_back()
        print(f"    Went back to: {back_page}")
        
        # Test Print Queue
        print("  🖨️ Testing PrintJobQueue:")
        print_queue = PrintJobQueue()
        print_queue.submit_job("document1.pdf", 5)
        print_queue.submit_job("urgent_report.docx", 10, "high")
        
        job = print_queue.process_next_job()
        print(f"    Processing job: {job}")
        
        print("✅ All application tests passed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("   Complete the implementation above!")

# Uncomment when ready to test:
# test_data_structure_applications()


# ============================================================================
# EXERCISE 4: PERFORMANCE ANALYSIS (30 minutes)
# ============================================================================

print("\n" + "=" * 60)
print("🔷 EXERCISE 4: Container Performance Analysis")
print("=" * 60)
print("Goal: Analyze and compare container performance characteristics")
print()

import time
from collections import deque

class PerformanceAnalyzer:
    """Tool for analyzing container performance"""
    
    def __init__(self):
        """Initialize performance analyzer"""
        self.results = {}
    
    def time_operation(self, operation_func, num_iterations=1000):
        """Time how long an operation takes"""
        # TODO: Record start time
        # TODO: Execute operation num_iterations times
        # TODO: Record end time
        # TODO: Return total time
        pass
    
    def test_queue_implementations(self, num_operations=1000):
        """Compare different queue implementations"""
        # TODO: Test different queue types:
        # - List-based queue (append/pop(0))
        # - Deque (append/popleft)
        # - Your custom implementations
        
        implementations = {
            'list_queue': self._test_list_queue,
            'deque_queue': self._test_deque_queue,
            'reverse_list_queue': self._test_reverse_list_queue
        }
        
        results = {}
        for name, test_func in implementations.items():
            # TODO: Time the test function
            # TODO: Store results
            pass
        
        return results
    
    def _test_list_queue(self, num_ops):
        """Test list-based queue performance"""
        # TODO: Create list
        # TODO: Perform enqueue operations (append)
        # TODO: Perform dequeue operations (pop(0))
        pass
    
    def _test_deque_queue(self, num_ops):
        """Test deque-based queue performance"""
        # TODO: Create deque
        # TODO: Perform enqueue operations (append)
        # TODO: Perform dequeue operations (popleft)
        pass
    
    def _test_reverse_list_queue(self, num_ops):
        """Test reverse list queue performance"""
        # TODO: Create list
        # TODO: Perform enqueue operations (insert(0))
        # TODO: Perform dequeue operations (pop())
        pass
    
    def analyze_memory_usage(self, container, num_items=10000):
        """Analyze memory usage of container"""
        import sys
        
        # TODO: Measure memory before adding items
        # TODO: Add items to container
        # TODO: Measure memory after adding items
        # TODO: Calculate memory per item
        pass
    
    def test_scaling_behavior(self, container_class, sizes=[100, 500, 1000, 5000]):
        """Test how performance scales with size"""
        results = {}
        
        for size in sizes:
            # TODO: Create container instance
            # TODO: Time operations for this size
            # TODO: Store timing results
            pass
        
        return results
    
    def generate_report(self):
        """Generate performance analysis report"""
        # TODO: Create formatted report of all test results
        # TODO: Include recommendations
        pass


class CustomQueue:
    """Your custom queue implementation for testing"""
    
    def __init__(self):
        # TODO: Implement your queue
        pass
    
    def enqueue(self, item):
        # TODO: Add item to queue
        pass
    
    def dequeue(self):
        # TODO: Remove and return item from queue
        pass
    
    def is_empty(self):
        # TODO: Check if queue is empty
        pass


class CustomStack:
    """Your custom stack implementation for testing"""
    
    def __init__(self):
        # TODO: Implement your stack
        pass
    
    def push(self, item):
        # TODO: Add item to stack
        pass
    
    def pop(self):
        # TODO: Remove and return item from stack
        pass
    
    def is_empty(self):
        # TODO: Check if stack is empty
        pass


# Exercise 4 Instructions:
print("""
EXERCISE 4 TASKS:
1. Complete PerformanceAnalyzer class:
   - Implement time_operation() method
   - Create queue performance tests
   - Implement memory usage analysis
   - Test scaling behavior

2. Complete the three test methods:
   - _test_list_queue(): Use list with append/pop(0)
   - _test_deque_queue(): Use deque with append/popleft
   - _test_reverse_list_queue(): Use list with insert(0)/pop()

3. Complete CustomQueue and CustomStack:
   - Implement your own efficient versions
   - Focus on performance optimization

4. Analyze performance characteristics:
   - Compare time complexity
   - Measure actual execution times
   - Test memory usage
   - Identify performance bottlenecks

5. Run performance comparison:
""")

def run_performance_tests():
    """Run comprehensive performance tests"""
    print("\n🧪 Running Performance Tests:")
    
    try:
        analyzer = PerformanceAnalyzer()
        
        # Test queue implementations
        print("  ⚡ Testing Queue Implementations:")
        queue_results = analyzer.test_queue_implementations(1000)
        
        for name, time_taken in queue_results.items():
            print(f"    {name}: {time_taken:.4f} seconds")
        
        # Find fastest implementation
        if queue_results:
            fastest = min(queue_results.items(), key=lambda x: x[1])
            slowest = max(queue_results.items(), key=lambda x: x[1])
            print(f"    Fastest: {fastest[0]} ({fastest[1]:.4f}s)")
            print(f"    Slowest: {slowest[0]} ({slowest[1]:.4f}s)")
            print(f"    Speed difference: {slowest[1]/fastest[1]:.1f}x")
        
        # Test scaling behavior
        print("  📈 Testing Scaling Behavior:")
        scaling_results = analyzer.test_scaling_behavior(CustomQueue)
        
        for size, time_taken in scaling_results.items():
            print(f"    Size {size}: {time_taken:.4f} seconds")
        
        print("✅ Performance tests completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("   Complete the implementation above!")

# Uncomment when ready to test:
# run_performance_tests()


# ============================================================================
# BONUS EXERCISE: ITERATOR DESIGN PATTERNS (25 minutes)
# ============================================================================

print("\n" + "=" * 60)
print("🔷 BONUS EXERCISE: Advanced Iterator Patterns")
print("=" * 60)
print("Goal: Implement sophisticated iterator design patterns")
print()

class ChainIterator:
    """Iterator that chains multiple iterables together"""
    
    def __init__(self, *iterables):
        """Initialize with multiple iterables"""
        # TODO: Store iterables
        # TODO: Initialize current iterable index and iterator
        pass
    
    def __iter__(self):
        """Return self as iterator"""
        # TODO: Return self
        pass
    
    def __next__(self):
        """Return next item from current iterable, advance to next when exhausted"""
        # TODO: Try to get next item from current iterator
        # TODO: If StopIteration, move to next iterable
        # TODO: Raise StopIteration when all iterables exhausted
        pass


class CycleIterator:
    """Iterator that cycles through an iterable infinitely"""
    
    def __init__(self, iterable, max_cycles=None):
        """Initialize with iterable and optional cycle limit"""
        # TODO: Store iterable and cycle information
        pass
    
    def __iter__(self):
        return self
    
    def __next__(self):
        """Return next item, cycling back to beginning when needed"""
        # TODO: Implement cycling logic
        # TODO: Handle max_cycles limit
        pass


class WindowIterator:
    """Iterator that returns sliding windows of items"""
    
    def __init__(self, iterable, window_size):
        """Initialize with iterable and window size"""
        # TODO: Store iterable and window size
        # TODO: Initialize data structures for windowing
        pass
    
    def __iter__(self):
        return self
    
    def __next__(self):
        """Return next window of items"""
        # TODO: Return tuple of window_size items
        # TODO: Slide window by one position each iteration
        pass


def demonstrate_advanced_iterators():
    """Show advanced iterator patterns in action"""
    print("\n🧪 Testing Advanced Iterator Patterns:")
    
    try:
        # Test ChainIterator
        print("  🔗 Chain Iterator:")
        chained = ChainIterator([1, 2, 3], ['a', 'b'], [10, 20])
        for item in chained:
            print(f"    {item}")
        
        # Test CycleIterator (limited cycles)
        print("  🔄 Cycle Iterator (2 cycles):")
        cycled = CycleIterator(['X', 'Y', 'Z'], max_cycles=2)
        for i, item in enumerate(cycled):
            if i >= 10:  # Safety limit
                break
            print(f"    {item}")
        
        # Test WindowIterator
        print("  🪟 Window Iterator (size 3):")
        windowed = WindowIterator([1, 2, 3, 4, 5, 6, 7], 3)
        for window in windowed:
            print(f"    {window}")
        
        print("✅ Advanced iterator tests passed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("   Complete the implementation above!")

# Uncomment when ready to test:
# demonstrate_advanced_iterators()


# ============================================================================
# EXERCISE WRAP-UP
# ============================================================================

print("\n" + "=" * 60)
print("📝 EXERCISE WRAP-UP")
print("=" * 60)

print("""
🎯 LEARNING OBJECTIVES COVERED:

1. Iterator Protocol:
   - Custom iterator classes with __iter__ and __next__
   - Different traversal patterns (forward, reverse, filtered)
   - State management in iterators

2. Exception Design:
   - Custom exception hierarchies
   - Meaningful error messages and context
   - Exception chaining and debugging

3. Container ADTs:
   - Queue vs Stack usage patterns
   - Performance trade-offs
   - Real-world applications

4. Performance Analysis:
   - Time complexity measurement
   - Memory usage analysis
   - Scaling behavior testing

💡 KEY INSIGHTS:
- Choose the right data structure for your problem
- Iterator patterns provide flexible data access
- Custom exceptions improve debugging experience
- Performance testing reveals hidden bottlenecks

🔄 FOR 180-MINUTE CLASS:
- Work through exercises progressively
- Compare solutions with classmates
- Discuss design trade-offs
- Experiment with optimizations
""")

def main():
    """Main function to run all exercises"""
    print("🚀 Starting Week 3 In-Class Exercises")
    print("=" * 60)
    
    print("📋 EXERCISE CHECKLIST:")
    print("□ Exercise 1: Custom Iterators (35 min)")
    print("□ Exercise 2: Exception Hierarchy (30 min)")
    print("□ Exercise 3: Queue vs Stack Apps (40 min)")
    print("□ Exercise 4: Performance Analysis (30 min)")
    print("□ Bonus: Advanced Iterator Patterns (25 min)")
    
    print("\n💻 INSTRUCTIONS:")
    print("1. Work through exercises in order")
    print("2. Uncomment test functions when ready")
    print("3. Focus on understanding trade-offs")
    print("4. Experiment with different approaches")
    
    print("\n✨ Good luck with the exercises!")


if __name__ == "__main__":
    main()
