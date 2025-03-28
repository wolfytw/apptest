# tien-tw-load-test

This project is designed to perform load testing on the external website [https://www.tien.tw](https://www.tien.tw) using Locust.

## Project Structure

```
tien-tw-load-test
├── locustfiles
│   ├── main.py
│   ├── behaviors
│   │   ├── __init__.py
│   │   ├── browse.py
│   │   └── search.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── data
│   └── test_data.csv
├── requirements.txt
├── run.sh
└── README.md
```

## Installation

To get started, clone the repository and install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Tests

To run the load tests, execute the following command:

```bash
sh run.sh
```

## User Behavior

The project simulates user behavior through two main actions:

1. **Browsing**: Users will navigate through the website.
2. **Searching**: Users will perform searches on the website.

## Data

Test data is stored in `data/test_data.csv`, which may include usernames, passwords, or other parameters necessary for the tests.

## Requirements

Make sure to have the following packages listed in `requirements.txt` installed:

- locust

## Contributing

Feel free to submit issues or pull requests to improve the project.