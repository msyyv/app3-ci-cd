import unittest

from urllib import response

from rakesh2 import app


class FlaskAppTest(unittest.TestCase):
    def test_home_status_code(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_status_code1(self):
        """Assert that user successfully lands on homepage"""
        tester = app.test_client(self)
        response = tester.get("/rkfdgs")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
