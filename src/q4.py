"""
Please implement this stub function to match the documentation.
As always, make sure to implement tests in the tests directory.
"""

from typing import Optional


def most_common_letter(s: str) -> Optional[str]:
    """Finds the most common letter in a given string.
    
    Parameters
    ----------
    s : str
        The input string
    
    Returns
    -------
    Optional[str]
        The most common letter in the string. If there is a tie, return the 
        letter that comes first alphabetically.
        Ignore case -- 'a' is equal to 'A'. Non-letter characters should be ignored.
        If there are no letters in the string, return None.
    """
    letters = [c.lower() for c in s if c.isalpha()]

    if not letters:
        return None
    
    counts: dict[str, int] = {}
    for c in letters:
        counts[c] = counts.get(c, 0) + 1
    
    return max(counts.keys(), key=lambda c: (counts[c], -ord(c)))    
    pass
