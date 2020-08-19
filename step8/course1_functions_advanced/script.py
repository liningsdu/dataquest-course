def split_and_stack(df, new_names):
    """Splits a DataFrame's columns into two halves and then stack
    them vertically, returning a new DataFrame with 'new_names' as the
    column names.

    Args:
        df (DataFrame): The DataFrame to split
        new_names (iterable or str): The column names for the new DataFrame

    Returns:
        DataFrame
    """
    half = int(len(df.columns) / 2)
    left = df.iloc[:, :half]
    right = df.iloc[:, half : ]
    return pd.DataFrame(
            data = np.vstack([left.values, right.values]),
            columns = new_names
    )
