from whats_your_name.whats_your_name import print_full_name # type: ignore

def test_print_full_name():
    result = print_full_name("Ross", "Taylor")
    assert "Hello Ross Taylor! You just delved into python." == result
