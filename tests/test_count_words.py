from src.count_words import count_words


def test_count_words():
    assert count_words([], "") == 0
    assert count_words(["ab"], "ba") == 2
    assert count_words(["cat", "bt", "hat", "tree", "caaat"], "atach") == 6
    assert count_words(["hello", "world", "students"], "welldonehoneyr") == 10
