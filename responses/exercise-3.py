# create a new dataset with columns customer_id, start_date, end_date, end_reason.

import os
from pathlib import Path
import re

import pandas as pd

# not functioning but have some questions 

#question: How is the final status supposed to be determined for cancel, freeze, expired? Does cancel == terminated? 
#question: is the status-changes.csv generated from the existing table-history.csv and has the most recent entries or does table-history.csv?


def parse_changes(x, name):
    # use regular expression to parse delimited attribute changes 
    matches = re.findall(r'(?P<attribute>[a-zA-Z_]*)-\^!\^!\^-(?P<oldValue>[a-zA-Z-\s\:\d]*)\s?-\^!\^!\^-(?P<newValue>[a-zA-Z-\s\:\d]*)\s?@#@#@#', x)
    if matches:
        for attr, old_value, new_value in matches:
            if attr == name:
                return old_value, new_value


def reformatData(status_changes_df, table_history_df):
    # only look at rows with start dates and customer_id 
    valid_table_history_df = table_history_df[table_history_df["changes"].str.contains("membership_start_date")]
    # Creates the final table with the column names we want to display
    final_table = pd.DataFrame(columns=['customer_id', 'status', 'start_date', 'end_date'])
    # iterate each row for membership changes and find closest start date and end date to complete the final table row status entry
    # would need to check completed start end dates to be valid   
    for index, row in valid_table_history_df.iterrows():
        start_date = parse_changes(row["changes"], "membership_start_date")
        if start_date.strip() != "0000-00-00":
            customer_id_status_changes["start_date"] = pd.to_datetime(customer_id_status_changes["start_date"])
            customer_id_status_changes = customer_id_status_changes[(customer_id_status_changes["start_date"] > start_date)]
            val = customer_id_status_changes.iloc[0]
            final_table.loc[len(final_table.index)] = [val['customer_id'], val['status'], start_date, val['start_date']]
    print(final_table)


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    parent_path = Path(dir_path).parent
    print(parent_path)
    status_changes_df = pd.read_csv(os.path.join(parent_path, "data-sources/status-changes.csv"))
    table_history_df = pd.read_csv(os.path.join(parent_path, "data-sources/table-history.csv"))

    result = reformatData(status_changes_df, table_history_df)
    print(result)
    print("hello world")
