class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq_dict = {}

        for word in words:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        heap = []
        for key, value in freq_dict.items():
            heappush_max(heap, (value, key))

        solution = []
        lex_heap = []


        previous_f, word = heappop_max(heap)
        heappush(lex_heap, word)

        while len(heap):
            f, word = heappop_max(heap)
            
            if previous_f != f:
                while lex_heap and (sol_word := heappop(lex_heap)):
                    solution.append(sol_word)
                
                if len(solution) >= k:
                    return solution[:k]

            previous_f = f
            heappush(lex_heap, word)

        while lex_heap and (sol_word := heappop(lex_heap)):
            solution.append(sol_word)                
            
        return solution[:k]
