"""You have n  tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: tiles = "AAABBC"
Output: 188

Example 3:
Input: tiles = "V"
Output: 1"""

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        seen=set()
        def backtrack(path,remaining_tiles):
            if path:
                seen.add(path)
            for i in range(len(remaining_tiles)):
                if i>0 and remaining_tiles[i-1]==remaining_tiles[i]:
                    continue
                backtrack(path+remaining_tiles[i],remaining_tiles[:i]+remaining_tiles[i+1:])
        tiles=sorted(tiles)
        backtrack("",tiles)
        return len(seen)

