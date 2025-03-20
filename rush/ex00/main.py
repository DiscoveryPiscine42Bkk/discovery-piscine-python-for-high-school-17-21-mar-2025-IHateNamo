#!/usr/bin/env python3

from checkmate import checkmate

def main():
    board = [
        "----------",
        "|........|",
        "|........|",
        "|........|",
        "|........|",
        "|....K...|",
        "|.....K..|",
        "|........|",
        "|........|",
        "----------"
    ]

    for kyunig in board: #print a board
        print(kyunig)



    checkmate(board)  

if __name__ == "__main__":
    main()
