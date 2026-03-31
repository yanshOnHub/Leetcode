class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # If there's only one row or the string is too short, return it directly
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list for each row
        rows = [''] * numRows
        current_row = 0
        direction = -1  # Will flip between +1 (down) and -1 (up)

        # Traverse each character
        for char in s:
            rows[current_row] += char
            # Change direction at the top or bottom
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
            current_row += direction

        # Join all rows to get the final zigzag string
        return ''.join(rows)

        