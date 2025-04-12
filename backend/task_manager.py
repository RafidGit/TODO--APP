import psycopg2

class TaskManager:
    def __init__(self, db_config):
        self.db_config = db_config

    def connect(self):
        return psycopg2.connect(**self.db_config)

    def get_all_tasks(self):
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM tasks;")
                return cur.fetchall()

    def add_task(self, task_name, status='pending'):
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO tasks (task_name, status) VALUES (%s, %s);", (task_name, status))
                conn.commit()

    def update_task_status(self, task_id, status):
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE tasks SET status = %s WHERE id = %s;", (status, task_id))
                conn.commit()

    def delete_task(self, task_id):
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM tasks WHERE id = %s;", (task_id,))
                conn.commit()
