def count_words(words: list[str], chars: str) -> int:
    result = 0
    chars_count = {char: chars.count(char) for char in set(chars)}

    for word in words:
        word_count = {char: word.count(char) for char in set(word)}
        if all(
            word_count[char] <= chars_count.get(char, 0) for char in word_count
        ):
            result += len(word)

    return result


# words = ["cat", "bt", "hat", "tree"], chars = "atach"

# words = ["hello", "world", "students"], chars = "welldonehoneyr"


print(count_words(["cat", "bt", "hat", "tree"], "atach"))
