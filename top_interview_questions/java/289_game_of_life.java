class Solution {
    public void gameOfLife(int[][] board) {
        int rows =  board.length;
        int columns = board[0].length;

        int[][] neighbors = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}, {1, 1}, {-1, -1}, {-1, 1}, {1, -1}};

        for (int row = 0; row < rows; row++) {
            for (int column = 0; column < columns; column++) {
                int live_neighbors = 0;
                for (int[] neighbor: neighbors) {
                    int r = row + neighbor[0];
                    int c = column + neighbor[1];
                    if (r >= 0 && r < rows && c >= 0 && c < columns && Math.abs(board[r][c]) == 1)
                        live_neighbors += 1;
                }
                if (board[row][column] == 1 && (live_neighbors < 2 || live_neighbors > 3))
                    board[row][column] = -1;
                if (board[row][column] == 0 && live_neighbors == 3)
                    board[row][column] = 2;
            }
        }

        for (int row = 0; row < rows; row++)
            for (int column = 0; column < columns; column++) {
                if (board[row][column] == -1)
                    board[row][column] = 0;
                if (board[row][column] == 2)
                    board[row][column] = 1;
            }
    }
}