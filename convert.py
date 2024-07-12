import os
import pandas as pd

base_directory = "/home/prasanjith/Desktop/atr/"
exceptions = []

#Forex = [folder for folder in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, folder))]
Forex = ["AUDCAD", "AUDUSD", "EURJPY", "GBPJPY", "GBPUSD", "USDJPY"]
exceptions = []
processed_file = "/home/prasanjith/Desktop/atr/processed.txt"

# Ensure the processed file exists
if not os.path.exists(processed_file):
    with open(processed_file, 'w') as f:
        pass  # Create the file if it does not exist

# Read the processed currency pairs from the text file
with open(processed_file, 'r') as f:
    processed_pairs = f.read().splitlines()

for i in Forex:
    if i in processed_pairs:
        print(f"{i} has already been processed. Skipping.")
        continue

    try:
        Folder_path = "/home/prasanjith/Desktop/atr/" + str(i) + "/"
        file1 = Folder_path + 'FOREXCOM_' + str(i) + ', 1D.csv'
        file2 = Folder_path + 'FOREXCOM_' + str(i) + ', 60.csv'

        # Create the folder if it does not exist
        if not os.path.exists(Folder_path):
            os.makedirs(Folder_path)
            print(f"The folder '{Folder_path}' was created.")

        try:
            # Read the CSV files
            read1 = pd.read_csv(file1)
            read2 = pd.read_csv(file2)

            # Save the JSON files in the same path as Folder_path
            json_file1 = Folder_path + str(i) + "1D" + '.json'
            json_file2 = Folder_path + str(i) + "60" + '.json'
            read1.to_json(json_file1, orient='records')
            read2.to_json(json_file2, orient='records')

            print(f"JSON files for {i} saved successfully in {Folder_path}")

            # Append the processed currency pair to the text file
            with open(processed_file, 'a') as f:
                f.write(i + '\n')

        except FileNotFoundError as e:
            raise FileNotFoundError(f"CSV file not found: {e}")
        except pd.errors.EmptyDataError as e:
            raise pd.errors.EmptyDataError(f"CSV file is empty or not readable: {e}")
        except Exception as e:
            raise Exception(f"Error reading CSV files: {e}")
        
        

    except Exception as e:
        exceptions.append((i, str(e)))
        print(f"Error processing {i}: {e}")

print("Exceptions encountered:")
for ex in exceptions:
    print(ex)
