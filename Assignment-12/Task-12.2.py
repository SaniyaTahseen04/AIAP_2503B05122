from typing import List, Any
import time, random

def bubble_sort(arr: List[Any]) -> List[Any]:
    """Sort list using Bubble Sort. O(n²) time, O(1) space."""
    arr = arr.copy()  # Keep original unmodified while sorting
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def is_sorted(arr: List[Any]) -> bool:
    """Check if list is sorted."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

if __name__ == "__main__":
    arr = []
    
    while True:
        print("\n1. Enter list  2. Sort  3. Check sorted  4. Performance  5. Exit")
        choice = input("Choice: ").strip()
        
        if choice == "1":
            arr = [int(x) if x.lstrip('-').isdigit() else x for x in input("Enter elements: ").split()]
            print(f"List: {arr}")
        
        elif choice == "2":
            if arr:
                arr = bubble_sort(arr)  # <-- FIX: now updates the actual list
                print(f"Sorted: {arr}")
            else:
                print("Enter list first")
        
        elif choice == "3":
            print("Sorted" if is_sorted(arr) else "Not sorted")
        
        elif choice == "4":
            for size in [100, 500, 1000]:
                test = [random.randint(1, 1000) for _ in range(size)]
                start = time.time()
                bubble_sort(test)
                print(f"Size {size}: {time.time() - start:.6f}s")
        
        elif choice == "5":
            print("Exited. Goodbye!")
            break
        
        else:
            print("Invalid choice")
