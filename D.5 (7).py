def longest_substring(s: str, k: int) -> int:
    from collections import Counter
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            count = Counter(substring)
            if all(val >= k for val in count.values()):
                max_len = max(max_len, len(substring))
    return max_len

s = input("Enter a string: ")
k = int(input("Enter an integer k: "))
print(longest_substring(s, k))
