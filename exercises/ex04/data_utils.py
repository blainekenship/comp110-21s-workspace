"""Utility functions for wrangling data."""

__author__ = "730400756"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows


def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    """Make a list of values in a single column from the CSV file"""
    columns: list[str] = []
    i: int = 0
    while i < len(table):
        columns.append(table[i][key])
        i += 1
    return columns
    

def columnar(lor: list[dict[str, str]]) -> dict[str, list[str]]:
    """List of rows to Dictionary of columns"""
    doc: dict[str, list[str]] = {}
    for name in lor[0]:
        doc[name] = column_values(lor, name)
    return doc


def head(old_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Making a column-based table from N number of rows"""
    new_table: dict[str, list[str]] = {}
    for i in old_table:
        N_value: list[str] = []
        if N > len(old_table[i]):
            return old_table
        else:
            j: int = 0
            while j < N:
                N_value.append(old_table[i][j])
                j += 1
            new_table[i] = N_value
    return new_table


def select(input_dict: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Make a new table with a specific subset of the original"""
    new_dict: dict[str, list[str]] = {}
    for i in col_names:
        new_dict[i] = input_dict[i]
    return new_dict


def count(freq_values: list[str]) -> dict[str, int]:
    """Count the frequency of a value in a given list"""
    final: dict[str, int] = {}
    for item in freq_values:
        if item in final:
            final[item] += 1
        else:
            final[item] = 1
    return final

