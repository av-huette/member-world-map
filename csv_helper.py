import pandas as pd
import user_inputs as ui


def read_csv() -> pd.DataFrame:
    """
    Read CSV specified by user inputs and return as pandas dataframe.
    """
    file_path = ui.get_file_path()
    delimiter = ui.get_delimiter()
    codec = ui.get_codec()
    column_indices = ui.get_column_indices()
    csv = pd.read_csv(file_path,
                      sep=delimiter,
                      encoding=codec,  # cp1252
                      usecols=column_indices)
    return csv


def chunk_csvs(csvs: []) -> []:
    """
    Divide CSVs in chunks of 50 lines (addresses).
    """
    chunks = []
    for csv in csvs:
        length = len(csv.values)
        if length > 50:
            i = 50
            while True:
                if i < length:
                    chunks.append(csv.values[i - 50: i])
                else:
                    chunks.append(csv.values[i - 50:length])
                    break
                i += 50
        else:
            chunks.append(csv.values)
    return chunks
