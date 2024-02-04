import sys
import pandas as pd
from W2V import W2V
from SimilarityCalc import SimilarityCalc


def main():
    process_mode = sys.argv[1]  # 'batch' or 'user' mode of processing
    csv_mode_path = 'vectors.csv'  # Path to the vectors.csv file

    # Initialize W2V model
    print('Loading W2V model, please wait.')
    w2v_loader = W2V(csv_mode_path)
    app = SimilarityCalc(w2v_loader)

    if process_mode == 'user':
        user_input = input("Enter a phrase for similarity check: ")
        phrases_df = pd.read_csv('phrases.csv', skiprows=1, header=None, names=['phrase'], encoding='ISO-8859-1')
        closest_phrase, distance = app.find_closest_phrase(user_input, phrases_df)
        print(f"Closest phrase: {closest_phrase}\n"
              f"Calculated distance: {distance}")

    elif process_mode == 'batch':
        phrases_path = input("Please, enter the path to the phrases.csv file: ")
        output_file_name = input("Please, specify output report name: ")
        if ".csv" not in output_file_name:
            output_file_name = output_file_name + '.csv'
        app.batch_process(phrases_path, output_file_name)
        print(f"Processing complete. Results saved to {output_file_name}")

    else:
        print("Invalid process mode. Use 'batch' or 'user'.")


if __name__ == "__main__":
    main()
