import requests

trivia_parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 15
}

trivia_api = requests.get('https://opentdb.com/api.php', params=trivia_parameters)
trivia_api.raise_for_status()

question_data = trivia_api.json()['results']

