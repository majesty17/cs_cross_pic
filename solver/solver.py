# -*- coding: utf-8 -*-
import copy
import logging

import numpy as np

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def guess(str, length, filter):
    '''

    :param str:  "1,1,2"
    :param length:   6
    :param filter:  [ -1 , -1 , -1 , -1 , 1 , -1]
    :return:
    '''

    if len(str) != 0:
        nums = str.split(',')
        nums = [int(i) for i in nums]
    else:
        nums = []
    seg_ct = len(nums)
    print nums, length
    if sum(nums) + len(nums) - 1 > length:
        print "illegal case!"
        return -1
    if len(filter) not in (0, length):
        print "illegal filter"
        return -2

    bucket = seg_ct + 1  # 桶的个数
    eggs = length - sum(nums) - bucket + 2
    # print "%d eggs put in %d buckets!" % (eggs, bucket)
    ways = puteggs(eggs, bucket)
    ret = []
    for i in ways:
        case = merge(nums, i)
        if filt(case, filter):  # 使用filter过滤
            ret.append(case)
            # ret.append(merge(nums, i))

    logging.info("%d eggs put in %d buckets!" % (eggs, bucket))
    logging.info("%d ways found!" % len(ret))
    return ret


def filt(case, filter):
    if len(filter) == 0:
        return True

    if len(case) != len(filter):
        logging.error("filt error! length not eaqle!")
        return False
    for i in range(len(case)):
        if filter[i] != -1 and filter[i] != case[i]:
            return False
    return True


def merge(nums, buckets):
    bucket = copy.copy(buckets)
    l_num = len(nums)
    l_buc = len(bucket)
    if l_num + 1 != l_buc:
        print "merge error!"
        return []
    # 增加已有egg
    ret = []
    for i in range(l_buc - 2):
        bucket[i + 1] = bucket[i + 1] + 1
    for i in range(l_num):
        ret = ret + ([0] * bucket[i])
        ret = ret + ([1] * nums[i])
    ret = ret + ([0] * bucket[l_buc - 1])
    return ret


def puteggs(egg, bucket):
    if egg == 0:
        return [[0] * bucket]
    if bucket == 1:
        return [[egg]]

    ret = []
    for i in range(egg + 1):
        qi = puteggs(egg - i, bucket - 1)  # 第一个桶放i个的方法数,放0个~全放
        for j in qi:
            ret.append([i] + j)

    return ret


def ana(data):
    ct = len(data)
    d = np.array(data)
    sum0 = d.sum(axis=0)
    ret = []
    for i in sum0:
        if i == 0:
            ret.append("□")
        elif i == ct:
            ret.append("■")
        else:
            ret.append("✕")
    logging.info("in ana")
    return "".join(ret)


if __name__ == "__main__":
    ret = guess("6,2,2", 15, [])
    for i in ret:
        print i
    print ana(ret)
