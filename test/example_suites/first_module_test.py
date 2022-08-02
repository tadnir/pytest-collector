"""First test module"""


class TestFirstSuite:
    """First test suite"""

    def test_1(self) -> None:
        """First test case"""

        a = """
This is some string that starts without an indent...
"""
        print(a)

    def test_2(self) -> None:
        """
        Second test case.

        :return: Nothing.
        """

        n = [1, 2, 3, 4, 5]
        for m in n:
            print(n)


class TestSecondSuite:
    """
    Second test suite, with some docs:
     * first
     * second
     * third
    """

    def test_3(self) -> None:
        """Some case...."""

        pass

    def test_4(self) -> None:
        """ This is a long line so the text is                                       set to be
Wrapped

        :return: Nothing.
        """

        pass


def test_5() -> None:
    """Case 5, with google doc style.
    Returns:
         Nothing.
    """
    pass


class TestSameNameSuite:
    """
    Something...
    """

    def test_same_name(self) -> None:
        """This has the same name as the test case under second module."""

        pass
