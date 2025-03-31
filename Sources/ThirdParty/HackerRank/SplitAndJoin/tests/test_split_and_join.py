from split_and_join.split_and_join import split_and_join # type: ignore

def test_split_and_join():
    input = "this is a string"
    result = split_and_join(input)
    assert "this-is-a-string" == result
    