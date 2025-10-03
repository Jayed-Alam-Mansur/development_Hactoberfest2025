def permutations(s: str) -> list[str]:
    if len(s) == 1:
        return [s]
    result = []
    for i in range(len(s)):
        for p in permutations(s[:i] + s[i+1:]):
            result.append(s[i] + p)
    return result

print(permutations("ABC"))
