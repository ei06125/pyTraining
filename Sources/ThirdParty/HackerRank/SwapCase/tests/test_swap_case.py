from swap_case.swap_case import swap_case  # type: ignore


def test_swap_case():
    string = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(string)
    assert 'hACKERrANK.COM PRESENTS "pYTHONIST 2".' == result
