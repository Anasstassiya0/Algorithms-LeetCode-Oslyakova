class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        
        for word in strs:
            key = "".join(sorted(word)) # отсортированное слово 
            
            # если нет - создать список
            if key not in hash_map:
                hash_map[key] = []
            
            # добавить слово в группу
            hash_map[key].append(word)
        
        return list(hash_map.values())