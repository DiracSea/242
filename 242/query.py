import csv 
import os
import crawler

def getQuery(dir,file): 
    res = []
    with open(os.path.join(dir,file), 'r') as f:
        reader = csv.reader(f) 
        for line in reader: 
            res.append(line[0])
    return res

def getQuery1(dir,name,file): 
    res = []
    with open(os.path.join(dir,file), 'r') as f:
        reader = csv.reader(f) 
        for line in reader: 
            res.append(name+" "+line[0])
    return res

def comQuery(dir, file1, file2): 
    res = []
    with open(os.path.join(dir,file1), 'r') as f1, open(os.path.join(dir,file2), 'r') as f2:
        reader1 = csv.reader(f1) 
        reader2 = csv.reader(f2) 
        for r1 in reader1: 
            for r2 in reader2: 
                res.append(r1[0]+" "+r2[0])

    return res

def genQueries(level): 
    dir = 'file'
    query = 'query'
    post = '.csv'
    low = query+'_low'+post
    high = query+'_high'+post
    mid = query+'_mid'+post
    act = query+'_act'+post

    if level == 5:
        q = getQuery(dir, query+post)
        q1 = getQuery1(dir, 'California', act)
        q.extend(q1)
        return q1
    elif level == 4: 
        q = getQuery(dir, act)
        q1 = comQuery(dir, high, act)
        q.extend(q1)
        return q
    elif level == 3: 
        q = getQuery(dir, high)
        q1 = comQuery(dir, mid, act)
        q.extend(q1)
        return q
    elif level == 2: 
        q = getQuery(dir, mid)
        q1 = comQuery(dir, low, act)
        q.extend(q1)
        return q
    else: 
        return getQuery(dir, low)

# if __name__ == "__main__": 
#     g = genQueries(1)
#     crawler.crawler(g[0], max_tweets = 2)