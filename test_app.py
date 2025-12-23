import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_hello_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        # Ключевое исправление: декодируем байты в строку
        self.assertIn('Привет', response.data.decode())

if __name__ == '__main__':
    unittest.main()
