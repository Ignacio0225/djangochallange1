from encodings import search_function

from django.test import TestCase

from rest_framework.test import APITestCase
from .models import Tweet
from users.models import User
# Create your tests here.

class TestTweets(APITestCase):


    NAME = "testname"
    PAYLOAD = "testpayload"
    USER = "testuser"
    URL = "/api/v1/tweets/"

    def setUp(self):
        user = User.objects.create_user(username=self.USER, password="testpassword")

        Tweet.objects.create(
            name=self.NAME,
            payload=self.PAYLOAD,
            user=user,
        )
    def test_all_tweets(self):
        response=self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "ok")

        self.assertIsInstance(data,list)

        self.assertEqual(len(data),1)

        self.assertEqual(
            data[0]["name"],
            self.NAME
        )
        self.assertEqual(
            data[0]["payload"],
            self.PAYLOAD
        )
        self.assertEqual(
            data[0]["user"],
            self.USER
        )

    def test_create_tweets(self):

        self.client.login(username = self.USER,password = "testpassword")

        new_tweet_name = "Max_10_str"
        new_tweet_payload = "New Tweet Payload"

        response = self.client.post(
            self.URL,
            data = {
                'name':new_tweet_name,
                'payload':new_tweet_payload,
            },
        )
        data = response.json()

        self.assertEqual(response.status_code,200,"Not 200 Found")
        self.assertIsInstance(data,dict)


class TestTweet(APITestCase):

    NAME = "testname"
    PAYLOAD = "testpayload"
    USER = "testuser"

    def setUp(self):

        user = User.objects.create_user(username=self.USER, password="testpassword")
        Tweet.objects.create(
            name=self.NAME,
            payload=self.PAYLOAD,
            user=user
        )

    def test_notfound_tweet(self):
        response = self.client.get("/api/v1/tweets/2")
        self.assertEqual(response.status_code,404,"Not 200 Found")

    def test_get_tweet(self):
        response = self.client.get("/api/v1/tweets/1")
        self.assertEqual(response.status_code, 200, "Not 200 Found")

    def test_put_tweet(self):
        self.client.login(username=self.USER,password= "testpassword")
        new_name="newname"
        new_payload="newpl"
        response = self.client.put(
            "/api/v1/tweets/1",
            data={
                "name":new_name,"payload":new_payload,
            }
        )
        data = response.json()

        self.assertEqual(response.status_code,200,"Not 200 Found")
        self.assertIsInstance(data,dict)
        self.assertEqual(data['name'],new_name)
        self.assertEqual(data['payload'],new_payload)
        self.assertEqual(data['user'],self.USER)

    def test_delete_tweet(self):
        self.client.login(username=self.USER, password="testpassword")
        response = self.client.delete("/api/v1/tweets/1")
        self.assertEqual(response.status_code,204,"Not 204")