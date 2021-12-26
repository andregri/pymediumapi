import unittest
import medium
import os


class TestMediumValidToken(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.token = os.environ.get('MEDIUM_INTEGRATION_TOKEN')
        cls.client = medium.Client(cls.token)
        return super().setUpClass()


    def test_invalid_token(self):
        c = medium.Client('')
        self.assertRaises(RuntimeError, c.authenticate)
        self.assertRaises(RuntimeError, c.get_pubblications)


    def test_authentication(self):
        """
        Test that the GET request https://api.medium.com/v1/me does not raise
        any exception if the token is valid
        """
        try:
            self.client.authenticate()
        except Exception as e:
            self.fail("Unexpected exception:" + str(e))


    def test_get_pubblications(self):
        """
        Test that the GET request
        https://api.medium.com/v1/users/{{userId}}/publications does not raise
        any exception if the user_id is valid
        """
        try:
            self.client.get_pubblications()
        except Exception as e:
            self.fail("Unexpected exception:" + str(e))


if __name__ == '__main__':
    unittest.main()