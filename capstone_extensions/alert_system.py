import csv
import time

class AlertSystem:
    def __init__(self, log_file='capstone_extensions/alerts_log.csv'):
        self.log_file = log_file
        with open(self.log_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp','object_id','priority','bbox','message'])

    def alert(self, object_id, priority, bbox, message):
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{ts}] ALERT id={object_id} priority={priority} msg={message} bbox={bbox}")
        with open(self.log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([ts, object_id, priority, bbox, message])
