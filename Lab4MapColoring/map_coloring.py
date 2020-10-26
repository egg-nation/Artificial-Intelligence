def find_best_candidate(graph, current_solution):
    if True:
        candidates_with_add_info = [
            (
                -len({current_solution[neigh] for neigh in graph[n] if neigh in current_solution}),  # nb_forbidden_colours
                -len({neigh for neigh in graph[n] if neigh not in current_solution}),  # minus nb_uncolored_neighbour
                n
            ) for n in graph if n not in current_solution]
        candidates_with_add_info.sort()
        candidates = [n for _, _, n in candidates_with_add_info]

    if candidates:
        candidate = candidates[0]
        assert (candidate not in current_solution)
        return candidate

    assert (set(graph.keys()) == set(current_solution.keys()))
    return None


def solve(graph, colours, current_solution, depth):
    n = find_best_candidate(graph, current_solution)

    if n is None:
        return current_solution  # Solution is found

    for c in colours - {current_solution[neigh] for neigh in graph[n] if neigh in current_solution}:
        assert (n not in current_solution)
        assert (all((neigh not in current_solution or current_solution[neigh] != c) for neigh in graph[n]))
        current_solution[n] = c
        print("Trying to give color %s to %s" % (c, n))

        if solve(graph, colours, current_solution, depth + 1):
            print("Gave color %s to %s" % (c, n))
            return current_solution
        else:
            del current_solution[n]
            print("Cannot give color %s to %s" % (c, n))

    return None


def check_valid(graph):
    for node, nexts in graph.items():
        assert (node not in nexts)  # no node linked to itself
        for next in nexts:
            assert (next in graph and node in graph[next])  # A linked to B implies B linked to A


def check_solution(graph, solution):
    if solution is not None:
        for node, nexts in graph.items():
            assert (node in solution)
            color = solution[node]
            for next in nexts:
                assert (next in solution and solution[next] != color)


def solve_problem(graph, colours):
    # we verify if the graph is okay: vertices and edges
    check_valid(graph)
    solution = solve(graph, colours, dict(), 0)
    print(solution)
    check_solution(graph, solution)

# regions
T = 'T'
WA = 'WA'
NT = 'NT'
SA = 'SA'
Q = 'Q'
NSW = 'NSW'
V = 'V'

# constraints
example_country = {T: {V},
                   WA: {NT, SA},
                   NT: {WA, Q, SA},
                   SA: {WA, NT, Q, NSW, V},
                   Q: {NT, SA, NSW},
                   NSW: {Q, SA, V},
                   V: {SA, NSW, T}
                   }

# domain
colours = {'Red', 'Green', 'Blue'}

solve_problem(example_country, colours)
