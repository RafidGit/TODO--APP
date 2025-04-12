from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase_client import supabase

app = Flask(__name__)
CORS(app)

# Fetch all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    response = supabase.table("tasks").select("*").execute()
    return jsonify(response.data), 200

# Add a task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task_name = data.get('task_name', '')
    response = supabase.table("tasks").insert({"task_name": task_name}).execute()
    return jsonify(response.data), 201

# Update task status
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    response = supabase.table("tasks").update({"status": True}).eq("id", task_id).execute()
    return jsonify(response.data), 200

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    response = supabase.table("tasks").delete().eq("id", task_id).execute()
    return jsonify(response.data), 200

if __name__ == '__main__':
    app.run(debug=True)
