import os

db_user = os.getenv('DB_USER', 'default_user')
db_password = os.getenv('DB_PASSWORD', 'default_password')

print(f"Database User: {db_user}")
print(f"Database User: {db_password}")

os.environ['DB_USER'] = 'admin'
os.environ['DB_PASSWORD'] = 's3cr3t'

