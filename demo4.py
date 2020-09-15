
def generator():
    for i in range(100):
        yield i


print(generator())