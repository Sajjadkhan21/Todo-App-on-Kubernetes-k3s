import os
import json
from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

r = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=int(os.environ.get("REDIS_PORT", "6379")),
    decode_responses=True,
)

@app.route("/api/health")
def health():
    return {"status": "ok"}

@app.route("/api/todos", methods=["GET"])
def list_todos():
    todos = [json.loads(v) for v in r.hvals("todos")]
    todos.sort(key=lambda t: t["id"])
    return jsonify(todos)

@app.route("/api/todos", methods=["POST"])
def add_todo():
    data = request.get_json(force=True)
    title = (data.get("title") or "").strip()
    if not title:
        return {"error": "title required"}, 400
    tid = r.incr("todo:id")
    todo = {"id": tid, "title": title, "done": False}
    r.hset("todos", tid, json.dumps(todo))
    return jsonify(todo), 201

@app.route("/api/todos/<int:tid>", methods=["PUT"])
def toggle_todo(tid):
    raw = r.hget("todos", tid)
    if not raw:
        return {"error": "not found"}, 404
    todo = json.loads(raw)
    todo["done"] = not todo["done"]
    r.hset("todos", tid, json.dumps(todo))
    return jsonify(todo)

@app.route("/api/todos/<int:tid>", methods=["DELETE"])
def delete_todo(tid):
    r.hdel("todos", tid)
    return "", 204
