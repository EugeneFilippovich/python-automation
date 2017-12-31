import random


def arange(*args, **kwargs):
    if len(args) == False and len(kwargs) == False:
        print("Input at least one Argument or Key Argument")
        return

    elif len(args) + len(kwargs) > 3:
        print("Input max 3 arguments")
        return

    elif len(args):
        if(args[0] * args[1]) < 0 or (args[0] * args[2]) < 0 or (args[1] * args[2]) < 0 or args[2] == 0:
            print("You have negative or zero stepping. Infinite loop causes.")
            return
        elif len(args) == 1:
            start = 0
            stop = args[0]
            step = 1

        elif len(args) == 2:
            start = args[0]
            stop = args[1]
            step = 1

        elif len(args) == 3:
            start = args[0]
            stop = args[1]
            step = args[2]
            if step > stop:
                print("Error! Your 'step' argument is greater than 'stop' argument")
                return

        while start <= stop:
            yield start
            start += step

    elif len(kwargs):
        # HELP! if I use less than 3 kwargs - error occurs
        if (int(kwargs['start']) * int(kwargs['stop'])) < 0 or (int(kwargs['start']) * int(kwargs['step'])) < 0 or (int(kwargs['stop']) * int(kwargs['step'])) < 0 or int(kwargs['step'] == 0):
            print("You have negative or zero stepping. Infinite loop causes.")
            return

        elif "stop" in kwargs and len(kwargs) == 1:
            start = 0
            stop = int(kwargs['stop'])
            step = 1

        elif "start" and "stop" in kwargs and len(kwargs) == 2:
            start = kwargs[0]
            stop = kwargs[1]
            step = 1

        elif "stop" and "step" in kwargs and len(kwargs) == 2:
            start = 0
            stop = kwargs[1]
            step = kwargs [2]
        elif "start" and "stop" and "step" in kwargs and len(kwargs) == 3:
            start = int(kwargs["start"])
            stop = int(kwargs["stop"])
            step = int(kwargs["step"])

        while start <= stop:
            yield start
            start += step


# var = int(raw_input("0 - manual, 1 - args, 2 - kwargs: "))

# if var == 0:
for n in arange(5):
    print(n)
#
# elif var == 1:
#
#     for n in arange(int(input("Input start: ")), int(input("Input stop: ")) , int(input("Input step: "))):
#         print(n)
# elif var == 2:
#     for n in arange(start=int(input("Input start: ")), stop=1000000000000000000000000000000000000000000000000000000000000000000, step=random.randint(12345678912345, 123456789123456789123456789)):
#         print(n)