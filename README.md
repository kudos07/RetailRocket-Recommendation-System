
# RetailRocket Recommendation System

This repository implements a **real-time recommendation system** for e-commerce using Apache Kafka and PySpark. The system streams and processes user events from the RetailRocket dataset to generate insights into customer behavior. It is a robust pipeline for handling high-velocity, large-scale data.

## Project Structure

```plaintext
.
├── producer.py                      # Streams data to Kafka topics
├── consumer.py                      # Consumes and processes Kafka streams with PySpark
├── retail-rocket-ecommerce-recommender-system.ipynb # Data analysis and recommendation system implementation
├── dataset/                         # Folder containing the RetailRocket dataset
```

## Dataset

The RetailRocket dataset is used to simulate user interactions, including browsing events, purchases, and clicks. The dataset should be placed in the `dataset/` folder. Ensure the file is named `events.csv` for compatibility with the `producer.py` script.

## Requirements

- Python 3.9 or later
- Apache Kafka
- PySpark
- Required Python libraries (listed in `requirements.txt` or install using the commands below)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kudos07/RetailRocket-Recommendation-System.git
    cd RetailRocket-Recommendation-System
    ```

2. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up Apache Kafka and ensure it is running locally on `localhost:9092`.

## Scripts Overview

### Producer Script (`producer.py`)
- Streams data from the RetailRocket dataset to the Kafka topic `retail_events`.
- Uses optimized settings for batch size, compression, and acknowledgments to ensure efficient streaming.

### Consumer Script (`consumer.py`)
- Processes real-time events streamed to the `retail_events` Kafka topic.
- Uses PySpark to group events by type (e.g., clicks, purchases) and count them in real-time.

### Jupyter Notebook (`retail-rocket-ecommerce-recommender-system.ipynb`)
- Analyzes the RetailRocket dataset.
- Implements machine learning algorithms for recommending items based on user behavior.

## How to Run

1. Start Apache Kafka and create the `retail_events` topic:

    ```bash
    kafka-topics.sh --create --topic retail_events --bootstrap-server localhost:9092
    ```

2. Run the producer script to stream data:

    ```bash
    python producer.py
    ```

3. Run the consumer script to process and analyze data in real-time:

    ```bash
    python consumer.py
    ```

4. Open the Jupyter Notebook for further analysis:

    ```bash
    jupyter notebook retail-rocket-ecommerce-recommender-system.ipynb
    ```

## Technologies Used

- **Apache Kafka**: Real-time data streaming.
- **PySpark**: Big data processing and streaming analytics.
- **Pandas**: Data manipulation and preprocessing.
- **Python**: Core programming language for scripts and analysis.

## Key Features

- Real-time data streaming from the RetailRocket dataset using Kafka.
- High-speed data processing and analytics with PySpark.
- Machine learning-based recommendation system implemented in the Jupyter Notebook.

## Author

Saransh Surana  
- GitHub: [kudos07](https://github.com/kudos07)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
