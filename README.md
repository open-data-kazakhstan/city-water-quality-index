# City Hospitals and Clinics

## Installation

To get started with the project, follow these steps:

1. Clone the repository:
    ```shell
    $ git clone https://github.com/open-data-kazakhstan/city-water-quality-index.git
    ```

2. Create and activate a virtual environment:
    ```bash
    pip install venv
    python -m venv /path/to/localrepo
    cd /path/to/localrepo
    Scripts/activate  # For Windows users
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the project:
    ```bash
    python scripts/main.py
    ```

## Data

Water data is sourced from ([stat.gov.kz](https://stat.gov.kz/ru/industries/environment/stat-eco/spreadsheets/?year=2022&name=19550&period=year&type=spreadsheets)).

- `source.xls`: Raw data of water consumption by region for the year 2022.
- `water.csv`: Cleaned version containing data of urban areas only in 2022.

All consumption values are provided in thousands of cubic meters.

## Scripts

- `package.py`: Used to create or update the datapackage.json file containing metadata about the dataset.
- `transform.py`: Used to convert the source.xls file to a CSV format for easier processing.

## License

This dataset is licensed under the Open Data Commons [Public Domain and Dedication License](https://www.opendatacommons.org/licenses/pddl/1-0/ "‌").