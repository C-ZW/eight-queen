# Eight problem

## Eight problem variant

    Given 
    1. Board with height and width
    2. Queen attack range
    
    Goal:
    Find maximum number of queens can be placed on board    


## Implement alogorithm

1. Use set as board data structrue
2. Random choice on board represent queen position
3. Calculate influence position as another set
4. Use set difference
5. go back 2 util size of board is equal to 0
6. Output how many iteration between step 2 to 5(one iteration choice one queen)
