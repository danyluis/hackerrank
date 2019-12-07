#!/usr/bin/python

# HackerRank
# Week of Code 5
# Bonetrousle
# https://www.hackerrank.com/challenges/bonetrousle/problem

#-----------------------------------------------------------------
def ri():
    return int(input().strip())

def ria(delim=" "):
    return [int(s) for s in input().strip().split(delim)]
#-----------------------------------------------------------------

def sumi(n):
    return (n * (n + 1)) >> 1;

def buy(n, k, b):
    if sumi(k) < n:
        return []

    l = []
    while True:
        if sumi(b) > n:
            break

        if sumi(b) == n:
            l.extend(range(1, b + 1))
            break
        
        box = min(k, n - sumi(b - 1))
        l.append(box)

        n -= box 
        b -= 1
        k = box - 1

    return l

def printl(l):
    print(" ".join(str(i) for i in l))

def main():
    for t in range(ri()):
        n, k, b = ria()
        sumk = sumi(k)
        if sumk < n:
            print(-1)
        elif sumk == n:
            printl(range(1, k + 1))
        else:
            l = buy(n, k, b)
            if sum(l) != n or len(l) != b:
                print(-1)
            else:
                printl(l)
main()
