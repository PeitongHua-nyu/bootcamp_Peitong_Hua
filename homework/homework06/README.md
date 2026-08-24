## Cleaning Strategy

This homework applies reusable data-cleaning functions from `src/cleaning.py` to the raw dataset stored in `data/raw/`.

### Missing Values

- Missing values in `age` and `income` are filled using the median.
- Median imputation was chosen because it is less sensitive to extreme values than the mean.
- `score` is left unchanged because it was not selected for median imputation.
- `extra_data` is left unchanged because it contains a high proportion of missing values.

### Dropping Missing Data

The `drop_missing()` function is used with a threshold of `0.5` to handle data with excessive missing values while avoiding unnecessary data loss.

### Normalization

The `age` and `income` columns are normalized to the 0–1 range using min-max scaling. This places the selected numeric features on a comparable scale.

### Data Storage

- The original dataset is stored in `data/raw/`.
- The cleaned dataset is stored in `data/processed/`.
- The original raw data is preserved and is not overwritten.

### Reusable Functions

The cleaning logic is implemented in `src/cleaning.py` using three reusable functions:

- `fill_missing_median()`
- `drop_missing()`
- `normalize_data()`