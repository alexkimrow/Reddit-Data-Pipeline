# YouTube Comments ETL Project

This project focuses on extracting comments from YouTube videos, performing data cleaning and transformation, and storing the processed data for further analysis. The primary goal is to prepare the YouTube comments data for downstream tasks such as sentiment analysis, topic modeling, or building recommendation systems.

## Project Overview

The project follows the Extract, Transform, Load (ETL) process to handle the YouTube comments data:

1. **Extraction**: YouTube Data API v3 is used to extract comments from specified YouTube videos. The extracted data includes comment text, author information, publication timestamps, and other relevant details.

2. **Cleaning**: The extracted comments undergo data cleaning to remove unwanted elements such as URLs, emojis, special characters, and stopwords. This step aims to prepare the text data for further analysis by eliminating noise and irrelevant information.

3. **Transformation**: Advanced text processing techniques, including lemmatization and stopword removal, are applied to further refine the comments. This helps in standardizing the text data and improving its quality for downstream tasks.

4. **Loading**: The cleaned and transformed comments are stored in CSV format for easy access and analysis. The final dataset includes structured information about the comments, making it suitable for various data analysis and machine learning tasks.

## Directory Structure

- **data/**: Contains the raw and cleaned datasets generated during the ETL process.
- **scripts/**: Houses the Python scripts responsible for data extraction, cleaning, and transformation.
- **requirements.txt**: Lists all the dependencies required to run the project.
- **README.md**: Provides an overview of the project, installation instructions, and usage guidelines.

## Setup Instructions

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip:

3. **Run the ETL Process**: Execute the main script to perform the ETL process and generate the cleaned dataset:

4. **Explore the Data**: Once the ETL process is complete, you can explore the cleaned dataset located in the `data/` directory.
