# Bus Times Fetcher with Storstockholms Lokaltrafik (SL) API and Raspberry PI
This project provides a simple Python script to fetch real-time bus departure information from the Trafiklab SL Transport API (for Stockholm Public Transport) and a systemd setup to run it periodically on a Raspberry Pi.

## 🚀 What This Application Does
This application is designed to keep you updated on bus departures from your preferred SL stop.

Here's how it works:

Fetches Real-Time Data: A Python script queries the Trafiklab SL Transport API to get the latest bus departure times for a specified siteId (a unique identifier for a bus stop or station) stored in the environment variable.

No API Key Needed: The SL Transport API is openly accessible and does not require an API key, making it very easy to get started.

Automated Scheduling: Using systemd services and timers, the script is configured to run automatically every hour on your Linux machine (Raspberry PI in this case). This means you get regular updates without manual intervention.

Logging: All output and errors from the script are logged to a file in project directory, making it easy to monitor and debug.
## 🧠 Key Learning Points
Building and deploying this application on a Raspberry Pi offers several valuable learning experiences:

1. Interacting with RESTful APIs
HTTP Requests: Understand how to make GET requests to a web API using Python's requests library.
JSON Parsing: Learn to handle and extract specific data from JSON responses.
API Documentation: Discover the importance of reading and understanding API documentation to identify endpoints, required parameters, and response formats.
2. Linux System Administration on Raspberry Pi
File System Navigation: Work with directories and files on a Linux system (e.g., /home/pi, /etc/systemd/system).
Permissions (chmod): Understand and apply execute permissions to scripts (chmod +x) to allow them to be run by the system.
Shell Scripting: Create simple bash wrapper scripts (.sh files) to execute Python scripts, manage their environment, and redirect output.
3. Systemd for Task Scheduling
Services (.service files): Define how a program should run as a background process, including its working directory, user, and logging behavior.
Timers (.timer files): Schedule services to run at specific intervals or timess.
systemctl Commands: Use systemctl to manage systemd units (e.g., daemon-reload, enable, start, status).
User vs. Root Context: Understand how systemd timers (often managed by root) can trigger services that run as a specific non-root user (using the User= directive in the .service file), which is crucial for security and proper file permissions.
4. Robust Scripting Practices
Error Handling: Implement try-except blocks in Python to gracefully handle potential issues like network errors or invalid API responses.
Logging: Direct script output and errors to log files or journald for easier debugging and monitoring of automated tasks.