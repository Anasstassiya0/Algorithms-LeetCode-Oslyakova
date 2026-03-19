class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = {}

        for character in s:
            count[character] = count.get(character, 0) + 1

        for character in t:

            if character not in count:
                return False

            count[character] -= 1

        return all(v == 0 for v in count.values())

