def linear_search(haystack: list[int], needle: int) -> bool:
    for i in haystack:
        if i == needle:
            return True
    return False
    