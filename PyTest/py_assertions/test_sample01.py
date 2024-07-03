import pytest
import ArthimeticOperations



class TestCases:

    def test_tc1(self):
        print("Test Case 1")
        assert 5+5==ArthimeticOperations.add2numbers(5,5)
        assert 6-5==ArthimeticOperations.subtract2numbers(6,5)
        assert 8/4==ArthimeticOperations.divide2numbers(8,4)
        assert 10*6==ArthimeticOperations.multiply2numbers(10,5)

    def test_tc2(self):
        with pytest.raises(Exception):
            assert 5-5==ArthimeticOperations.add2numbers(5,5), "given assertion is not valid"

    @pytest.mark.skipif(ArthimeticOperations.divide2numbers(8,4)==2, reason="Skipping based on condition")
    def test_tc3(self):
        with pytest.raises(Exception) as exe:
            assert 9/5==1, "given assertion is not valid"
        print(str(exe))

    def test_tc4(self):
        assert 9//5==ArthimeticOperations.truncationdivision(9,5), "given assertion is not valid"

    @pytest.mark.skip(reason="Skipping the test case")
    def test_tc5(self):
        val = ArthimeticOperations.getremainderquotient(9,5)
        assert val[0]==1
        assert val[1]==4
        assert 1 in val
        assert 4 not in val
        raise ValueError("Exception occoured")

    def test_tc6(self):
        assert 1 in [1,2,3]
        assert [1,2] in [1,2,3]

