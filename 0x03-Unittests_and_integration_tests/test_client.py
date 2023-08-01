#!/usr/bin/env python3
'''Unittests and Integration tests module'''

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''TestGithubOrgClient class'''

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, test_org_name, mock_get_json):
        '''test_org method'''
        test_class = GithubOrgClient(test_org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/{}'.format(test_org_name))

    def test_public_repos_url(self):
        '''test_public_repos_url method'''
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url': 'test_url'}
            test_class = GithubOrgClient('test_org')
            self.assertEqual(test_class._public_repos_url, 'test_url')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        '''test_public_repos method'''
        mock_get_json.return_value = [{'name': 'test_repo', 'license': {
            'key': 'my_license'}}]
        with patch.object(GithubOrgClient, 'repos_payload',
                          new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = [{'name': 'test_repo'}]
            test_class = GithubOrgClient('test_org')
            self.assertEqual(test_class.public_repos(), ['test_repo'])
            self.assertEqual(test_class.public_repos('my_license'),
                             ['test_repo'])
            self.assertEqual(test_class.public_repos('other_license'), [])

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license_key, expected):
        '''test_has_license method'''
        test_class = GithubOrgClient('test_org')
        self.assertEqual(test_class.has_license(repo, license_key), expected)


@parameterized_class(['org_payload', 'repos_payload', 'expected_repos',
                      'apache2_repos'], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''TestIntegrationGithubOrgClient class'''

    @classmethod
    def setUpClass(cls):
        '''setUpClass method'''
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)

        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        '''tearDownClass method'''
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''test_public_repos method'''
        test_class = GithubOrgClient('test')
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos('test'), [])
        self.mock_get.assert_called()

    def test_public_repos_with_license(self):
        '''test_public_repos_with_license method'''
        test_class = GithubOrgClient('test')
        self.assertEqual(test_class.public_repos(
            'apache-2.0'), self.apache2_repos)
        self.assertEqual(test_class.public_repos('mit'), [])


if __name__ == '__main__':
    unittest.main()
