class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq_dict = {}

        for word in words:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        heap = []
        for word in freq_dict:
            if len(heap) < k:
                heappush_max(heap, (-freq_dict[word], word))
            elif freq_dict[word] > -heap[0][0]:
                heappushpop_max(heap, (-freq_dict[word], word))
            elif freq_dict[word] == -heap[0][0] and word < heap[0][1] :
                heappushpop_max(heap, (-freq_dict[word], word))
        sol = []
        while len(sol) < k:
            sol.append(heappop_max(heap)[1])
        sol.reverse()
        return sol

