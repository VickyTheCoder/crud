import requests
import unittest

class TestPersonCreate(unittest.TestCase):
    def setUp(self):
        self.client = requests.session()
        self.client.get('http://127.0.0.1:8000/html/add')
        self.csrftoken = self.client.cookies['csrftoken']
    def test_new_insert(self):
        adr = 123
        create_url = 'http://127.0.0.1:8000/add/save'
        del_url = 'http://127.0.0.1:8000/html/delete'
        read_url = 'http://127.0.0.1:8000/html/read'
        dele = self.client.post(url=del_url, 
                                data={'aadhar': adr,
                                 'csrfmiddlewaretoken': self.csrftoken
                                 })
        if dele.text == f"Contact({adr}) deleted":
            print(f"Deleted the existing record for {adr}")
        excepted = {
            'aadhar': adr,
            'name': 'somu',
            'dob': '1987-11-11',
            'email': 'somu@gmail.com',
            'mobile': '9745932745',
            'dp_pic': 'somu.jpg',
            'csrfmiddlewaretoken': self.csrftoken,
        }
        res2 = self.client.post(url=create_url, data=excepted)
        # checks the response to the browser/client
        self.assertEqual(res2.text, 'Inserted')
        res3 = self.client.post(url=read_url,
                                data={
                                    'aadhar': adr,
                                 'csrfmiddlewaretoken': self.csrftoken
                                 })
        text_res = res3.text
        status = f'aadhar: {adr}' in text_res
        status = status and f'name: {excepted.get('name')}' in text_res
        status = status and f'DOB: {excepted.get('dob')}' in text_res
        status = status and f'email: {excepted.get('email')}' in text_res
        status = status and f'mobile: {excepted.get('mobile')}' in text_res
        status = status and f'dp pic: {excepted.get('dp_pic')}' in text_res
        # print(text_res, 555555555)
        status = bool(status)
        # checks if the values are correctly updated in DB
        self.assertEqual(status, True)

unittest.main(verbosity=3)
