#!/usr/bin/env python3

from checkmate import checkmate

def main():
    board = [
        "----------",
        "|........|",
        "|........|",
        "|........|",
        "|........|",
        "|........|",
        "|........|",
        "|....B...|",
        "|.....K..|",
        "----------"
    ]

    for kyunig in board: #print a board
        print(kyunig)



    checkmate(board)  

if __name__ == "__main__":
    main()
