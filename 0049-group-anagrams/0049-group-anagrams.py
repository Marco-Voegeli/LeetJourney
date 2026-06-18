class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def heatmap(x):
            heatmap = {}
            for c in x:
                if c in heatmap:
                    heatmap[c] += 1
                else:
                    heatmap[c] = 1
            return heatmap
        def compare_heatmap(h1, h2):
            if not h1 and h2:
                return False
            if len(h1) != len(h2):
                return False
            for (key, val) in h1.items():
                if key not in h2:
                    return False
                if h2[key] != val:
                    return False
            return True
        strs_with_heatmap = [(heatmap(x), x) for x in strs]
        print(strs_with_heatmap)
        result = []
        for (heatmap, string) in strs_with_heatmap:
            added = False
            if not result:
                result.append((heatmap, [string]))
                continue
            for (heatmap_base, str_ls) in result:
                if compare_heatmap(heatmap_base, heatmap):
                    str_ls.append(string)
                    added = True
            if not added:
                result.append((heatmap, [string]))
        return [x[1] for x in result]
