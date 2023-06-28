import json
import glob

# List all JSON files in the directory
json_files = glob.glob("*.json")

# Initialize an empty list to store the combined dictionaries
combined_data = []

# Iterate over each JSON file
for file_name in json_files:
    print(f"Reading {file_name}")
    with open(file_name, "r") as file:
        data = json.load(file)
        combined_data.extend(data)

# Create a dictionary with the @context and @graph
output_data = {
    "@context": "https://raw.githubusercontent.com/atlaskb/models/main/jsonld-context-autogen/kbmodel.context.jsonld",
    "@graph": combined_data
}

# Write the combined dictionaries to a new JSON file
with open("combined.json", "w") as outfile:
    json.dump(output_data, outfile, indent=2)