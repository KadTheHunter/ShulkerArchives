import csv
import json
import sys


def database(csv_file_path, json_file_path=None):
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            data = [row for row in csv_reader]

        json_entries = [
            '    ' + json.dumps(row, separators=(', ', ': '), ensure_ascii=False)
            for row in data
        ]

        json_data = '{\n  "data": [\n' + ',\n'.join(json_entries) + '\n  ]\n}'

        if json_file_path:
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json_file.write(json_data)
            print(f"Successfully converted {csv_file_path} to {json_file_path}")
        else:
            print(json_data)

    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


def get_input():
    print("CSV to JSON Converter")
    print("-" * 40)

    while True:
        input_path = input("Enter the path to your CSV file: ").strip('"')
        if input_path:
            if not input_path.endswith('.csv'):
                input_path += '.csv'
            try:
                with open(input_path, 'r', encoding='utf-8'):
                    break
            except FileNotFoundError:
                print(f"File '{input_path}' not found. Please try again.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Please enter a valid file path.")

    output_path = input("Enter output JSON file path (or press Enter to print to console): ").strip('"')
    if output_path and not output_path.endswith('.json'):
        output_path += '.json'

    return input_path, output_path if output_path else None


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv) < 2 or len(sys.argv) > 3:
            print("Usage: python database.py [input_csv] [output_json]")
            print("If no arguments are provided, interactive mode will start.")
            sys.exit(1)
        input_csv = sys.argv[1]
        output_json = sys.argv[2] if len(sys.argv) > 2 else None
    else:
        input_csv, output_json = get_input()

    database(input_csv, output_json)
