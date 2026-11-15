
class Solution:
    def floodFill(self, image, sr, sc, color):

        original = image[sr][sc]

        # If both colors are same, no changes needed
        if original == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):

            # Change the current pixel
            image[r][c] = color

            # Four directions: up, down, left, right
            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Check boundaries and original color
                if (0 <= nr < rows and
                    0 <= nc < cols and
                    image[nr][nc] == original):

                    dfs(nr, nc)

        dfs(sr, sc)

        return image
