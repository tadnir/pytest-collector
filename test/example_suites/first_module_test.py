
class TestFirstSuite:
    def test_1(self):
        a = """
This is some string that starts without an indent...
"""
        print(a)

    def test_2(self):
        n = [1, 2, 3, 4, 5]
        for m in n:
            print(n)


class TestSecondSuite:
    def test_3(self):
        pass

    def test_4(self):
        pass


def test_5():
    pass


class TestSameNameSuite:
    def test_same_name(self):
        pass
