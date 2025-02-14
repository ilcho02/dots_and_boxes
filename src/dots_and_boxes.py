class DotsAndBoxes:
    """
    This class handles the internal logic of the game
    """
    def __init__(self, vertical_squares:int, horizontal_squares:int):
        self.n = vertical_squares
        self.m = horizontal_squares

        # 0 represents undrawn edge, 1 is first player and -1 is second player
        self.edges:list[int] = [0 for i in range(self.n * (self.m + 1) + (self.n + 1) * self.m)]
        # 0 represents unocupied box, 1 is ocupied by the first player and -1 is ocupoed by the second player
        self.squares:list[int] = [0 for i in range(self.n * self.m)]
        self.score = [0, 0]
        self.player_turn = 'first'
        
    def get_score(self) -> list[int]:
        """
        returns the score of the game
        """
        return self.score
    
    def is_edge_horizontal(self, edge_index:int) -> bool:
        """
        returns whether the given edge is horisontal or vertical
        """
        return edge_index % (2 * self.m + 1) < self.m
    
    def get_neighbour_squares_indices(self, edge_index:int) -> list[int]:
        """
        returns the indices of the squares that the given edge surrounds
        """
        if self.is_edge_horizontal(edge_index):
            column_index = edge_index % (2 * self.m + 1)
            row_index = edge_index // (2 * self.m + 1)
            result = [(row_index - 1) * self.m + column_index, row_index * self.m + column_index] if row_index != 0 and row_index != self.n else [row_index * self.m + column_index] if row_index == 0 else [(row_index - 1) * self.m + column_index]            
        else:
            column_index = edge_index % (2 * self.m + 1) - self.m
            row_index = edge_index // (2 * self.m + 1)
            result = [row_index * self.m + column_index - 1, row_index * self.m + column_index] if column_index != 0 and column_index != self.m else [row_index * self.m + column_index] if column_index == 0 else [row_index * self.m + column_index - 1]

        return result
    
    def get_surrounding_edges_indices(self, square_index:int) -> list[int]:
        """
        returns the indices of the edges around the given square
        """
        row = square_index // self.m
        column = square_index % self.m
        return [row * (2 * self.m + 1) + column, (row + 1) * (2 * self.m + 1) + column, row * (2 * self.m + 1) + self.m + column, row * (2 * self.m + 1) + self.m + 1 + column]
    
    def get_surrounding_edges(self, square_index:int) -> int:
        """
        returns the number of drawn edges around the given square
        """
        return sum([self.edges[edge] != 0 for edge in self.get_surrounding_edges_indices(square_index)])
    
    def make_move(self, edge:int) -> str:
        """
        Makes the given move without checking
        whether it's valid or not.
        Returns whose player's turn is next
        """
        self.edges[edge] = 1 if self.player_turn == 'first' else -1
        neighbouring_squares = self.get_neighbour_squares_indices(edge)
        are_squares_closed_this_turn = [self.squares[square] == 0 and self.get_surrounding_edges(square) == 4 for square in neighbouring_squares]
        if any(are_squares_closed_this_turn):
            
            if len(neighbouring_squares) == 1:
                self.squares[neighbouring_squares[0]] = self.edges[edge]
                if self.player_turn == 'first':
                    self.score[0] += 1
                else:
                    self.score[1] += 1
            else:
                if are_squares_closed_this_turn[0]:
                    self.squares[neighbouring_squares[0]] = self.edges[edge]
                    if self.player_turn == 'first':
                        self.score[0] += 1
                    else:
                        self.score[1] += 1

                if are_squares_closed_this_turn[1]:
                    self.squares[neighbouring_squares[1]] = self.edges[edge]
                    if self.player_turn == 'first':
                        self.score[0] += 1
                    else:
                        self.score[1] += 1
                
        else:
            self.player_turn = 'second' if self.player_turn == 'first' else 'first'

        return self.player_turn
