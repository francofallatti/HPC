#!/usr/bin/env python3

# Copyright (c) 2019-2021 Forschungszentrum Jülich GmbH

from mpi4py import MPI


def global_sum_ring(x, root, comm):
    r = comm.rank
    s = comm.size

    next = r + 1 if r + 1 < s else 0
    prev = r - 1 if r - 1 >= 0 else s - 1

    if r == root:
        # use `MPI.Comm.sendrecv` to
        # send initial value `x` to process `next`
        # receive final result from process `prev`
        pass  # this can be removed
    else:
        tmp = x
        # use `MPI.Comm.recv` to receive partial result from process `prev`
        # use `MPI.Comm.send` to send partial result to process `next`


def global_sum_tree(x, root, comm):
    r = comm.rank
    s = comm.size

    res = x
    dist = 1
    while dist < s:
        if r % (2 * dist) == 0:
            if r + dist < s:
                # use `MPI.Comm.recv` to receive partial result
                # from right process
                pass  # this can be removed
        else:
            # use `MPI.Comm.send` to send partial result to left process
            break

        dist = 2 * dist

    if r == root:
        # use `MPI.Comm.irecv` to initiate receive from process 0
        pass  # this can be removed

    if r == 0:
        # use `MPI.Comm.send` to send final result to process `root`
        pass  # this can be removed

    if r == root:
        # use `MPI.Request.wait` to complete receive operation
        pass  # this can be removed


def global_sum_reduce(x, root, comm):
    # this can be implemented in a single call to `MPI.Comm.reduce`
    pass  # this can be removed


def main():
    test_global_sum(global_sum_ring)
    # test_global_sum(global_sum_tree)
    # test_global_sum(global_sum_reduce)


# You can ignore everything below this line
def test_global_sum(global_sum):
    r = MPI.COMM_WORLD.rank
    s = MPI.COMM_WORLD.size

    for i in range(s):
        res = global_sum(1, i, MPI.COMM_WORLD)
        if r == i and res != s:
            print(f"'{global_sum.__name__}' failed a test")
            print(f"1 + ... + 1 should be {s} but is {res}")
            MPI.COMM_WORLD.Abort(1)

        res = global_sum(r, i, MPI.COMM_WORLD)
        if r == i and res != (s * (s - 1)) // 2:
            print(f"'{global_sum.__name__}' failed a test")
            print(
                f"1 + ... + s - 1 should be {(s * (s - 1)) // 2} but is {res}"
            )
            MPI.COMM_WORLD.Abort(1)

    if r == 0:
        print(f"'{global_sum.__name__}' successfully passed all tests")


if __name__ == "__main__":
    main()
