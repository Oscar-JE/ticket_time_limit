import unittest
import os
class Learning(unittest.TestCase):

    def test_getTerminalSize(self):
        print(os.get_terminal_size())

    @unittest.skip("undersöker inte detta just nu")
    def test_Terminal_hight(self):
        for i in range(0,20):
            print(i)



if __name__ == "__main__":
    unittest.main()
