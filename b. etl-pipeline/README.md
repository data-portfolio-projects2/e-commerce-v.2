🏗 Proposed ETL Pipeline Flow
1️⃣ Extract (Load to Dask)

Extract data from Salesforce as-is
Convert all columns to strings initially (prevents coercion errors in Dask)
2️⃣ Automated Data Validation (Before Cleaning)

Detect mixed types (flag unexpected alphanumeric in numeric fields, etc.)
Identify invalid values (negative Customer IDs, missing mandatory fields, etc.)
Save invalid records separately (for review before cleaning)
3️⃣ Transformation & Cleaning (Only for Valid Data)

Convert valid columns back to their intended dtypes
Apply standard formatting (lowercase names, date formats, currency standardization, etc.)
4️⃣ Final Processing & Compute

Save cleaned data for dashboard ingestion
Keep flagged records for manual review without modifying original files
