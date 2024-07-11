from typing import Iterable
from pvlive_api import PVLive


def get_pv_live():
    """Print IDs of all GSPs and PESs"""
    pvl = PVLive()

    print(len(pvl.pes_ids))
    print(len(pvl.gsp_ids))


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)
