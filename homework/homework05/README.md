## Data Storage

Using environment-driven paths for data storage.

- `data/raw/` stores raw data in CSV format.
- `data/processed/` stores processed data in Parquet format.
- Storage paths are configured using environment variables loaded from `.env`.
- `.env.example` provides a template for the required environment settings.
- CSV files are written without the DataFrame index.
- Parquet files preserve data types and provide efficient storage.