def longest_substring_two_chars(s: str) -> str:
    maxLen = 0
    maxSS = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i : j + 1]
            unique_chars = set(substring)
            if len(unique_chars) <= 2 and len(substring) > maxLen:
                maxLen = len(substring)
                maxSS = substring

    return maxSS


test_case = input("Enter a test string: ")
print(
    "Longest substring:",
    longest_substring_two_chars(test_case),
)
print("23bcs11317\tYash Gupta")
