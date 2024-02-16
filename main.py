import pywhatkit as kit
import time
import pandas as pd
import numpy as np

data_frame = pd.read_csv('data.csv')
appended_df = pd.read_csv('sent_data.csv')

# List of phone numbers
numbers = np.array(data_frame['NUMBERS'])
names = np.array(data_frame['NAMES'])

interval = 15

for i in range(len(numbers)):
    message = f"""Hi *{names[i]}*, Good Afternoon!

    Message goes here!
    """

    # Get the current time
    current_time = time.localtime()

    # Extract current hour and minute
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min + 1
    kit.sendwhatmsg('+91'+str(numbers[i]), message, current_hour, current_minute)
    new_data = {'NUMBERS': [numbers[i]],
            'NAMES': [names[i]]}
    appended_df = appended_df.append(pd.DataFrame(new_data), ignore_index=True)
    time.sleep(interval)
