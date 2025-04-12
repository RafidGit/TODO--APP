from supabase import create_client, Client

# Initialize Supabase client
url = "https://erkfsnxxomewxvjqvbhb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVya2Zzbnh4b21ld3h2anF2YmhiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQzNDg4MTMsImV4cCI6MjA1OTkyNDgxM30.4jZa07M0bDP3MmVVkDAqItBvuF0qzEWxtgOQKjCdZtc"
supabase = create_client(url, key)

def insert_task(task_name, status=False):
    task_data = {
        "task_name": task_name,
        "status": status
    }
    response = supabase.table('tasks').insert(task_data).execute()
    print(f"Inserted task response: {response}")
    return response
