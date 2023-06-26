import subprocess
import os

# Define the command to publish a message
command = [
    "mosquitto_pub",
    "-h", "127.0.0.1",
    "-p", "1221",
    "--cafile", "/etc/mosquitto/certs/certificate.pem",
    "--cert", "/etc/mosquitto/certs/certificate.pem",
    "--key", "/etc/mosquitto/certs/key.pem",
    "-t", "test",
    "-m", "Salvi Kigali Rwanda",
    "-q", "2",
    "-r"  # Add the retain option to retain the Last Will message
]

# Publish the message
try:
    subprocess.run(command, check=True)
    print("Success")
    success = True
except subprocess.CalledProcessError:
    print("Error occurred.")
    success = False

# Read and print the log file if successful
if success:
    log_file = "/var/log/mosquitto/mosquitto1.log"
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            # Tail the last few lines of the log file
            lines = f.readlines()
            last_lines = lines[-5:]  # Adjust the number of lines to display as needed
            print("Log file contents:")
            print("".join(last_lines))
    else:
        print("Log file not found.")
