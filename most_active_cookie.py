#!/usr/bin/env python3
import sys
import csv
from collections import Counter

if __name__ == "__main__":
    cookieCount = Counter()
    topCookies = []
    maxCookieCount = 0

    if sys.argv[2] == "-d":
        date = sys.argv[3]
        with open(sys.argv[1]) as cookieFile:
            cookies = csv.reader(cookieFile)
            
            for i, row in enumerate(cookies):
                if i > 0 and row[1][:10] == date:
                    cookieCount[row[0]] += 1
                    if cookieCount[row[0]] == maxCookieCount:
                        topCookies.append(row[0])
                    elif cookieCount[row[0]] > maxCookieCount:
                        maxCookieCount = cookieCount[row[0]]
                        topCookies.clear()
                        topCookies.append(row[0])
    
    for t in topCookies:
        print(t)
