`
@author: Fizz Cao 
@file: 289_game_of_life.py
@time: 5/10/2021 12:12 am
`
/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife = function(board) {
    let rows =  board.length;
    let columns = board[0].length;

    neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]];

    for (let row = 0; row < rows; row++) {
        for (let column = 0; column < columns; column++) {
            let live_neighbors = 0;
            for (neighbor of neighbors) {
                let r = row + neighbor[0];
                let c = column + neighbor[1];
                if (r >= 0 && r < rows && c >= 0 && c < columns && Math.abs(board[r][c]) == 1)
                    live_neighbors += 1;
            }
            if (board[row][column] == 1 && (live_neighbors < 2 || live_neighbors > 3))
                board[row][column] = -1;
            if (board[row][column] == 0 && live_neighbors == 3)
                board[row][column] = 2;
        }
    }

    for (let row = 0; row < rows; row++)
        for (let column = 0; column < columns; column++) {
            if (board[row][column] == -1)
                board[row][column] = 0;
            if (board[row][column] == 2)
                board[row][column] = 1;
        }
};