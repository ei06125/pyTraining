# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Imports
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Standard Library
import pytest

import tracemalloc

from string_mutations.string_mutations import mutate_string_1, mutate_string_2  # type: ignore

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Tests
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# ===========================================================================
# Sample Tests
# ===========================================================================


@pytest.mark.parametrize("solver", [mutate_string_1, mutate_string_2])
def test_mutate_string(solver):
    result = solver("abracadabra", 5, "k")
    assert result == "abrackdabra"


# ===========================================================================
# Generated Tests (ChatGPT)
# ===========================================================================


@pytest.mark.parametrize("solver", [mutate_string_1, mutate_string_2])
@pytest.mark.parametrize(
    "s, position, character, expected",
    [
        # ✅ Basic Functionality
        ("abracadabra", 5, "k", "abrackdabra"),
        ("hello", 0, "y", "yello"),
        ("world", 4, "z", "worlz"),
        # 🧪 Edge Cases
        ("a", 0, "b", "b"),
        ("aaaaa", 2, "b", "aabaa"),
        ("testcase", 0, "T", "Testcase"),
        ("openai", 5, "G", "openaG"),
        # 🧠 Special Characters
        ("abcde", 2, "@", "ab@de"),
        # 📏 Large Input
        ("a" * 10000, 9999, "z", "a" * 9999 + "z"),
    ],
)
def test_mutate_string(solver, s, position, character, expected):
    assert solver(s, position, character) == expected


@pytest.mark.parametrize("solver", [mutate_string_1, mutate_string_2])
def test_mutate_string_benchmark(solver, benchmark):
    s = "a" * 10000
    position = 9999
    character = "z"

    result = benchmark(solver, s, position, character)

    assert result == "a" * 9999 + "z"


@pytest.mark.parametrize("solver", [mutate_string_1, mutate_string_2])
def test_memory_usage(solver):
    s = "a" * 10000
    position = 9999
    character = "z"

    tracemalloc.start()
    _ = solver(s, position, character)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Current: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB")

    # You can assert upper bounds if needed:
    assert peak < 500 * 1024  # e.g., less than 500 KB
