# %%
# standard
import datetime as dt
import logging
from pathlib import Path

# project specific
import yaml

# custom
from src.example_module import download, process, visualise


def run_pipeline():
    """Runs analysis pipline accoridng to config file settings"""
    BASE_DIR = Path(__file__).parents[1]
    INPUT_DIR = BASE_DIR / "input"
    OUTPUT_DIR = BASE_DIR / "output"

    with open(INPUT_DIR / "configs" / "example_config.yml", "r") as file:
        example_config = yaml.safe_load(file)

    example_config["date_stamp"] = dt.datetime.now().strftime("%Y%m%d-%H%M")

    logging.basicConfig(
        filename=OUTPUT_DIR / f'{example_config["date_stamp"]}_example.log',
        encoding="utf-8",
        level=logging.INFO,
    )
    logging.info("Running analyis")
    download.download_nhs_data(example_config)

    summary_df, _, nims_monthly_df = process.load_and_process()

    visualise.make_plots(summary_df, nims_monthly_df, example_config)

    with open(
        INPUT_DIR / "configs" / f'config_{example_config["date_stamp"]}.yml', "w"
    ) as outfile:
        yaml.dump(example_config, outfile)

    logging.info("Finished")


if __name__ == "__main__":
    run_pipeline()
