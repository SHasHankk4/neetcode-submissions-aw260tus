class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        def flood(row,column,original_color):
            if not (0<=row<len(image)) or not (0<=column<len(image[0])) or image[row][column]!=original_color:
                return None
            image[row][column]=color
            flood(row-1,column,original_color)
            flood(row+1,column,original_color)
            flood(row,column-1,original_color)
            flood(row,column+1,original_color)
        flood(sr,sc,image[sr][sc])
        return image
        