

def numberofmoves(numofdiscs):
    return 2**numofdiscs - 1

def discpattern(numofdiscs):
    total_moves = numberofmoves(numofdiscs)
    print(f'With {numofdiscs} discs given, you require {total_moves} moves')

    # Set peg order depending on parity
    if numofdiscs % 2 == 1:
        peg_sequence = ['A', 'C', 'B']
    else:
        peg_sequence = ['A', 'B', 'C']

    for move in range(1, total_moves + 1):
        for disc in range(1, numofdiscs + 1):
            if (move - 2**(disc-1)) % (2**disc) == 0:
                # Determine direction of disc rotation
                direction = ((move - 1) // (2**(disc))) % 3
                from_peg = peg_sequence[direction]
                to_peg = peg_sequence[(direction + 1) % 3]
                print(f'{move}. Move disc {disc} from {from_peg} to {to_peg}')
                break

discpattern(int(input("WELCOME TO THE TOWER OF HANOI! YOU MAY GIvE US YOUR NUMBER OF DISCS, AND WE SHALL TELL YOU HOW TO SOLVE IT: ")))