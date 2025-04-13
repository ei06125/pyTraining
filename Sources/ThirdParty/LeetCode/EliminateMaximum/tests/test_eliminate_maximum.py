# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Imports
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import pytest

from eliminate_maximum.eliminate_maximum import Solution, FastestSolution, MemorySolution, GptSolution  # type: ignore

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Tests
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


@pytest.fixture(scope="function", autouse=True)
def setup():
    print("")


# ===========================================================================
# Sample Tests
# ===========================================================================


@pytest.mark.parametrize(
    "solution",
    [Solution(), MemorySolution(), FastestSolution(), GptSolution()],
)
def test_eliminate_maximum_from_leetcode(solution):
    print(test_eliminate_maximum_from_leetcode.__name__)

    # Case 1
    dist = [1, 3, 4]
    speed = [1, 1, 1]
    result = solution.eliminateMaximum(dist, speed)
    assert 3 == result

    # Case 2
    dist = [1, 1, 2, 3]
    speed = [1, 1, 1, 1]
    result = solution.eliminateMaximum(dist, speed)
    assert 1 == result

    # Case 3
    dist = [3, 2, 4]
    speed = [5, 3, 2]
    result = solution.eliminateMaximum(dist, speed)
    assert 1 == result

    # Submit Case 1
    dist = [4, 3, 3, 3, 4]
    speed = [1, 1, 1, 1, 4]
    result = solution.eliminateMaximum(dist, speed)
    assert 3 == result

    # Submit Case 2
    dist = [3, 5, 7, 4, 5]
    speed = [2, 3, 6, 3, 2]
    result = solution.eliminateMaximum(dist, speed)
    assert 2 == result


# ===========================================================================
# Generated Tests (ChatGPT)
# ===========================================================================


@pytest.mark.parametrize(
    "solution",
    [Solution(), MemorySolution(), FastestSolution(), GptSolution()],
    ids=lambda s: s.__class__.__name__,
)
def test_eliminate_maximum_large_input(solution, benchmark):
    print(test_eliminate_maximum_large_input.__name__)
    print(solution.__class__.__name__)
    # All monsters are 100000 km away, speed = 1 km/min => 100000 min till city
    n = 100000
    dist = [100000] * n
    speed = [1] * n

    result = benchmark(solution.eliminateMaximum, dist, speed)
    assert result == n


import time


@pytest.mark.parametrize("solution", [Solution(), MemorySolution(), FastestSolution(), GptSolution()])
def test_time_trend(solution):
    print(test_time_trend.__name__)
    print(solution.__class__.__name__)
    for size in [10_000, 50_000, 100_000]:
        dist = [100_000] * size
        speed = [1] * size
        start = time.time()
        solution.eliminateMaximum(dist, speed)
        print(f"n={size}: time={time.time() - start:.4f} sec")


import tracemalloc


@pytest.mark.parametrize(
    "solution",
    [Solution(), MemorySolution(), FastestSolution(), GptSolution()],
)
def test_memory_usage_large_input(solution):
    print(test_memory_usage_large_input.__name__)
    print(solution.__class__.__name__)
    n = 100000
    dist = [100000] * n
    speed = [1] * n

    tracemalloc.start()
    solution.eliminateMaximum(dist, speed)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Peak memory usage: {peak / 1024:.2f} KB")
    assert peak < 10 * 1024 * 1024  # e.g., under 10MB
