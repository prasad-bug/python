from datetime import datetime

# Get current date and time
now = datetime.now()

# Format as YYYY-MM-DD HH:MM:SS
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time: {formatted}")
