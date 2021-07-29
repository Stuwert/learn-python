def right_justify(str):
    max_length = 70
    leftover = max_length - len(str)
    if (leftover > 0):
        return ' ' * leftover + str
    return str[-70:]


print(right_justify('test'))
print(right_justify('tesASDFLJKAHSDFLKJASHDFLKJASHDFOIa;lksjdf;lmnasd;fsau;giasudf;lksandf;lkans;ldfkasujd;flkajs;dlfkjt'))


def do_twice(f, arg):
    f(arg)
    f(arg)


def print_spam(arg):
    print(arg)


do_twice(print_spam, 'spam')


def do_four(f, arg):
    for list in range(0, 4):
        f(arg)


do_four(print_spam, 'bam')
