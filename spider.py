import requests
import re

class Hash:
    def __init__(self, inits):
        self.dict = {}
        for item in inits:
            self.add(item)

    def add(self, i):
        if(self.dict.has_key(i)):
            seld.dict[i] += 1
        else:
            self.dict[i] = 1

    def check(self, i):
        if(self.dict.has_key(i)):
            self.dict[i] += 1
            return False
        return True

class Queue:
    def __init__(self, inits):
        self.list = inits
        self.head = 0

    def enqueue(self, p):
        if(type(p) == list):
            self.list += p
        else:
            self.list += [p]
    def dequeue(self):
        self.head += 1
        return self.list[self.head - 1]

def main():
    start_urls = ["http://www.baidu.com"]
    ht = Hash(start_urls)
    qu = Queue(start_urls)
    while(1):
        url = qu.dequeue()
        print url
        s = requests.get(url).text
        m = re.findall(re.compile('"(http://.*?)"'), s)
        for i in range(0,len(m)):
            if ht.check(m[i]):
                ht.add(m[i])
                qu.enqueue(m[i])

if __name__ == "__main__":
    main()
