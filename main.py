from collections import Counter
import sys


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2

        flowers = data[idx : idx + n]
        idx += n

        counts = Counter(flowers)
        best = 0

        for petals, count in counts.items():
            next_count = counts.get(petals + 1, 0)

            take_current = min(count, m // petals)
            spent = take_current * petals

            take_next = min(next_count, (m - spent) // (petals + 1))
            spent += take_next * (petals + 1)

            upgrades = min(take_current, next_count - take_next, m - spent)
            best = max(best, spent + upgrades)

        out.append(str(best))

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    solve()
