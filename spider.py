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
        try:
            self.head += 1
            return self.list[self.head - 1]
        except Exception as e:
            print e
            return None

def main():
    start_urls = ["http://store.steampowered.com"]
    ht = Hash(start_urls)
    qu = Queue(start_urls)
    games = []
    while(1):
        #print ht.dict
        url = qu.dequeue()
        if url == None:
            break
        print url
        try:
            s = requests.get(url, params=None, timeout=5).text
            game_ids = re.findall(re.compile('http://store.steampowered.com/app/(.*?)/.*'), url)
            if len(game_ids) > 0:
                game_id = int(game_ids[0])
                game_name = re.findall(re.compile('<div class="apphub_AppName">(.*?)</div>'), s)[0]
                games += [(game_name, game_id)]

            m = re.findall(re.compile('(http://store.steampowered.com/app/.*?)/'), s)
            #print len(m)
            for i in range(0,len(m)):
                if ht.check(m[i]):
                    ht.add(m[i])
                    qu.enqueue(m[i])
                else:
                    print "-----"
            if qu.head > 200:
                break
        except Exception as e:
            print e
    f = open("out", 'w')
    for game in games:
        f.write(str(game) + '\n')
    f.close()

if __name__ == "__main__":
    main()
