import os
import sys
import fileinput

def cleaning(dir, file): 
    for line in fileinput.FileInput(os.path.join(dir,file),inplace=1):
        if line[0] == '{' and line[-2] == '}' and line.find('}{"id') == -1:
            if line[line.find('"geo": null}')+12] == '\n': 
                sys.stdout.write(line)


def errNum(dir, file): 
    c1 = 0; c2 = 0; c3 = 0; c4 = 0; c5 = 0
    with open(os.path.join(dir,file), 'r') as f: 
        for line in f:
            if line[0] != '{' or line[-2] != '}':
                c1 += 1
            elif line.find('}{"id') != -1: 
                c2 += 1
            elif line[line.find('"geo": null}')+12] != '\n': 
                c3 += 1
            elif line[0] == '{' and line[-2] == '}' and line.find('}{"id') == -1:
                c4 += 1
            else: 
                c5 += 1
    return (c1, c4, c3, c2, c5)

def getTop(dir, file, num): 
    with open(os.path.join(dir,file), 'r') as f: 
        count = 0 
        for line in f: 
            if count == num: 
                # idx = line.find('}{"id')
                idx = line.find('"geo": null}')
                print(line[idx+12])
                break
            count += 1
            
        

# if __name__ == "__main__":
#     print(errNum('result', 'samples.json'))
#     cleaning('result', 'samples.json')
#     print(errNum('result', 'samples.json'))
    #getTop('result', 'samples.json',2)