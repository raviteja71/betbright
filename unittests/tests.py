# unit tests for the /brands endpoint
#command: nosetests /home/raviteja/Downloads/betBright/unittests/tests.py
from flask import Flask
import unittest
import requests
import os
import json
import sys

# tells sql_models to use the testing database
os.environ['API_TESTING'] = '1'
sys.path.append('/')

app = Flask(__name__)

class TestMatchesEndpoint(unittest.TestCase):

    def test_match(self):
        """
        get matches related to provided id
        - sets the brand's 'offers_running' status
        - returns serialized match data like so: {id:match_id,..etc}
        - test status code + name, id fields are not null
        """
        result = requests.get('http://localhost:5000/api/match/1')
        data = json.loads(result.content)
        self.assertEqual(result.status_code, 200)
        self.assertIsNotNone(data["name"])
        self.assertIsNotNone(data["id"])
    def test_matchbyname(self):
        """
        get matches related to provided id
        - sets the brand's 'offers_running' status
        - returns serialized match data like so: {id:match_id,..etc}
        - test status code + name, id fields are not null
        """
        result = requests.get('http://localhost:5000/api/match/name=Poland%20vs%20Irland')
        data = json.loads(result.content)
        self.assertEqual(result.status_code, 200)
        self.assertIsNotNone(data["name"])
        self.assertIsNotNone(data["id"])
    def test_matchbysport(self):
        """
        get matches related to provided id
        - sets the brand's 'offers_running' status
        - returns serialized match data like so: {id:match_id,..etc}
        - test status code + name, id fields are not null
        """
        result = requests.get('http://localhost:5000/api/match/sport=football/ordering=start_time')
        data = json.loads(result.content)
        self.assertEqual(result.status_code, 200)
        self.assertIsNotNone(data["results"])


if __name__ == '__main__':
    unittest.main()