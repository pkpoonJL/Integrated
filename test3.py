from collections import deque


def find_derivation_path(initial, rules, target):

    queue = deque()
    queue.append((initial, []))
    visited = set()

    while queue:
        current, path = queue.popleft()


        frozen = frozenset(current)
        if frozen in visited:
            continue
        visited.add(frozen)

        if target in current:
            return path


        for rule in rules:
            a, b, c, d = rule

            if (b != 0 and c !=0 and a in current and b in current and c in current and d not in current) or (b == 0 and c == 0 and a in current and d not in current)or(b!=0 and c==0 and a in current and b in current and d  not in current):
                new_current = current | {d}
                # 生成规则描述
                if b != 0 and c !=0:
                    rule_desc = f"({a},{b},{c})→{d}"
                elif b!=0 and c==0:
                    rule_desc = f"({a},{b})→{d}"
                else:
                    rule_desc = f"{a}→{d}"
                new_path = path + [rule_desc]
                queue.append((new_current, new_path))

    return None



initial_state = {1}
rules = [
    [1, 0, 0, 2],   # 1→2
    [2, 0, 0, 3],   # 2→3
    [1, 3, 0, 4],   # (1,3)→4
    [1, 2, 3, 5]    # (1,2,3)→5

]
target = 5

path = find_derivation_path(initial_state, rules, target)

if path:
    print("Path Found：", " → ".join(path))
else:
    print("None")