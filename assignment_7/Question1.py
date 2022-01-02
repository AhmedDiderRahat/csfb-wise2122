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


# The function returns the best possible set of task with maximum benefits withing cost constraints
def optimize_scrum_tasks(_cost_constraint: int) -> (int, int, [int]):
    _sol_benefit, _sol_cost, _solution = 0, 0, []

    # get all possible sets of solution
    _candidates_set = generate(list(range(0, len(scrum_tasks))))

    _sol_benefit = 0
    _sol_cost = 0

    for _candidate in _candidates_set:
        _sum_benefit = 0
        _sum_cost = 0

        # Calculating sum of benefit and costs
        for _data in _candidate:
            _sum_benefit += scrum_tasks[_data][1]
            _sum_cost += scrum_tasks[_data][2]

        if _sum_cost <= _cost_constraint and _sum_benefit > _sol_benefit:
            _sol_cost = _sum_cost
            _sol_benefit = _sum_benefit
            _solution = _candidate

    return _sol_benefit, _sol_cost, _solution


# generate the all possible sets
def generate(_items: [int]) -> [[int]]:
    res = [[]]
    for item in _items:
        new_set = [r + [item] for r in res]
        res.extend(new_set)
    return res


for cost_limit in [9, 10, 20, 30, 40, 50, 60, 100, 150, 200, 1000]:
    sol = optimize_scrum_tasks(cost_limit)

    print('cost_constraint:' + str(cost_limit).rjust(5) +
          ', b/c: ' + str(str(sol[0]) + '/' + str(sol[1])).rjust(7) +
          ', solution: ' + str(sol[2]))
