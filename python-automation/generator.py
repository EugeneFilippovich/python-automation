def arange(*args, **kwargs):
    if len(args) + len(kwargs) > 3:
        return
    if len(args) == 1:
        if len(kwargs) == 0:
            current = 0
            stop = int(args[0])
            step = 1
        elif len(kwargs) == 1:
            current = int(args[0])
            stop = int(kwargs["stop"])
            step = 1
        elif len(kwargs) == 2:
            current = int(args[0])
            stop = int(kwargs["stop"])
            step = int(kwargs["step"])
    elif len(args) == 2:
        if len(kwargs) == 0:
            current = int(args[0])
            stop = int(args[1])
            step = 1
        elif len(kwargs) == 1:
            current = args[0]
            stop = int(args[1])
            step = int(kwargs["step"])
    elif len(args) == 3:
        current = int(args[0])
        stop = int(args[1])
        step = int(args[2])
    elif len(args) == 0:
        if len(kwargs) == 1:
            current = 0
            stop = int(kwargs["stop"])
            step = 1
        elif len(kwargs) == 2:
            current = 0
            stop = int(kwargs["stop"])
            step = 1
        elif len(kwargs) == 3:
            current = int(kwargs["start"])
            stop = int(kwargs["stop"])
            step = int(kwargs["step"])
    else:
        return
    if stop < current and step > 0:
        return
    if stop > current and step < 0:
        return
    if step == 0:
        return
    if step > 0:
        yield current
        current += step
        while current < stop:
            yield current
            current += step
    else:
        yield current
        current += step
        while current > stop:
            yield current
            current += step

gen = arange(start=1, stop=8, step=2)
print(list(gen))