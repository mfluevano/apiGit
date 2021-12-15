#Unit test for the MpyGitApi class
#Author: @mfluevano
# Usage: !python -m unittest test_MpyGitApi.py
import unittest
import requests

class TestMpyGitApi(unittest.TestCase):
    def test_get_user_info(self):
        api = MpyGitApi()
        user = api.get_user_info('mpycoder')
        self.assertEqual(user.login, 'mpycoder')
        self.assertEqual(user.id, '1234')
        self.assertEqual(user.avatar_url, 'https://avatars.githubusercontent.com/u/1234?v=3')
        self.assertEqual(user.html_url, '
