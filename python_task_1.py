import pandas as pd

def generate_car_matrix(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Pivot the DataFrame using id_1 and id_2 columns
    matrix_df = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    # Set diagonal values to 0
    for col in matrix_df.columns:
        matrix_df.at[col, col] = 0

    return matrix_df

# Example usage:
file_path = 'E:\Suresh task\dataset-1.csv'
result_df = generate_car_matrix(file_path)
print(result_df)
