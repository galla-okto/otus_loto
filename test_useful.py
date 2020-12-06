from useful import generate_number_not_used, find_free_place, fill_list_numbers

class TestUsefulGenerateNumberNotUsed:
    def test_return_number(self, list_numbers90, list_numbers_used):
        res = generate_number_not_used(list_numbers90, list_numbers_used)
        assert res in range(1, 21)

    def test_return_type_int(self, list_numbers90, list_numbers_used):
        res = generate_number_not_used(list_numbers90, list_numbers_used)
        assert isinstance(res, int)

class TestUsefulFindFreePlace:
    def test_return_index(self, list_numbers10):
        res = find_free_place(list_numbers10)
        assert res in ([index + 1 for index in range(len(list_numbers10)) if list_numbers10[index] == 0])

    def test_return_type_int(self, list_numbers10):
        res = find_free_place(list_numbers10)
        assert isinstance(res, int)

class TestFillListNumbers:
    def test_return_list_numbers(self, list_numbers90, list_numbers_used):
        res = fill_list_numbers(list_numbers90, list_numbers_used)
        assert len([item for item in res if item != 0]) == 5