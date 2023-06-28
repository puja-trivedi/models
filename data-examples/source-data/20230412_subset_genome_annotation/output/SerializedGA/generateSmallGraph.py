import json
import argparse

parser = argparse.ArgumentParser(description='Create a graph based on a subset of single json data file.')
parser.add_argument('--file_name', '-f', type=str, required=True)
parser.add_argument('--num_objects', '-n', type=int, default=15)
args = parser.parse_args()

# Initialize an empty list to store the combined dictionaries
combined_data = []

# Iterate over each JSON file
with open(args.file_name, "r") as file:
    data = json.load(file)
    combined_data.extend(data)

# Create a dictionary with the @context and @graph
output_data = {
    "@context": "https://raw.githubusercontent.com/atlaskb/models/main/jsonld-context-autogen/kbmodel.context.jsonld",
    "@graph": combined_data[:args.num_objects]
}

# Write the combined dictionaries to a new JSON file
with open("small_graph_" + str(args.num_objects) + "_" + args.file_name + "ld", "w") as outfile:
    json.dump(output_data, outfile, indent=2)