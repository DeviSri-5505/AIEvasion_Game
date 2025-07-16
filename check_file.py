import os

# Check if the file exists
file_exists = os.path.exists("background.jpg")
print(f"Does 'background.jpg' exist in current directory? {file_exists}")

# List all files in the current directory (to see what Python sees)
print("\nFiles in current directory:")
for item in os.listdir('.'):
    print(item)