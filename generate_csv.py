import csv


def generate_markdown(query_text: str, image_url: str, title: str, description: str) -> str:
    new_line = '\n'
    markdown = (
        f"### Search Query: `{query_text}`"
        f"{new_line}"
        f"---"
        f"{new_line}"
        f"### Product Image:"
        f"{new_line}"
        f"![]({image_url})"
        f"{new_line}"
        f"{new_line}"
        f"### Product Title:"
        f"{new_line}"
        f"`{title}`"
        f"{new_line}"
        f"{new_line}"
        f"### Product Description:"
        f"{new_line}"
        f"`{description}`"
    )

    return markdown


# Instantiate output data
output_data = []

# Read input file
with open('calibration-data-set.csv') as file:

    # Create reader object by passing the file
    # object to DictReader method
    reader = csv.DictReader(file)

    # Iterate over each row in the input csv file to generate output row
    row_number = 1
    for row in reader:
        row_markdown = generate_markdown(
            row['QUERY_TEXT'], row['PRODUCT_IMAGE_URL'], row['PRODUCT_NAME'], row['PRODUCT_DESCRIPTION'])
        row_metadata = f"{{\'id\': \'{row_number}\'}}"

        output_data.append([row_markdown, row_metadata])

        # Increment row number
        row_number += 1

# Write to output file
header = ['text', 'metadata']

with open('output-calibration-data-set.csv', 'w', encoding='UTF8', newline='') as file:
    # Instantiate writer object - account for double quote escapes
    writer = csv.writer(file)

    # Write the header
    writer.writerow(header)

    # Write the output data
    writer.writerows(output_data)
