import psutil
import time
import os


def format_bytes(size):
    units = ["B", "KB", "MB", "GB", "TB"]

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


def main():
    previous = psutil.net_io_counters()

    total_downloaded = 0
    total_uploaded = 0

    print("Starting Bandwidth Monitor...")
    time.sleep(1)

    try:
        while True:
            current = psutil.net_io_counters()

            download_speed = current.bytes_recv - previous.bytes_recv
            upload_speed = current.bytes_sent - previous.bytes_sent

            total_downloaded += download_speed
            total_uploaded += upload_speed

            os.system("cls" if os.name == "nt" else "clear")

            print("=" * 45)
            print("          PYTHON BANDWIDTH MONITOR")
            print("=" * 45)

            print("\n[ REAL-TIME BANDWIDTH ]")
            print(f"Download Speed : {format_bytes(download_speed)}/s")
            print(f"Upload Speed   : {format_bytes(upload_speed)}/s")

            print("\n[ TOTAL DATA THIS SESSION ]")
            print(f"Downloaded     : {format_bytes(total_downloaded)}")
            print(f"Uploaded       : {format_bytes(total_uploaded)}")

            print("\n" + "=" * 45)
            print("Monitoring is running... Press CTRL+C to stop.")

            previous = current
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\nBandwidth monitoring stopped.")
        print("Thank you for using this tool!")


if __name__ == "__main__":
    main()