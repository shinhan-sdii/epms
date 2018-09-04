"""
Example written for Qxf2 Services' blog post on Python Unit Checking
Check if IsCheckmate method in ChessRules class calls GetListOfValidMoves  
Assert that it called with the expected arguments
URL : https://qxf2.com/blog/python-unit-checks/
"""
import unittest, mock
import ChessRules 
from ChessBoard import ChessBoard

# hello world
class CheckIsCheckmate(unittest.TestCase):
    "Class to unit check the IsCheckmate method of ChessRules.py module"
    # creating a mock for GetListOfValidMoves
    @mock.patch('ChessRules.ChessRules.GetListOfValidMoves')        
    def test_Checkmate(self, mockGetListOfValidMoves):
        "Unit test for ChessRules method: IsCheckmate"
        # NOTE 1: We only check that there are valid moves for a given color
        # NOTE 2: We are NOT checking the setting color logic in this unit test. You need to write another unit test for this logic.

        # Creating objects of Chessboard and ChessRules class and calling IsCheckmate function with each piece for initial position and "black" color
        cb = ChessBoard(0) #Create a chess board object with the initial position
        chess_rules_obj = ChessRules.ChessRules()
        chess_rules_obj.IsCheckmate(cb.GetState(),"black")

        # Create expected_arg_calls list which is supposed to be called with GetListOfValidMoves for initial position
        # IsCheckmate calls GetListOfValidMoves with arguments: board, color (who is to play?) and co-ordinates of a square with a piece on it
        expected_arg_calls = []
        for row in range(0,2):
            for col in range(0,8):
                expected_arg_calls.append(mock.call(cb.GetState(), 'black', (row, col)))

        # Assert that the mockGetListOfValidMoves.call_args_list matches expected_arg_calls
        self.assertEqual(mockGetListOfValidMoves.call_args_list, expected_arg_calls)

        # assert that method was called at least once with some argument        
        mockGetListOfValidMoves.assert_any_call(cb.GetState(),"black",(1,6))

        # check the number of times your mocked method was called
        self.assertEqual(mockGetListOfValidMoves.call_count,16)

        # DID YOU KNOW?
        # assert_any_call can be used to assert a method that was called at least once with some arguments        
        #mockGetListOfValidMoves.assert_any_call(cb.GetState(),"black",(1,6))

        # DID YOU KNOW?
        # call_count can be used to check the number of times your mocked method was called
        #self.assertEqual(mockGetListOfValidMoves.call_count,16)


if __name__=="__main__":
    unittest.main()