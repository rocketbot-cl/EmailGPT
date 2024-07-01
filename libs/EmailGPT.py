from gpt_services import connect, get_task, get_tasks


class EmailGPT:
    def __init__(self, api_key):
        self.api_key = api_key

    def validate_api_key(self) -> bool:
        res = get_tasks(self.api_key)
        return res.ok

    def get_tasks_list(self) -> list[str]:
        res = get_tasks(self.api_key)
        if res.ok:
            tasks = res.json().get("data", [])
            return [task["uuid"] for task in tasks]
        return []

    def get_task_result(self, uuid: str) -> dict | None:
        res = get_task(self.api_key, uuid)
        if res.ok:
            return res.json().get("data", None)
        return None

    def connect(self) -> bool:
        res = connect(self.api_key)
        if res.ok:
            return res.json().get("status", False)
        return False
