#! /usr/bin/env python3

import os
import requests

# Directory path to the feedbacks
directory = os.getcwd()

# Create empty lists to store data
feedbacks = []

files = [txt_file for txt_file in os.listdir(directory) if txt_file.endswith('.txt')]

for file in files:
    with open(file) as f:
            feedback_dict = {}
            for line_num, line in enumerate(f):
                line = line.strip()
                if line_num == 0:
                    feedback_dict['title'] = line
                elif line_num == 1:
                    feedback_dict['name'] = line
                elif line_num == 2:
                    feedback_dict['date'] = line
                else:
                    feedback_dict['feedback'] = line
            feedbacks.append(feedback_dict)

for feedback in feedbacks:
    response = requests.post('http://34.136.190.81/feedback/', data=feedback)
    if response.status_code == 201:
        print('Succeeded...')
    else:
        response.raise_for_status()
