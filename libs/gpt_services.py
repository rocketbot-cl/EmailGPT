import requests
from gpt_consts import URL


def get_tasks(api_key: str, url: str):
    headers = {"Authorization": f"Bearer {api_key}"}

    return requests.get(f"{url}/api/tasks", headers=headers)


def get_task(api_key: str, id: str, url: str):
    headers = {"Authorization": f"Bearer {api_key}"}

    return requests.get(f"{url}/api/tasks/{id}/results", headers=headers)


def connect(api_key: str, url: str):
    headers = {"Authorization": f"Bearer {api_key}"}

    return requests.post(f"{url}/api/connect", headers=headers)
