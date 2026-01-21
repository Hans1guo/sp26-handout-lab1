from typing import Callable

"""
This question has two parts:

Part 1: Please implement these stub functions to match the documentation.
It will be useful to use a dict to store the "threshold" for each tax bracket, 
and use an appropriate control structure to go over it and find the right tax bracket.

Part 2: The California, New York, and Federal tax functions should have code in common.
Factor it out into a helper function, so that the code is not repeated, but the functionality
remains the same.

As always, make sure to implement tests in the tests directory.
"""
def progressive_tax(income: int, brackets:list[tuple[int, float]]) -> float:
    """
    Compute progressive tax.
    brackets: list of (upper_bound_inclusive, rate) sorted by upper_bound ascending.
              The last upper_bound can be a very large number.
    """
    if income <= 0:
        return 0.0
    
    tax = 0.0
    lower = 0

    for upper, rate in brackets:
        if income <= lower:
            break

        chunk = min(income, upper) - lower
        tax += chunk * rate
        lower = upper

        if income <= upper:
            break

    return tax


# Relevant information:
# Federal income tax rates:  https://www.irs.gov/filing/federal-income-tax-rates-and-brackets
# California income tax rates: https://www.hrblock.com/tax-center/filing/states/california-tax-rates
# Massachusetts income tax rate: 5% for everyone
# New York state income tax rates: https://www.nerdwallet.com/article/taxes/new-york-state-tax

def income_tax_fed(income: int) -> float:
    """Calculates the amount of federal income tax paid by somebody in the United States
    
    Parameters
    ----------
    income : int
        A person's annual income (before tax)
    
    Returns
    -------
    float
        The amount of federal income tax they pay
    """
    fed_brackets: list[tuple[int, float]] = [
        (11_600, 0.10),
        (47_150, 0.12),
        (100_525, 0.22),
        (191_950, 0.24),
        (243_725, 0.32),
        (609_350, 0.35),
        (10**18, 0.37),
    ]
    return progressive_tax(income, fed_brackets)
    pass

def income_tax_ca(income: int) -> float:
    """Calculates the amount of state income tax paid by somebody who lives in California
    
    Parameters
    ----------
    income : int
        A person's annual income (before taxes)
    
    Returns
    -------
    float
        The amount of CA state tax they pay if they live in California
    """
    ca_brackets: list[tuple[int, float]] = [
        (10_756, 0.01),
        (25_499, 0.02),
        (40_245, 0.04),
        (55_866, 0.06),
        (70_606, 0.08),
        (360_659, 0.093),
        (432_787, 0.103),
        (721_314, 0.113),
        (10**18, 0.123),
    ]
    return progressive_tax(income, ca_brackets)
    pass

def income_tax_ma(income: int) -> float:
    """Calculates the amount of state income tax paid by somebody who lives in Massachusetts
    
    Parameters
    ----------
    income : int
        A person's annual income (before taxes)
    
    Returns
    -------
    float
        The amount of MA state tax they pay if they live in Masachusetts
    """
    if income <= 0:
        return 0.0
    return income * 0.05
    pass

def income_tax_ny(income: int) -> float:
    """Calculates the amount of state income tax paid by somebody who lives in New York state
    
    Parameters
    ----------
    income : int
        A person's annual income (before taxes)
    
    Returns
    -------
    float
        The amount of MA state tax they pay if they live in New York state
    """
    ny_brackets: list[tuple[int, float]] = [
        (8_500, 0.04),
        (11_700, 0.045),
        (13_900, 0.0525),
        (80_650, 0.055),
        (215_400, 0.06),
        (1_077_550, 0.0685),
        (5_000_000, 0.0965),
        (25_000_000, 0.103),
        (10**18, 0.109),
    ]
    return progressive_tax(income, ny_brackets)
    pass

def calculate_income_tax() -> None:
    """
    1. Ask the user to input their state (CA for California, MA for Massachusetts, NY for New York)
    2. Ask the user to input an annual income
    3. Print a sentence formatted like this: "Your income is XX before tax and XX after tax. You pay XX income tax."
    4. Handle invalid unit inputs gracefully with the error message "Invalid state. Please enter CA, MA, or NY."
    """
    state = input("Enter your state (CA, MA, NY): ").strip().upper()

    tax_func_map: dict[str, Callable[[int], float]] = {
        "CA": income_tax_ca,
        "MA": income_tax_ma,
        "NY": income_tax_ny,
    }

    if state not in tax_func_map:
        print("Invalid state. Please enter CA, MA, or NY.")
        return

    income_str = input("Enter your annual income: ").strip()
    income = int(income_str)

    tax = tax_func_map[state](income)
    after_tax = income - tax

    print(
        f"Your income is {income} before tax and {after_tax:.2f} after tax. "
        f"You pay {tax:.2f} income tax."
    )
    pass
