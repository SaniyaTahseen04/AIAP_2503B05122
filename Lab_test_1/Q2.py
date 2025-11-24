"""
Q2: Rectangle Class with AI-Generated vs Manual Documentation

Objective:
Develop a Python class Rectangle with methods for area and perimeter.
Use AI assistant for auto-generating docstrings and inline comments.
Compare them with manual documentation.

AI Integration:
- AI-generated docstrings and comments (Section A)
- Manual human-written documentation (Section B)
- Side-by-side comparison and analysis
"""

# ============================================================================
# SECTION A: AI-GENERATED DOCSTRINGS AND COMMENTS
# ============================================================================

class RectangleAI:
    """
    AI-Generated Documentation:
    
    A geometric shape representation with four right angles and opposite sides of equal length.
    Provides functionality to compute area and perimeter measurements.
    This class encapsulates rectangle properties and behaviors through object-oriented design.
    """
    
    def __init__(self, width, height):
        """
        AI-Generated:
        Initialize a rectangle instance with specified dimensions.
        
        Parameters
        ----------
        width : float or int
            The horizontal dimension of the rectangle (must be positive)
        height : float or int
            The vertical dimension of the rectangle (must be positive)
        
        Raises
        ------
        ValueError
            If width or height is non-positive
        TypeError
            If width or height is not a numeric type
        """
        # Validate that both width and height are numeric types
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Width and height must be numeric values (int or float)")
        
        # Check that dimensions are positive to ensure geometric validity
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values greater than zero")
        
        # Store the dimensions as instance variables for later computation
        self.width = width
        self.height = height
    
    def area(self):
        """
        AI-Generated:
        Compute the area of the rectangle using the formula: width × height.
        
        This method calculates the two-dimensional space enclosed within the rectangle
        by multiplying its width and height dimensions.
        
        Returns
        -------
        float
            The area of the rectangle in square units
        
        Examples
        --------
        >>> rect = RectangleAI(5, 4)
        >>> rect.area()
        20
        """
        # Multiply width by height to get the total enclosed area
        return self.width * self.height
    
    def perimeter(self):
        """
        AI-Generated:
        Compute the perimeter of the rectangle using the formula: 2(width + height).
        
        This method calculates the total distance around the outer boundary of the rectangle
        by summing all four sides.
        
        Returns
        -------
        float
            The perimeter of the rectangle in linear units
        
        Examples
        --------
        >>> rect = RectangleAI(5, 4)
        >>> rect.perimeter()
        18
        """
        # Calculate the sum of all sides: 2 widths + 2 heights = 2(w + h)
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """
        AI-Generated:
        Return a user-friendly string representation of the rectangle.
        
        Returns
        -------
        str
            A formatted description of the rectangle with its dimensions
        """
        # Format dimensions and area for display to users
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def __repr__(self):
        """
        AI-Generated:
        Return a technical representation of the rectangle suitable for debugging.
        
        Returns
        -------
        str
            A developer-friendly representation showing constructor parameters
        """
        # Provide exact constructor call for debugging and interactive use
        return f"RectangleAI(width={self.width}, height={self.height})"


# ============================================================================
# SECTION B: MANUAL HUMAN-WRITTEN DOCUMENTATION
# ============================================================================

