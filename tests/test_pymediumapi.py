import unittest
import pymediumapi
import os
import random
import responses


class TestMediumValidToken(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.token = os.environ.get("MEDIUM_INTEGRATION_TOKEN")
        cls.client = pymediumapi.Client(cls.token)
        return super().setUpClass()

    def test_invalid_token(self):
        c = pymediumapi.Client("")
        self.assertRaises(RuntimeError, c.authenticate)
        self.assertRaises(RuntimeError, c.get_pubblications)

    @responses.activate
    def test_authentication(self):
        """
        Test that the GET request https://api.medium.com/v1/me does not raise
        any exception if the token is valid
        """
        responses.add(
            responses.GET,
            "https://api.medium.com/v1/me",
            json={
                "data": {
                    "id": "a",
                    "username": "b",
                    "name": "c",
                    "url": "d",
                    "imageUrl": "e",
                }
            },
            status=200,
        )
        try:
            resp = self.client.authenticate()
            self.assertTrue("id" in resp)
            self.assertTrue("username" in resp)
            self.assertTrue("name" in resp)
            self.assertTrue("url" in resp)
            self.assertTrue("imageUrl" in resp)
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

    def test_get_contibutors(self):
        """
        Test that the GET request
        https://api.medium.com/v1/publications/{{publicationId}}/contributors
        does not raise any exception
        """
        try:
            self.client.get_contributors("0")
        except Exception as e:
            self.fail("Unexepcted exception: " + str(e))

    def test_create_post(self):
        """
        Test that the POST request
        https://api.medium.com/v1/users/{{authorId}}/posts does not raise
        any exception
        """
        with open("README.md") as f:
            lines = f.readlines()
            content = "".join(lines)

            try:
                self.client.create_post(
                    title="Title" + str(random.randint(0, 100)),
                    content_format="markdown",
                    content=content,
                )
            except Exception as e:
                self.fail("Unexpected exception: " + str(e))


if __name__ == "__main__":
    unittest.main()
