#!/usr/bin/env python3


def GenerateBBSTArray(a):
    def CalculateGreaterOrEqualBBSTArrayLen(filled_len):
        BBST_len = 0
        depth = 0
        while True:
            BBST_len = 2 ** (depth + 1) - 1
            if BBST_len >= filled_len:
                return BBST_len
            depth += 1

    BBST_len = CalculateGreaterOrEqualBBSTArrayLen(len(a))
    BBST = [None] * BBST_len

    sorted_arr = a.copy()
    sorted_arr.sort()

    def FillTreeRec(BBST, sorted_arr, work_range, root_index):
        range_length = len(work_range)
        if range_length == 0:
            return
        range_center = work_range[0] + int(range_length / 2)
        BBST[root_index] = sorted_arr[range_center]

        left_range = range(work_range[0], range_center)
        left_child_index = 2 * root_index + 1
        FillTreeRec(BBST, sorted_arr, left_range, left_child_index)

        right_range = range(range_center+1, work_range[0] + range_length)
        right_child_index = 2 * root_index + 2
        FillTreeRec(BBST, sorted_arr, right_range, right_child_index)

    FillTreeRec(BBST, sorted_arr, range(0, len(a)), 0)
    return BBST
