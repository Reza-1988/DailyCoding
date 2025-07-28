import functions
from threading import Thread


def threadize() -> None:
    f = []
    g = []

    for i in range(4):
        f.append(Thread(target=functions.f[i], name=str(i + 1)))
    for t in f:
        t.start()
    for t in f:
        t.join()

    for i in range(2):
        g.append(Thread(target=functions.g[i], name=str(i + 1)))
    for t in g:
        t.start()
    for t in g:
        t.join()

    t = Thread(target=functions.h[0], name=str(0))
    t.start()
    t.join()


