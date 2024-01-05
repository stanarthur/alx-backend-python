import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Tuple, Dict, Union


class TestAccessNestedMap(unittest.TestCase):
    """To Test access nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple,
            expected_answer: Union[int, Dict],
            ) -> None:
        """This tests access_nested_map output"""
        self.assertEqual(access_nested_map(nested_map, path), expected_answer)


if __name__ == '__main__':
    unittest.main()