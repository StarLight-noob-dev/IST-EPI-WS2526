import cmath
import math


def is_invalid(x: float) -> bool:
    """Returns True if x is NaN or infinite."""
    return math.isnan(x) or math.isinf(x)


def solve_quadratic(a: float, b: float, c: float):
    """Solves ax^2 + bx + c = 0 and returns solutions and discriminant."""

    # Check invalid inputs
    if is_invalid(a) or is_invalid(b) or is_invalid(c):
        raise ValueError("Input values must not be NaN or infinite.")

    # Case 1: Not a quadratic equation
    if a == 0:
        if b == 0:
            if c == 0:
                # 0x + 0 = 0 → infinitely many solutions
                return None, None, "infinite"
            else:
                # 0x + c = 0 → no solutions
                return None, None, "none"
        else:
            # Linear equation bx + c = 0
            x = -c / b
            return x, None, "linear"

    # True quadratic equation
    discriminant = b * b - 4 * a * c
    sqrt_disc = cmath.sqrt(discriminant)

    x1 = (-b + sqrt_disc) / (2 * a)
    x2 = (-b - sqrt_disc) / (2 * a)

    return x1, x2, discriminant


def describe(discriminant):
    """Describes number and type of solutions based on discriminant."""
    if discriminant == "none":
        return "No solutions (contradiction)", 0
    if discriminant == "infinite":
        return "Infinitely many solutions", float("inf")
    if discriminant == "linear":
        return "One real solution (linear equation)", 1

    # Quadratic cases:
    if discriminant > 0:
        return "Two real solutions", 2
    elif discriminant == 0:
        return "One real double root", 1
    else:
        return "Two complex solutions", 2


def main():
    print("Solving ax^2 + bx + c = 0 (robust version)\n")

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    try:
        x1, x2, disc = solve_quadratic(a, b, c)
    except ValueError as err:
        print("\nError:", err)
        return

    description, count = describe(disc)

    print(f"\nSolution type: {description}")
    print(f"Number of solutions: {count}")

    if x1 is not None:
        print(f"\nx1 = {x1}")
    if x2 is not None:
        print(f"x2 = {x2}")


if __name__ == "__main__":
    # The input in this case is not robust but it can be
    # managed with while-try block...
    main()