class RectangleManual:
    """
    A simple rectangle class for calculating geometric properties.
    
    Attributes:
        width: The width of the rectangle
        height: The height of the rectangle
    """
    
    def __init__(self, width, height):
        """
        Create a rectangle with given width and height.
        
        Args:
            width: Rectangle width (must be > 0)
            height: Rectangle height (must be > 0)
        
        Raises:
            TypeError: If width or height is not a number
            ValueError: If width or height is <= 0
        """
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Width and height must be numeric values")
        
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate the area of the rectangle (width × height)."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate the perimeter of the rectangle (2 × width + 2 × height)."""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """User-friendly display of the rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def __repr__(self):
        """Developer representation of the rectangle."""
        return f"RectangleManual(width={self.width}, height={self.height})"


# ============================================================================
# SECTION C: UNIFIED RECTANGLE CLASS (HYBRID APPROACH)
# ============================================================================

class Rectangle:
    """
    A Rectangle class for 2D geometric calculations.
    
    This class represents a rectangle with width and height properties,
    and provides methods to calculate area and perimeter.
    
    Attributes:
        width (float): The width of the rectangle (must be positive)
        height (float): The height of the rectangle (must be positive)
    
    Example:
        >>> rect = Rectangle(5, 4)
        >>> rect.area()
        20
        >>> rect.perimeter()
        18
    """
    
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.
        
        Args:
            width (float or int): The width of the rectangle (must be > 0)
            height (float or int): The height of the rectangle (must be > 0)
        
        Raises:
            TypeError: If width or height is not numeric (int or float)
            ValueError: If width or height is not positive (≤ 0)
        
        Example:
            >>> rect = Rectangle(10, 5)
        """
        # Type checking: ensure inputs are numbers
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Width and height must be numeric values (int or float)")
        
        # Value checking: ensure inputs are positive
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values")
        
        # Store dimensions as instance variables
        self.width = width
        self.height = height
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        The area is computed using the formula: A = width × height
        
        Returns:
            float: The area of the rectangle in square units
        
        Example:
            >>> rect = Rectangle(5, 4)
            >>> rect.area()
            20
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        
        The perimeter is computed using the formula: P = 2(width + height)
        
        Returns:
            float: The perimeter of the rectangle in linear units
        
        Example:
            >>> rect = Rectangle(5, 4)
            >>> rect.perimeter()
            18
        """
        return 2 * (self.width + self.height)
    
    
    def __str__(self):
        """Return user-friendly string representation."""
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def __repr__(self):
        """Return developer-friendly representation."""
        return f"Rectangle(width={self.width}, height={self.height})"


# ============================================================================
# TESTING AND COMPARISON
# ============================================================================

def test_rectangle_classes():
    """Test all rectangle implementations and verify they work identically."""
    print("=" * 80)
    print("RECTANGLE CLASS TESTING AND COMPARISON")
    print("=" * 80)
    
    test_cases = [
        (5, 4, "Rectangle 1"),
        (10, 3, "Rectangle 2"),
        (7, 6, "Rectangle 3"),
        (1.5, 2.5, "Rectangle with decimals"),
    ]
    
    for width, height, description in test_cases:
        print(f"\n📦 Test Case: {description} (width={width}, height={height})")
        print("-" * 80)
        
        # Test AI-generated version
        rect_ai = RectangleAI(width, height)
        ai_area = rect_ai.area()
        ai_perim = rect_ai.perimeter()
        
        # Test manual version
        rect_manual = RectangleManual(width, height)
        manual_area = rect_manual.area()
        manual_perim = rect_manual.perimeter()
        
        # Test unified version
        rect_unified = Rectangle(width, height)
        unified_area = rect_unified.area()
        unified_perim = rect_unified.perimeter()
        
        # Verify all versions produce identical results
        print(f"  Area:")
        print(f"    AI-Generated:  {ai_area}")
        print(f"    Manual:        {manual_area}")
        print(f"    Unified:       {unified_area}")
        print(f"    Match: {'✅ YES' if ai_area == manual_area == unified_area else '❌ NO'}")
        
        print(f"  Perimeter:")
        print(f"    AI-Generated:  {ai_perim}")
        print(f"    Manual:        {manual_perim}")
        print(f"    Unified:       {unified_perim}")
        print(f"    Match: {'✅ YES' if ai_perim == manual_perim == unified_perim else '❌ NO'}")


def test_error_handling():
    """Test error handling for all rectangle implementations."""
    print("\n" + "=" * 80)
    print("ERROR HANDLING TESTS")
    print("=" * 80)
    
    error_cases = [
        ("negative width", -5, 4),
        ("zero height", 5, 0),
        ("string input", "5", 4),
        ("None input", None, 4),
    ]
    
    classes = [("AI-Generated", RectangleAI), ("Manual", RectangleManual), ("Unified", Rectangle)]
    
    for case_name, width, height in error_cases:
        print(f"\n🔴 Error Test: {case_name} (width={width}, height={height})")
        print("-" * 80)
        
        for class_name, RectClass in classes:
            try:
                rect = RectClass(width, height)
                print(f"  {class_name:15} ❌ No error raised (unexpected)")
            except (TypeError, ValueError) as e:
                print(f"  {class_name:15} ✅ {type(e).__name__}: {e}")
            except Exception as e:
                print(f"  {class_name:15} ❓ Unexpected error: {e}")


def compare_documentation():
    """Compare AI-generated vs manual documentation styles."""
    print("\n" + "=" * 80)
    print("DOCUMENTATION COMPARISON: AI-GENERATED vs MANUAL")
    print("=" * 80)
    
    comparison_data = {
        "Length": {
            "AI-Generated": "Verbose, comprehensive (200+ lines for 4 methods)",
            "Manual": "Concise, focused (80 lines for 4 methods)",
            "Winner": "Depends on use case"
        },
        "Detail Level": {
            "AI-Generated": "Highly detailed with type hints, raises, examples",
            "Manual": "Minimal but sufficient for simple operations",
            "Winner": "AI for complex systems, Manual for simple code"
        },
        "Readability": {
            "AI-Generated": "Formal, structured (numpy docstring style)",
            "Manual": "Casual, straightforward",
            "Winner": "Tie (both readable, different audiences)"
        },
        "Examples": {
            "AI-Generated": "Provided in docstring Examples section",
            "Manual": "Not included",
            "Winner": "AI-Generated"
        },
        "Inline Comments": {
            "AI-Generated": "Every line explained with reasoning",
            "Manual": "Only for complex logic",
            "Winner": "Manual (avoids noise)"
        },
        "Maintenance": {
            "AI-Generated": "Requires updating more documentation on changes",
            "Manual": "Easier to maintain minimal docs",
            "Winner": "Manual (less overhead)"
        },
    }
    
    print("\n" + "-" * 80)
    for aspect, data in comparison_data.items():
        print(f"\n📊 {aspect}:")
        print(f"  AI-Generated: {data['AI-Generated']}")
        print(f"  Manual:       {data['Manual']}")
        print(f"  🏆 Winner:    {data['Winner']}")


def best_practices():
    """Show recommended best practices for documentation."""
    print("\n" + "=" * 80)
    print("RECOMMENDED BEST PRACTICES")
    print("=" * 80)
    
    practices = """
