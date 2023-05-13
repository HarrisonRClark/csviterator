import itertools
from typing import List, Iterator


class CombinationGenerator:
    """This class is responsible for generating combinations"""
    @staticmethod
    def generate_combinations(data: List[List[str]]) -> Iterator:
        return itertools.product(*data)