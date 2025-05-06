'''def numberofmoves(numofdiscs):
    listofnumbers = [1]
    while listofnumbers[-1] < 2**numofdiscs -1:
        listofnumbers.append(listofnumbers[-1] + 1)
    return listofnumbers'''

def numberofmoves(numofdiscs):
    return 2**numofdiscs - 1


def discpattern(numofdiscs):
    total_moves = numberofmoves(numofdiscs)
    print(f'With {numofdiscs} discs given, you require {total_moves} moves')


    for move in range(1, total_moves + 1): # Move
        for disc in range(1, numofdiscs + 1): # Discs
            if (move - 2**(disc-1)) % (2**disc) == 0:
                if numofdiscs % 2 == 1: 
                    peg_sequence = ['A', 'C', 'B']
                else:     
                    peg_sequence = ['A','B','C']

                '''if disc == 1:
                    print(peg_sequence[move])
                else:
                    print(peg_sequence[move])'''
                    
                from_peg = peg_sequence[(((move - disc)//(2**disc))%3)+1]
                to_peg = peg_sequence[((move - disc)//(2**disc))%(3)]
                print(f'{move}. Move disc {disc} from {from_peg} to {to_peg}')
                break
discpattern(int(input("WELCOME TO THE TOWER OF HANOI! YOU MAY GIvE US YOUR NUMBER OF DISCS, AND WE SHALL TELL YOU HOW TO SOLVE IT: ")))


