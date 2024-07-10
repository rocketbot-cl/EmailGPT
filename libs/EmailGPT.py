from gpt_services import connect, get_task, get_tasks
from gpt_consts import URL

class EmailGPT:
    def __init__(self, api_key, url):
        self.api_key = api_key
        self.url_server = URL.get(url)

    def get_tasks_list(self) -> list[str]:
        res = get_tasks(self.api_key, self.url_server)
        if res.ok:
            tasks = res.json().get("data", [])
            return [task["uuid"] for task in tasks]
        return []

    def get_task_results(self, uuid: str) -> list[dict] | bool:
        res = get_tasks(self.api_key, self.url_server)
        if res.ok:
            tasks: list[dict] = res.json().get("data", [])
            if len(tasks) == 0:
                return []

            task = list(filter(lambda task: task["uuid"] == uuid, tasks))[0]

            task_res = get_task(self.api_key, task["id"], self.url_server)

            if task_res.ok:
                task_data = task_res.json().get("data", {})
                task_results = task_data.get("task_results", [])
                task_results_data = [
                    {
                        "id": result["id"],
                        "result": result["result"],
                        "attacheds": result["attacheds"],
                        "length": result["length"],
                    }
                    for result in task_results
                ]

                return task_results_data
            return False
        return False

    def connect(self) -> bool:
        res = connect(self.api_key, self.url_server)
        if res.ok:
            return res.json().get("status", False)
        return False
