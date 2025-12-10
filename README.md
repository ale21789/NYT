# Big Data Final Project

This repository contains the analysis and visualization code for the Big Data final project, focusing on the Internet Research Agency (IRA) Twitter dataset and California Road Network analysis.

## Project Structure

- **`big data final.ipynb`**: The main notebook for data processing. It handles the ingestion of raw CSV files, merging, and generation of the final parquet and CSV datasets.
- **`California Road Analysis.ipynb`**: Notebook for analyzing the California road network graph. **Requires Databricks.**
- **`Network Analysis Twitter Dataset.ipynb`**: Notebook for performing network analysis on the Twitter dataset. **Requires Databricks.**
- **`index.html` & `us.html`**: The web interface for presenting the analysis results.
- **`styles.css` & `script.js`**: Styling and interactivity for the web interface.
- **`graphs/`**: Contains generated HTML graph visualizations.
- **`motif/`**: Contains motif analysis visualizations for the road network.
- **`images/`**: Static images used in the report.
- **`raw csv/`**: Directory for raw input data (see Setup Instructions).

## Setup Instructions

### 1. Data Placement
Due to file size limits, the raw data is not included in this repository. To reproduce the analysis:

1.  Create a folder named `raw csv` in the root directory of this project (if it doesn't exist).
2.  Place all the raw CSV data files into this `raw csv` folder.

### 2. Data Processing
Run the **`big data final.ipynb`** notebook first. This notebook will:
- Read the raw files from the `raw csv` folder.
- Process and merge the data.
- Generate the necessary output files, including `merged_twitter_trolls.csv` and `russian_trolls.parquet`.

### 3. Databricks Requirements
The following notebooks are designed to run on a **Databricks** environment due to their computational requirements and library dependencies:

- `California Road Analysis.ipynb`
- `Network Analysis Twitter Dataset.ipynb`

Please upload these notebooks and the processed data to Databricks to execute them.
