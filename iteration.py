import math
# column widths: 1, 9, 12, 4
template = "{a:1}|{mysqrt:20}|{math:20}|{diff:20}"


def mysqrt(a, x):
    half_of_nume = a / x
    numerator = x + half_of_nume
    return numerator / 2


# print(func(4))

# stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
# pp = pprint.PrettyPrinter(indent=4)
# test = {
#     "a": "test",
#     "b": "test",
#     "c": "test",
# }
# pp.pprint(test)
# print(test)


def test_square_root(limit):
    print(template.format(a="a", mysqrt="mysqrt(a)",
                          math="math.sqrt(a)", diff="diff"))
    for a in range(1, limit):
        dict = {
            "a": a,
            "mysqrt": mysqrt(a, 10),
            "math": math.sqrt(a),
            "diff": mysqrt(a, 3) - math.sqrt(a)
        }
        print(template.format(**dict))


test_square_root(10)


def eval_loop():
    while True:
        something = input("Evaluate something")
        if something == 'done':
            break
        print(eval(something))


eval_loop()
