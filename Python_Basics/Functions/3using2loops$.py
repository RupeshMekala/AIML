
def print_pattern(no):
        trace = ""
        for i in range(1, no + 1):
            s = ""
            for j in range(i):
                s += "*"
            trace += s + "\n"
        return trace


sample = print_pattern(10)
print(sample)