from gpt_services import connect, get_task, get_tasks


class EmailGPT:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_tasks_list(self) -> list[str]:
        res = get_tasks(self.api_key)
        if res.ok:
            tasks = res.json().get("data", [])
            return [task["uuid"] for task in tasks]
        return []

    def get_task_result(self, uuid: str) -> dict | bool:
        res = get_tasks(self.api_key)
        if res.ok:
            tasks: list[dict] = res.json().get("data", [])
            task = list(filter(lambda task: task["uuid"] == uuid, tasks))[0]

            return task
        return False

    def connect(self) -> bool:
        res = connect(self.api_key)
        if res.ok:
            return res.json().get("status", False)
        return False
