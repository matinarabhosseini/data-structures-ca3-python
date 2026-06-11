def can_place_ships(bad_spots, n, k, a):
    bad_spots.sort()
    bad_spots = [0] + bad_spots + [n + 1]
    count = 0

    for i in range(1, len(bad_spots)):
        space = bad_spots[i] - bad_spots[i - 1] - 1
        count += max(0, (space + 1) // (a + 1))

    return count >= k

def get_first_impossible_round(n, k, a, m, shots):
    left = 0
    right = m
    result = -1

    while left < right:
        mid = (left + right) // 2
        if can_place_ships(shots[:mid + 1], n, k, a):
            left = mid + 1
        else:
            result = mid + 1
            right = mid

    return result if result != -1 else -1

n, k, a = map(int, input().split())
m = int(input())
shots = list(map(int, input().split()))

print(get_first_impossible_round(n, k, a, m, shots))