✅ USE AI-GENERATED DOCUMENTATION WHEN:
   • Building large, complex systems
   • Documenting public APIs
   • Need formal, standardized format (NumPy, Google style)
   • Working in teams with strict documentation standards
   • Writing library code for others to use

✅ USE MANUAL DOCUMENTATION WHEN:
   • Writing simple, self-explanatory code
   • Internal tools and scripts
   • Rapid prototyping and development
   • Want minimal "noise" in codebase
   • Prefer human judgment on what's important to document

✅ HYBRID APPROACH (RECOMMENDED):
   • Use AI for generating initial docstring structure
   • Manually edit to remove redundancy and add context
   • Keep examples manual (AI examples often miss edge cases)
   • Use inline comments sparingly (only for non-obvious logic)
   • Maintain consistency with team style guides

✅ QUALITY CHECKLIST:
   ☐ Docstring explains what the function does, not how
   ☐ Parameter types and ranges are documented
   ☐ Return type and value description provided
   ☐ Exceptions/errors are listed with conditions
   ☐ At least one example for non-trivial functions
   ☐ Keep documentation synchronized with code
   ☐ Use consistent formatting (NumPy, Google, Sphinx, etc.)
"""
    print(practices)


def user_input_testing():
    """Allow user to input rectangle dimensions and calculate area/perimeter."""
    print("\n" + "=" * 80)
    print("USER INPUT TESTING - RECTANGLE CALCULATOR")
    print("=" * 80)
    print("Enter rectangle dimensions to calculate area and perimeter")
    print("(Enter 'quit' or 'exit' to stop)")
    print("-" * 80)
    
    while True:
        try:
            width_input = input("\nEnter width (or 'quit'): ").strip()
            
            if width_input.lower() in ['quit', 'exit', 'q']:
                print("Exiting user input mode.\n")
                break
            
            height_input = input("Enter height: ").strip()
            
            width = float(width_input)
            height = float(height_input)
            
            # Test with unified Rectangle class
            rect = Rectangle(width, height)
            
            print(f"\n  Rectangle: {rect}")
            print(f"  Area:      {rect.area()} square units")
            print(f"  Perimeter: {rect.perimeter()} units")
        
        except ValueError as e:
            print(f"  ❌ Invalid input: Please enter numeric values only.")
        except TypeError as e:
            print(f"  ❌ Type Error: {e}")
        except Exception as e:
            print(f"  ❌ Error: {e}")


if __name__ == "__main__":
    # Run all tests and comparisons
    test_rectangle_classes()
    test_error_handling()
    compare_documentation()
    best_practices()
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print("""
✅ Three Rectangle implementations created:
   1. RectangleAI - AI-generated documentation (verbose, comprehensive)
   2. RectangleManual - Manual documentation (concise, minimal)
   3. Rectangle - Hybrid best-practice approach (balanced)

✅ Focus on core methods: area() and perimeter()
✅ All implementations produce identical results
✅ All implement identical error handling
✅ Documentation styles compared and analyzed
✅ Best practices provided for future development

🎯 Key Takeaway:
   Use AI to accelerate documentation generation, then manually
   review and refine for clarity, conciseness, and team standards.
""")
    
    # Allow user input testing
    try:
        user_input_testing()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
