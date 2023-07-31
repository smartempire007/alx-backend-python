#!/usr/bin/env python3
'''Unittests and Integration tests module'''

import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock, Mock
from utils import (
    access_nested_map,
    get_json,
    memoize
)


class TestAccessNestedMap(unittest.TestCase):
    '''TestAccessNestedMap class'''

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''test_access_nested_map method'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        '''test_access_nested_map_exception method'''
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''TestGetJson class'''

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    def test_get_json(self, test_url, test_payload):
        '''test_get_json method'''
        mock = Mock()
        mock.json.return_value = test_payload
        with patch('requests.get', return_value=mock):
            self.assertEqual(get_json(test_url), test_payload)
            mock.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    '''TestMemoize class'''

    def test_memoize(self):
        '''test_memoize method'''
        class TestClass:
            '''TestClass class'''

            def a_method(self):
                '''a_method method'''
                return 42

            @memoize
            def a_property(self):
                '''a_property method'''
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test = TestClass()
            test.a_property
            test.a_property
            mock.assert_called_once()
