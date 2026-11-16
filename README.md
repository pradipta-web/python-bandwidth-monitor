# Python Bandwidth Monitor

A simple real-time network bandwidth monitoring tool built with Python. This tool tracks download and upload speeds, as well as total data transferred during the current monitoring session.

## Features

- Real-time download speed monitoring.
- Real-time upload speed monitoring.
- Displays total downloaded data.
- Displays total uploaded data.
- Automatically refreshes every second.
- Supports readable data units (B, KB, MB, GB, TB).
- Lightweight and easy to use.

## Technologies Used

- Python
- Psutil
- Time
- OS

## Requirements

- Python 3.8 or newer
- Psutil

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/pradipta-web/python-bandwidth-monitor.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-bandwidth-monitor
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using:

```bash
py main.py
```

The monitor will display real-time network bandwidth information in your terminal.

Press `CTRL + C` to stop monitoring.

## Project Structure

```text
python-bandwidth-monitor/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Notes

- Network statistics are collected using Psutil.
- Download and upload speeds are refreshed every second.
- Total transferred data is calculated from the moment the program starts.
- Network traffic is aggregated across available network interfaces.

## Author

**Kinervaaa**