"""
Q1: Prime Number Checker with AI-Generated Test Cases

Objective:
Write a Python function `is_prime(n)` to check if a number is prime.
Use AI coding tool to generate and justify test cases before implementation.
Pass all generated test cases.

AI Integration:
- Used AI to generate comprehensive test cases covering edge cases
- Justified each test case category
- Implemented function to pass all test cases
"""

def is_prime(n):
    """
    Check if a number is prime.
    
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    
    Args:
        n (int): The number to check for primality
    
    Returns:
        bool: True if n is prime, False otherwise
    
    Raises:
        TypeError: If n is not an integer
    
    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(17)
        True
        >>> is_prime(1)
        False
        >>> is_prime(-5)
        False
        >>> is_prime(4)
        False
    """
    # Type validation
    if not isinstance(n, int):
        raise TypeError(f"Expected integer, got {type(n).__name__}")
    
    # Prime numbers are natural numbers greater than 1
    if n <= 1:
        return False
    
    # 2 is the only even prime number
    if n == 2:
        return True
    
    # All other even numbers are not prime
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    # If n has a divisor greater than sqrt(n), it must also have one smaller than sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True


# ============================================================================
# AI-GENERATED TEST CASES WITH JUSTIFICATION
# ============================================================================
# The following test cases were generated using AI and are organized by category.
# Each category tests a specific aspect of the prime-checking function.

TEST_CASES = {
    "boundary_cases": [
        # (input, expected_output, justification)
        (0, False, "0 is not prime (not > 1)"),
        (1, False, "1 is not prime (by definition)"),
        (2, True, "2 is the smallest and only even prime"),
    ],
    
    "small_primes": [
        (3, True, "3 is prime"),
        (5, True, "5 is prime"),
        (7, True, "7 is prime"),
        (11, True, "11 is prime"),
        (13, True, "13 is prime"),
        (17, True, "17 is prime"),
        (19, True, "19 is prime"),
        (23, True, "23 is prime"),
        (29, True, "29 is prime"),
    ],
    
    "small_composites": [
        (4, False, "4 = 2×2 (composite)"),
        (6, False, "6 = 2×3 (composite)"),
        (8, False, "8 = 2×4 (composite)"),
        (9, False, "9 = 3×3 (perfect square)"),
        (10, False, "10 = 2×5 (composite)"),
        (12, False, "12 = 2×6 (composite)"),
        (15, False, "15 = 3×5 (odd composite)"),
        (16, False, "16 = 4×4 (even composite)"),
        (20, False, "20 = 4×5 (composite)"),
        (21, False, "21 = 3×7 (composite)"),
    ],
    
    "perfect_squares": [
        (25, False, "25 = 5×5 (perfect square)"),
        (49, False, "49 = 7×7 (perfect square)"),
        (121, False, "121 = 11×11 (perfect square)"),
    ],
    
    "large_primes": [
        (97, True, "97 is a 2-digit prime"),
        (101, True, "101 is a 3-digit prime"),
        (541, True, "541 is a larger prime"),
        (1009, True, "1009 is a 4-digit prime"),
    ],
    
    "large_composites": [
        (100, False, "100 = 10×10"),
        (143, False, "143 = 11×13"),
        (1000, False, "1000 = 8×125"),
        (1001, False, "1001 = 7×143"),
    ],
    
    "negative_numbers": [
        (-1, False, "Negative numbers are not prime"),
        (-2, False, "-2 is not prime (by definition)"),
        (-5, False, "-5 is not prime"),
        (-17, False, "-17 is not prime (primes are natural numbers)"),
    ],
}


def run_test_cases():
    """
    Run all AI-generated test cases and report results.
    
    Returns:
        dict: Test results with pass/fail counts
    """
    total_tests = 0
    passed_tests = 0
    failed_tests = []
    
    print("=" * 80)
    print("RUNNING AI-GENERATED TEST CASES FOR is_prime(n)")
    print("=" * 80)
    
    for category, tests in TEST_CASES.items():
        print(f"\n📋 Category: {category.replace('_', ' ').title()}")
        print("-" * 80)
        
        category_passed = 0
        
        for input_val, expected, justification in tests:
            total_tests += 1
            try:
                result = is_prime(input_val)
                passed = result == expected
                
                if passed:
                    passed_tests += 1
                    category_passed += 1
                    status = "✅ PASS"
                else:
                    status = "❌ FAIL"
                    failed_tests.append({
                        'input': input_val,
                        'expected': expected,
                        'got': result,
                        'category': category
                    })
                
                print(f"  {status} | is_prime({input_val:>5}) = {str(result):<5} | {justification}")
            
            except Exception as e:
                total_tests += 1
                status = "❌ ERROR"
                failed_tests.append({
                    'input': input_val,
                    'expected': expected,
                    'error': str(e),
                    'category': category
                })
                print(f"  {status} | is_prime({input_val:>5}) raised {type(e).__name__}: {e}")
        
        print(f"  Category Result: {category_passed}/{len(tests)} passed")
    
    # Summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    print(f"Total Tests:  {total_tests}")
    print(f"Passed:       {passed_tests} ✅")
    print(f"Failed:       {len(failed_tests)} ❌")
    print(f"Pass Rate:    {(passed_tests/total_tests)*100:.1f}%")
    
    if failed_tests:
        print("\n❌ FAILED TESTS:")
        for fail in failed_tests:
            if 'error' in fail:
                print(f"  - Input: {fail['input']}, Error: {fail['error']}")
            else:
                print(f"  - Input: {fail['input']}, Expected: {fail['expected']}, Got: {fail['got']}")
    else:
        print("\n🎉 ALL TESTS PASSED! 🎉")
    
    return {
        'total': total_tests,
        'passed': passed_tests,
        'failed': len(failed_tests),
        'pass_rate': (passed_tests/total_tests)*100
    }


