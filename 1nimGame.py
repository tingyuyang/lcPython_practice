"""
You are playing the following Nim Game with your friend: 
There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. 
The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. 
Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, 
then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.
"""
# i forgot the case when the stone # is < 4! need to be more careful
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # ture is i win the game
        left = n-1
        var = False
        if (n < 4):# if the stone is 1,2,3, i win
            var = True
        else:
            if (n % 4 != 0): # if n != 4*x, then i win 
                var = True
        return var
 # my solution is partially guessing. if the stone number is 4, 8, 12.... i will not win for sure.
"""
how to print appropriate on repl:

"a = Solution()"
=>None
"print a.canWinNim(5)"
True
=>None
"""
