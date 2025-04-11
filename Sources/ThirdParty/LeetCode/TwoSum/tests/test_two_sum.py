# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Imports
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import pytest
import time

from two_sum.two_sum import Solution, OtherSolution  # type: ignore

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Tests
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# ===========================================================================
# Sample Tests
# ===========================================================================


@pytest.mark.parametrize("solver", [Solution(), OtherSolution()])
def test_two_sum(solver):
    s = solver

    # Case 1
    result = s.twoSum([2, 7, 11, 15], 9)
    assert [0, 1] == sorted(result)

    # Case 2
    result = s.twoSum([3, 2, 4], 6)
    assert [1, 2] == sorted(result)

    # Case 1
    result = s.twoSum([3, 3], 6)
    assert [0, 1] == sorted(result)


# ===========================================================================
# Additional Tests
# ===========================================================================


@pytest.mark.parametrize("solver", [Solution(), OtherSolution()])
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        # Minimal size (2 elements)
        ([1, 2], 3, [0, 1]),
        # Normal cases
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        # Large numbers within range
        ([1_000_000_000, -1_000_000_000], 0, [0, 1]),
        ([10**9, 10**9 - 1, -1], 999_999_999, [0, 2]),
        # Target is negative
        ([-5, -2, -3, -7], -10, [2, 3]),
        # Mixed positive/negative
        ([-3, 4, 3, 90], 0, [0, 2]),
        # Zeros and duplicates
        ([0, 4, 3, 0], 0, [0, 3]),
    ],
)
def test_two_sum_valid_cases(solver, nums, target, expected):
    result = solver.twoSum(nums, target)
    assert sorted(result) == sorted(expected)


# ===========================================================================
# Performance Tests
# NOTE(PO): Run with `pytest -s` to see the results
# ===========================================================================

@pytest.mark.parametrize("solver", [Solution(), OtherSolution()])
def test_two_sum_max_size(solver):
    # nums has 10,000 elements, with the answer guaranteed at the end
    nums = list(range(9998)) + [1_000_000_000, -1]
    target = 999_999_999
    expected = [9998, 9999]

    start_time = time.perf_counter()
    
    result = solver.twoSum(nums, target)
    
    end_time = time.perf_counter()
    elapsed = end_time - start_time
        
    print(f"\n[{solver.__class__.__name__}] Execution time: {elapsed:.6f} seconds")

    assert sorted(result) == sorted(expected)
