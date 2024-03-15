# %%
# standard
import logging
from pathlib import Path

# project specific
import numpy as np
import pandas as pd

# custom
from src.example_module import util


def load_and_process() -> pd.DataFrame:
    """
    loads and cleans data

    Loads the summary and nims datasets as dfs from the data directory
    Cleans dataframes ready for analysis
    Calculates a monthly total df from the nims dataset

    Returns:
        pd.DataFrame: dataframe containing summary data
        pd.DataFrame: dataframe containing nims data
        pd.DataFrame: dataframe containing monthly totals of nims data
    """

    BASE_DIR = Path(__file__).parents[2]
    INPUT_DIR = BASE_DIR / "input"

    summary_df = load_summary_data(INPUT_DIR / "data")
    nims_df = load_nims_df(INPUT_DIR / "data")
    nims_monthly_totals = get_monthly_totals(nims_df)

    return summary_df, nims_df, nims_monthly_totals


def load_summary_data(data_path: Path) -> pd.DataFrame:
    """
    Loads summary dataset and cleans

    Renames columns, drops unnecessary rows,
    and cols and explictly casts column data types

    Args:
        data_path (Path): path to data directory

    Returns:
        pd.DataFrame: dataframe of cleaned summary data
    """
    logging.info(f'Reading table 2a from {data_path / "summary.xlsx"}')
    summary_df = pd.read_excel(data_path / "summary.xlsx", sheet_name="Table 2a")

    # define start and end
    start_row = util.get_regex_match(summary_df.iloc[:, 0], "^Table 2a")
    end_row = util.get_regex_match(summary_df.iloc[:, 0], "^Source: NHS England$")
    summary_df = summary_df.iloc[start_row:end_row, :].reset_index(drop=True)

    final_col_names = [
        (
            summary_df.iloc[2, x]
            if summary_df.iloc[2, x] not in ["-", np.nan]
            else summary_df.iloc[3, x]
        )
        for x in range(0, len(summary_df.columns))
    ]
    summary_df.columns = [x.lower().replace(" ", "_") for x in final_col_names]

    # GJ unsure if this is best practice ..
    drop_null_cols = [
        x
        for x in summary_df.columns
        if summary_df[x].isna().sum() > len(summary_df[x]) * 0.8
    ]
    drop_null_rows = [
        x
        for x in summary_df.index
        if summary_df.loc[x].isna().sum() > len(summary_df.loc[x]) * 0.8
    ]
    summary_df = summary_df.drop([2, 3] + drop_null_rows, axis=0)
    summary_df = summary_df.drop(drop_null_cols, axis=1)

    summary_df = summary_df.rename(columns={"date": "weekday", "unknown1": "unknown"})
    summary_df = summary_df.astype(
        {
            "weekday": "object",
            "appointment_date": "datetime64[ns]",
            "total_count_of_appointments": "int64",
            "attended": "int64",
            "did_not_attend": "int64",
            "unknown": "int64",
        }
    )
    return summary_df


def load_nims_df(data_path: Path) -> pd.DataFrame:
    """Loads nims data

    Args:
        data_path (Path): path to data directory

    Returns:
        pd.DataFrame: dataframe of nims data
    """

    logging.info(f'Reading file {data_path / "nims.csv"}')

    nims_df = pd.read_csv(data_path / "nims.csv")
    nims_df.columns = [x.lower().replace(" ", "_") for x in nims_df.columns]
    nims_df = nims_df.astype(
        {
            "date": "datetime64[ns]",
            "type": "object",
            "nhs_area_code": "object",
            "ons_code": "object",
            "name": "object",
            "total": "int64",
        }
    )
    return nims_df


def get_monthly_totals(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates totals by month

    Args:
        df (DataFrame): _description_

    Returns:
        pd.DataFrame: dataframe holding monthly totals of input data
    """
    logging.info("Creating monthly totals")

    grouped_df = df.groupby([df["date"].dt.year, df["date"].dt.month])["total"].sum()

    grouped_df.index = grouped_df.index.rename("month", level=1).rename("year", level=0)
    grouped_df = grouped_df.reset_index()

    grouped_df.month = grouped_df.month.astype("object")
    grouped_df.loc[:, "month"] = (
        pd.to_datetime(grouped_df[["year", "month"]].assign(DAY=1))
        .dt.month_name()
        .str.slice(stop=3)
    )

    return grouped_df
