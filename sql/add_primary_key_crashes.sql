-- After crashes dataset is successfully imported,
-- create a primary key in the table using objectid.
-- Check objectid is unique across the rows, first (which it is).

SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT objectid) AS unique_ids,
    COUNT(*) FILTER (WHERE objectid IS NULL) AS null_ids
FROM crashes;

ALTER TABLE crashes
ADD PRIMARY KEY (objectid);
