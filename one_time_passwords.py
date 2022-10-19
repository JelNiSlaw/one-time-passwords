def main():
    with open("slowa.txt") as f:
        words = [line.rstrip() for line in f]

    solve_a(words)
    solve_b(words)


def solve_a(words: list[str]):
    passwords = [word[::-1] for word in words]

    writelines("hasla_a.txt", passwords)

    longest_password = min(passwords, key=len)
    shortest_password = min(passwords, key=len)

    lines = [
        f"Longest password ({len(longest_password)} chars): {longest_password}",
        f"Shortest password ({len(shortest_password)} chars): {shortest_password}",
    ]

    writelines("slowa_a.txt", lines)


def solve_b(words: list[str]):
    passwords = []

    for word in words:
        palindrome = starting_palindrome(word)
        tail = word[len(palindrome) :]
        passwords.append(tail[::-1] + word)

    writelines("hasla_b.txt", passwords)

    lines = ["12 char passwords:"]
    lines.extend(f"- {password}" for password in passwords if len(password) == 12)
    lines.append("")

    longest_password = min(passwords, key=len)
    shortest_password = min(passwords, key=len)
    lines.append(f"Longest password: {longest_password}")
    lines.append(f"Shortest password: {shortest_password}")
    lines.append("")

    len_sum = sum(len(password) for password in passwords)
    lines.append(f"Summed length of all passwords: {len_sum}")

    writelines("slowa_b.txt", lines)


def starting_palindrome(word: str) -> str:
    palindrome = word[0]
    for i in range(1, len(word)):
        slice = word[: i + 1]
        if slice == slice[::-1]:
            palindrome = slice

    return palindrome


def writelines(filename: str, lines: list[str]):
    with open(filename, "w") as f:
        f.writelines(line + "\n" for line in lines)


if __name__ == "__main__":
    main()
