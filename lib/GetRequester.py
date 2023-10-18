import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url
        url = " https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        people_list = []
        people = json.loads(GetRequester.get_response_body(self))

        return people