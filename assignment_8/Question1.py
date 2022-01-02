scrum_tasks = [
    # task_id, benefit, cost estimates, description
    ('id_428', 50, 10, 'bug #3150: left column alignment broken'),
    ('id_528', 25, 20, 'bug #4254: logout leaves hourglass on screen'),
    ('id_644', 30, 10, 'idea: move shopping cart icon to the right'),
    ('id_222', 15, 80, 'investigate #4259: logout slow'),
    ('id_680', 30, 60, 'feat #4386: color scheme for fall skin'),
    ('id_220', 30, 20, 'feat #4255: internationalize for Spanish'),
    ('id_421', 30, 20, 'feat #4256: internationalize for Russian'),
    ('id_682', 120, 30, 'bug #4002: empty password crashes backend'),
    ('id_368', 30, 10, 'fix comments in optimization module'),
    ('id_932', 30, 25, 'bug #4846: exception thrown for empty field'),
    ('id_387', 30, 25, 'feat #8427: new option to change color scheme'),
]


# get benefits and costs from the tasks
def get_benefit_cost():
    _benefit = []
    _cost = []
    for _task in scrum_tasks:
        _benefit.append(_task[1])
        _cost.append(_task[2])
    return _benefit, _cost


# the optimizing function using DP
def optimize_scrum_tasks(_cost_constraint: int) -> (int, int, [int]):
    _sol_benefit, _sol_cost, _solution = 0, 0, []

    _val, _wt = get_benefit_cost()
    n = len(_wt)

    # Build table _dp[][] in bottom
    _dp = [[0 for w in range(_cost_constraint + 1)] for i in range(n + 1)]

    # up manner
    for i in range(n + 1):
        for w in range(_cost_constraint + 1):
            if i == 0 or w == 0:
                _dp[i][w] = 0
            elif _wt[i - 1] <= w:
                _dp[i][w] = max(_val[i - 1] + _dp[i - 1][w - _wt[i - 1]],
                                _dp[i - 1][w])
            else:
                _dp[i][w] = _dp[i - 1][w]

    # stores the result of Knapsack
    res = _dp[n][_cost_constraint]
    _sol_benefit = res

    w = _cost_constraint
    for i in range(n, 0, -1):
        if res <= 0:
            break

        if res == _dp[i - 1][w]:
            continue
        else:
            # This item is included.
            _solution.append(i - 1)
            _sol_cost += _wt[i-1]

            # Since this weight is included
            # its value is deducted
            res = res - _val[i - 1]
            w = w - _wt[i - 1]

    return _sol_benefit, _sol_cost, sorted(_solution)


for cost_limit in [9, 10, 20, 30, 40, 50, 60, 100, 150, 200, 1000]:
    sol = optimize_scrum_tasks(cost_limit)

    print('cost_constraint:' + str(cost_limit).rjust(5) +
          ', b/c: ' + str(str(sol[0]) + '/' + str(sol[1])).rjust(7) +
          ', solution: ' + str(sol[2]))
