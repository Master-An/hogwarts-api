import requests

def test_get_homepage():
    url = "https://mubu.com/"
    res = requests.get(url, verify=False)
    # print(res.text)
    assert res.status_code == 200

if __name__ == '__main__':
    test_get_homepage()