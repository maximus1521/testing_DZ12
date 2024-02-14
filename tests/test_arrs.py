from utils import arrs


def test_get():
    assert arrs.get([1, 3, 3], 1, "test") == 3
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([4, 6, 6], 1, "test") == 6
    assert arrs.get([1, 2, 3, 4], 4, "test") == "test"
    assert arrs.get([1, 2, 3, 4], 0, "test") == 1


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -1, 2) == []
    assert arrs.my_slice([1, 2, 3, 4], 0, 4) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4], None, 4) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4], 1, 5) == [2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4],1, None) == [2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4], 0, 5) == [1, 2, 3, 4]
    assert arrs.my_slice([], 0, 0) == []