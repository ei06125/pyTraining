# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Imports
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import pytest
import tracemalloc

from remove_duplicates.remove_duplicates import Solution  # type: ignore

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Tests
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# ===========================================================================
# Sample Tests
# ===========================================================================


@pytest.mark.parametrize("solver", [Solution()])
def test_remove_duplicates_leetcode(solver):
    s = solver

    # Case 1
    nums = [1, 1, 2]
    k = s.removeDuplicates(nums)
    assert 2 == k
    assert [1, 2] == nums[:k]

    # Case 2
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = s.removeDuplicates(nums)
    assert 5 == k
    assert [0, 1, 2, 3, 4] == nums[:k]


# ===========================================================================
# Generated Tests (ChatGPT)
# ===========================================================================


@pytest.mark.parametrize("solver", [Solution()])
@pytest.mark.parametrize(
    "nums, expected_k, expected_nums_prefix",
    [
        # 🔁 Basic Cases
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        # 🎯 Edge Cases
        ([1], 1, [1]),  # Single element
        ([-100], 1, [-100]),  # Lowest bound value
        ([100] * 10, 1, [100]),  # All duplicates, upper bound value
        ([-1, 0, 1, 2, 3], 5, [-1, 0, 1, 2, 3]),  # No duplicates
        ([1, 1, 1, 1, 1, 1, 1, 1], 1, [1]),  # All elements the same
        # 🧪 Large Cases (still fast to run)
        ([1] * 1000 + [2] * 1000 + [3] * 1000, 3, [1, 2, 3]),
        (list(range(30000)), 30000, list(range(30000))),  # Max size, all unique
    ],
)
def test_remove_duplicates(solver, nums, expected_k, expected_nums_prefix):
    k = solver.removeDuplicates(nums)
    assert k == expected_k
    assert nums[:k] == expected_nums_prefix


# ===========================================================================
# Performance Tests
# ===========================================================================


@pytest.mark.parametrize("solver", [Solution()])
def test_large_input_performance(solver, benchmark):
    nums = list(range(10000)) * 3  # 30,000 elements with duplicates
    nums.sort()  # Ensure sorted input

    def run():
        solver.removeDuplicates(nums)

    result = benchmark(run)
    print(result)


@pytest.mark.parametrize("solver", [Solution()])
def test_memory_usage(solver):
    nums = list(range(10000)) * 2
    nums.sort()

    tracemalloc.start()
    k = solver.removeDuplicates(nums)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Memory used: {peak / 1024:.2f} KB")
    assert k > 0  # sanity check
    assert peak < 1_000_000  # less than ~1 MB, for example
