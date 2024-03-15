# standard
import logging
from pathlib import Path

import pandas as pd

# project specific
import requests
from bs4 import BeautifulSoup

# custom
from src.example_module import util


def download_nhs_data(config: dict):
    """Runs the download sub-pipline"""
    # GJ unsure of best practice for setting dir
    BASE_DIR = Path(__file__).parents[2]
    INPUT_DIR = BASE_DIR / "input"

    file_links = scrape_file_links(config["url"])

    download_file(
        file_links,
        config["summary"]["regex"],
        config["summary"]["file_name"],
        INPUT_DIR / "data",
    )

    download_file(
        file_links,
        config["nims"]["regex"],
        config["nims"]["file_name"],
        INPUT_DIR / "data",
    )


def scrape_file_links(url: str) -> pd.DataFrame:
    """
    Scrape website links

    Scrape the links to valid file formats (.xlsx, .csv) from supplied url

    Args:
        url (str): url of target website

    Returns:
        pd.DataFrame: df with colums for 'title' and 'link; (href)

    Raises:
        TypeError: The name variable is not a str
    """
    if not isinstance(url, str):
        raise TypeError("The url entered was not a string")

    else:
        html = requests.get(url=url, timeout=5)

        soup = BeautifulSoup(html.content, "html.parser")
        link_results = soup.select('a[href$=".xlsx"], a[href$=".csv"]')

        file_links_df = pd.DataFrame()
        file_links_df.loc[:, "title"], file_links_df["link"] = [
            [x.find("p").text for x in link_results],
            [x["href"] for x in link_results],
        ]

    return file_links_df


def download_file(
    file_links_df: pd.DataFrame, file_regex: str, file_name: str, data_path: Path
):
    """
    Download file of interest

    Uses a regular expression to find file of interest in `file_links_df`,
    then downloads and saves to named directory

    Args:
        file_links_df (pd.DataFrame): df with a 'title' colum and a 'link' column
        file_regex (str): regular expression to match against file_links_df 'title'
        file_name (str): name to save file under
        data_path (Path): directory to save file in
    """
    file_url = file_links_df.link[util.get_regex_match(file_links_df.title, file_regex)]
    file = requests.get(file_url, timeout=5)

    with open(data_path / f'{file_name}.{file_url.split(".")[-1]}', "wb") as output:
        output.write(file.content)

    logging.info(
        f'file downloaded to {data_path / file_name}.{file_url.split(".")[-1]}'
    )
