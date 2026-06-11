def is_enough_time(mid, ovens, t):
    total_bread = 0
    for k in ovens:
        total_bread += mid // k
        if total_bread >= t:
            return True
    return False

def minimum_time_to_bake(n, t, ovens):
    left = 1
    right = max(ovens) * t
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if is_enough_time(mid, ovens, t):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

n, t = map(int, input().split())
ovens = list(map(int, input().split()))

print(minimum_time_to_bake(n, t, ovens))
