import redis, json
r = redis.Redis(host='redis', port=6379, decode_responses=True)
class StateManager:
    async def set(self, task_id, key, value):
        r.set(f"{task_id}:{key}", json.dumps(value))
    async def get(self, task_id, key):
        data = r.get(f"{task_id}:{key}")
        return json.loads(data) if data else None
state_manager = StateManager()
