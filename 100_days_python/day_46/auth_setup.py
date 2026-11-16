import ytmusicapi
import json
import os

file_path = "D:/python/100_days_python/day_46/browser.json"

# with open(file_path, "r") as file:
#     data = json.load(file)

# print("JSON is valid:", isinstance(data, dict))
# print("Header keys found:", len(data))

ytmusicapi.setup(filepath=file_path)