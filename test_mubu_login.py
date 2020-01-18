import requests
import unittest

class TestMubuLogin(unittest.TestCase):

    def test_get_homepage(self):
        url = "https://mubu.com/"
        res = requests.get(url, verify=False)
        # print(res.text)
        assert res.status_code == 200

if __name__ == '__main__':
    pass
