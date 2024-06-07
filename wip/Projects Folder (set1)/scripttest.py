import subprocess

# Define the 'ps' command and its arguments
command = ["ps", "aux"]

# Run the command and capture its output
result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

# Print the captured output
print(result.stdout)
# Parse the output into a structured list
lines = result.stdout.splitlines()
keys = lines[0].lower().split()
processes = [dict(zip(keys, line.split(None, len(keys)-1))) for line in lines[1:]]
