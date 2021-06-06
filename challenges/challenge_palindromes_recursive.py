def is_palindrome_recursive(word: str, low: int, high: int) -> bool:
    """Identifica palavras ou frases palíndromas de forma recursiva"""
    if word == "" or word[low] != word[high]:
        return False
    if low == high:
        return True
    if (low < high + 1):
        return is_palindrome_recursive(word, low + 1, high - 1)
    return True
