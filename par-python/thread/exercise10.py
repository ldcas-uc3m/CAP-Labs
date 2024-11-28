# using the thread module

from _thread import start_new_thread


def mysqr(val):
    """Calculates the square root of val"""
    eps = 0.00001
    old = 1
    new = 1
    while True:
        old,new = new, (new + val/new) / 2.0
        if abs(new - old) < eps:
            break
    result = new
    print ('\n root de ', val, 'is ', new, '\n') 
    return (new)

if __name__ == "__main__":
    start_new_thread(mysqr,(99,))
    start_new_thread(mysqr,(999,))
    start_new_thread(mysqr,(1733,))

    c = input("Type something to quit.")
