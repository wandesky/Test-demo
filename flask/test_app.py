from app import app
import unittest
import json

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {"username":"john", "email":"email@gmail.com","password":"12345"}
       

    def test_login(self):
        response = self.app.get('/api/v1/login')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "You are logged in")
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.app.post('/api/v1/register', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["username"], "john")
        self.assertEqual(result["email"], "email@gmail.com")
        self.assertEqual(result["password"], "12345")
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()