import csv
import json
import pandas as pd

# Input CSV data (abbreviated for clarity)
csv_data = '''6446507942,default,daily_report,sleep,1677715200,"{""avg_hr"":60,""avg_spo2"":0,""day_sleep_evaluation"":0,""segment_details"":[{""avg_hr"":60,""bedtime"":1677706020,""sleep_deep_duration"":153,""duration"":454,""sleep_light_duration"":197,""max_hr"":99,""min_hr"":47,""sleep_rem_duration"":104,""timezone"":12,""awake_count"":2,""sleep_awake_duration"":58,""wake_up_time"":1677736740}],""long_sleep_evaluation"":19,""max_hr"":99,""min_hr"":47,""sleep_awake_duration"":58,""sleep_deep_duration"":153,""sleep_light_duration"":197,""sleep_rem_duration"":104,""sleep_score"":82,""sleep_stage"":3,""total_duration"":454}",1677753402
6446507942,default,daily_report,sleep,1677801600,"{""avg_hr"":60,""avg_spo2"":0,""day_sleep_evaluation"":0,""segment_details"":[{""avg_hr"":60,""bedtime"":1677795000,""sleep_deep_duration"":171,""duration"":492,""sleep_light_duration"":191,""max_hr"":98,""min_hr"":50,""sleep_rem_duration"":130,""timezone"":12,""awake_count"":1,""sleep_awake_duration"":18,""wake_up_time"":1677825600}],""long_sleep_evaluation"":3,""max_hr"":98,""min_hr"":50,""sleep_awake_duration"":18,""sleep_deep_duration"":171,""sleep_light_duration"":191,""sleep_rem_duration"":130,""sleep_score"":85,""sleep_stage"":4,""total_duration"":492}",1677868252
6446507942,default,daily_report,sleep,1677888000,"{""avg_hr"":63,""avg_spo2"":0,""day_sleep_evaluation"":0,""segment_details"":[{""bedtime"":1677926700,""sleep_deep_duration"":0,""duration"":35,""sleep_light_duration"":0,""timezone"":12,""awake_count"":0,""sleep_awake_duration"":0,""wake_up_time"":1677928800},{""avg_hr"":63,""bedtime"":1677887400,""sleep_deep_duration"":175,""duration"":478,""sleep_light_duration"":252,""max_hr"":108,""min_hr"":50,""sleep_rem_duration"":51,""timezone"":12,""awake_count"":2,""sleep_awake_duration"":11,""wake_up_time"":1677916740}],""long_sleep_evaluation"":3,""max_hr"":108,""min_hr"":50,""sleep_awake_duration"":0,""sleep_deep_duration"":175,""sleep_light_duration"":252,""sleep_rem_duration"":51,""sleep_score"":77,""sleep_stage"":3,""total_duration"":513}",1677972559
'''

# Split CSV into rows
rows = []
for row in csv.reader(csv_data.splitlines(), delimiter=','):
    rows.append(row)

# Prepare data for extraction
data = []
for row in rows:
    timestamp = row[4]
    sleep_data = json.loads(row[5].replace('""', '"'))  # Correcting embedded quotes

    # Extract relevant fields
    avg_hr = sleep_data.get("avg_hr")
    sleep_score = sleep_data.get("sleep_score")
    total_duration = sleep_data.get("total_duration")
    deep_sleep_duration = sleep_data.get("sleep_deep_duration")
    light_sleep_duration = sleep_data.get("sleep_light_duration")
    rem_sleep_duration = sleep_data.get("sleep_rem_duration")
    awake_count = sleep_data["segment_details"][0].get("awake_count")

    # Add extracted data to list
    data.append({
        "timestamp": timestamp,
        "avg_hr": avg_hr,
        "sleep_score": sleep_score,
        "total_duration": total_duration,
        "deep_sleep_duration": deep_sleep_duration,
        "light_sleep_duration": light_sleep_duration,
        "rem_sleep_duration": rem_sleep_duration,
        "awake_count": awake_count
    })

# Create DataFrame and save to Excel
df = pd.DataFrame(data)
df.to_excel(r'C:\Users\burak\Desktop\MiFitness Analyze\sleep_data.xlsx', index=False)

print("Excel file 'sleep_data.xlsx' created successfully.")
