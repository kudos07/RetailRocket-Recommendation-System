from kafka import KafkaProducer
import pandas as pd
import json
import time

# Kafka Configuration
TOPIC_NAME = "retail_events"
BROKER = "localhost:9092"

# Initialize Kafka Producer with optimizations
producer = KafkaProducer(
    bootstrap_servers=BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    batch_size=16384,  # Increase batch size to 16KB (you can adjust this value)
    linger_ms=10,      # Milliseconds to wait before sending a batch (higher values improve throughput)
    acks=1,            # Leader acknowledgment only (faster)
    compression_type='gzip'  # Enable compression (reduces network load)
)

# Load a smaller subset of the dataset (1000 rows)
chunk_size = 10000  # Number of rows to process
progress_step = chunk_size // 10  # Report every 10% progress within each chunk

# Process the dataset with 1000 rows and stream to Kafka
for chunk in pd.read_csv('events.csv', chunksize=chunk_size):
    futures = []  # List to hold futures for asynchronous sending
    
    for index, row in chunk.iterrows():
        event = {
            "timestamp": row["timestamp"],
            "visitorid": row["visitorid"],
            "event": row["event"],
            "itemid": row["itemid"],
            "transactionid": row["transactionid"] if not pd.isna(row["transactionid"]) else None,
        }
        
        # Asynchronously send event to Kafka
        future = producer.send(TOPIC_NAME, value=event)
        futures.append(future)
        
        # Print progress every 10% within the chunk
        if index % progress_step == 0:
            progress = (index + 1) / chunk_size
            print(f"{int(progress * 100)}% of current chunk streamed.")
        
        time.sleep(0.1)  # Simulate real-time data
    
    # Wait for all messages in the chunk to be sent before moving to the next chunk
    for future in futures:
        future.get(timeout=10)  # Ensure all messages are sent before exiting
    
    print(f"Chunk processed, {len(chunk)} events streamed.")

# Close the producer
producer.close()

print("1000 events streamed successfully.")
