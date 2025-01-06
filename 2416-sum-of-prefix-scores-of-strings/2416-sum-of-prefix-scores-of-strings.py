class Node:
    def __init__(self, counter):
        self.last_char = False
        self.children = {}
        self.counter = counter
class Trie:
    def __init__(self):
        self.root = Node(counter = 0)
    
    def insert(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:    
                cur.children[c] = Node(counter = 1)
            else:
                cur.children[c].counter += 1
            cur = cur.children[c]
        cur.last_char = True

    def score(self, word: str):
        cur = self.root
        res = 0
        for c in word:
            if c not in cur.children:
                print("Word not exist")
                return 0
            else:
                res += cur.children[c].counter
                cur = cur.children[c]
        return res
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        print(trie.root.children)
        res = []
        for word in words:
            res.append(trie.score(word))
        return res
    def sumPrefixScores_1(self, words: List[str]) -> List[int]:
        prefix_seen = {}
        def score_cal(prefix, words):
            if prefix in prefix_seen:
                return prefix_seen[prefix]
            prefix_score = sum([prefix == word[:len(prefix)] for word in words])
            prefix_seen[prefix] = prefix_score
            return prefix_score
        res_scores = [0]*len(words)
        for j, word in enumerate(words):
            prefixes = 1
            prefixes = [word[:i+1] for i in range(len(word))]
            for prefix in prefixes:
                res_scores[j] += score_cal(prefix, words)
        return res_scores