def demonstrate_function():
    """Demonstrate the is_prime function with various examples."""
    print("\n" + "=" * 80)
    print("FUNCTION DEMONSTRATION")
    print("=" * 80)
    
    test_numbers = [1, 2, 3, 4, 5, 10, 15, 17, 20, 29, 30, 97, -5, 0]
    
    print("\nQuick Demonstration:")
    print("-" * 80)
    for num in test_numbers:
        result = is_prime(num)
        print(f"  is_prime({num:>3}) = {result}")


# ============================================================================
# AI JUSTIFICATION FOR TEST CASE COVERAGE
# ============================================================================
"""
TEST CASE JUSTIFICATION (Generated by AI):

1. BOUNDARY CASES:
   - Tests edge cases (0, 1) where standard algorithms might fail
   - Ensures the function correctly handles the definition of prime numbers
   - Tests smallest prime (2), which is special (only even prime)

2. SMALL PRIMES:
   - Tests well-known small primes (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
   - Verifies the function correctly identifies primes
   - Covers range where manual verification is easy

3. SMALL COMPOSITES:
   - Tests various composite numbers (products of primes)
   - Includes both even and odd composites
   - Tests products of small primes

4. PERFECT SQUARES:
   - Special case: numbers like 25, 49, 121 are products of two identical primes
   - Tests divisibility by square roots
   - Important for optimization verification (loop goes up to sqrt(n))

5. LARGE PRIMES:
   - Tests function efficiency with larger numbers
   - Verifies the sqrt(n) optimization works correctly
   - Examples: 97, 101, 541, 1009

6. LARGE COMPOSITES:
   - Tests function with larger non-prime numbers
   - Ensures efficiency for larger inputs
   - Confirms divisibility checks work at scale

7. NEGATIVE NUMBERS:
   - Tests behavior with negative integers
   - Ensures function correctly returns False (primes are natural numbers > 1)
   - Verifies type handling

WHY THIS COVERAGE IS COMPREHENSIVE:
✓ Tests mathematical edge cases (0, 1, 2)
✓ Tests small numbers (verification possible by hand)
✓ Tests large numbers (optimization verification)
✓ Tests all input types (positive, negative, zero)
✓ Tests different compositeness patterns
✓ Tests algorithmic efficiency (sqrt optimization)

ALGORITHM ANALYSIS:
- Time Complexity: O(√n) - checks divisors only up to √n
- Space Complexity: O(1) - constant space
- Why it works: If n = a×b and a ≤ b, then a ≤ √n
"""


def user_input_testing():
    """Allow user to input numbers and test them for primality."""
    print("\n" + "=" * 80)
    print("USER INPUT TESTING")
    print("=" * 80)
    print("Test custom numbers for primality")
    print("(Enter 'quit' or 'exit' to stop)")
    print("-" * 80)
    
    while True:
        try:
            user_input = input("\nEnter a number to check if it's prime (or 'quit'): ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Exiting user input mode.\n")
                break
            
            number = int(user_input)
            result = is_prime(number)
            
            print(f"  is_prime({number}) = {result}")
            
            if result:
                print(f"  ✅ {number} is a PRIME number")
            else:
                print(f"  ❌ {number} is NOT a prime number")
        
        except ValueError:
            print(f"  ❌ Invalid input: '{user_input}' is not an integer. Please try again.")
        except Exception as e:
            print(f"  ❌ Error: {e}")


if __name__ == "__main__":
    # Run all test cases
    results = run_test_cases()
    
    # Demonstrate the function
    demonstrate_function()
    
    # Print summary
    print("\n" + "=" * 80)
    print("FINAL RESULT")
    print("=" * 80)
    if results['failed'] == 0:
        print("✅ SUCCESS: All test cases passed!")
        print(f"   Total: {results['total']} tests")
        print(f"   Pass Rate: {results['pass_rate']:.1f}%")
    else:
        print(f"❌ FAILURE: {results['failed']} test(s) failed")
    
    # Allow user input testing
    try:
        user_input_testing()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
