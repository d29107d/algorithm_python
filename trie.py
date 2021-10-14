import json
import re

class Trie:
    def __init__(self):
        self.root = {}
        self.word_end = -1

    def insert(self, word):
        curNode = self.root
        for c in word:
            if not c in curNode:
                curNode[c] = {}
            curNode = curNode[c]

        if curNode == {}:
            curNode[self.word_end] = True

    def search(self, word):
        curNode = self.root
        for c in word:
            if not c in curNode:
                return False
            curNode = curNode[c]

        return self.word_end in curNode

    def startsWith(self, prefix):
        curNode = self.root
        for c in prefix:
            if not c in curNode:
                return False
            curNode = curNode[c]
        return True

    def count(self, node=None):
        # t = json.dumps(self.root)
        # s = r'"\d"'
        # ret = re.findall(s, t)
        # print(len(ret))
        if not node:
            node = self.root

        t = 0
        for k in node.keys():
            t += 1
            if self.word_end not in node[k]:
                t += self.count(node[k])

        return t

# input_data = [
#     '0412578440',
#     '0412199803',
#     '0468892011',
#     '112',
#     '15',
#     '112',
# ]
with open('trie.txt') as file:
    t = file.readlines()
    input_data = sorted([s.strip() for s in t][1:])
obj = Trie()
[obj.insert(s) for s in input_data]
print(obj.count())

# telephones = set()
# # for i in range(int(input())):
# #     s = input();
# for s in input_data:
#     l = [s[0:i+1] for i in range(len(s))]
#     t = set(l)
#     telephones.update(t)
# print(len(telephones))

