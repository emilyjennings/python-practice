#My first python code - in a while, anyway

print("Hello World")

if 5 > 2:
    print("good work")

x = "me"
y = 10

print(x)
print(y)


# Codewars

def xo(s):
    array = s.split()
    xs = 0
    os = 0
    x = "x"
    o = "o"
    for item in array:
        if item == o:
            os += 1
        elif item == x:
            xs += 1

    if xs == os:
        return True


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
