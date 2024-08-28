def reverse_words_middle(s: str) -> str:
    return " ".join([reverse_word_middle(word) for word in s.split(" ")])


def reverse_word_middle(s: str) -> str:
    n: int = len(s)
    if n <= 3:
        return s[::-1]
    mid = n // 2
    return s[: mid - 1] + s[mid + n % 2 : mid - 2 : -1] + s[mid + 1 + n % 2 :]


test_case = input("Enter a test string: ")
print(
    "Reverse Words:",
    reverse_words_middle(test_case),
)
print("23bcs11317\tYash Gupta")
