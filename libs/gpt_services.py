import requests
from gpt_consts import URL


def get_tasks(api_key: str):
    headers = {"Authorization": f"Bearer {api_key}"}

    return requests.get(f"{URL}/api/tasks", headers=headers)


def get_task(api_key: str, id: str):
    headers = {"Authorization": f"Bearer {api_key}"}

    return requests.get(f"{URL}/api/tasks/{id}/results", headers=headers)


def connect(api_key: str):
    headers = {"Authorization": f"Bearer {api_key}"}

    return requests.post(f"{URL}/api/connect", headers=headers)
