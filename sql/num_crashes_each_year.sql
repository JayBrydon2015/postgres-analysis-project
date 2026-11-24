-- Create index on crash year for faster querying

CREATE INDEX idx_crashes_crashyear
ON crashes (crashyear);

-- Count number of crashes in each year; show in ascending order

SELECT crashyear, COUNT(*) as num_crashes
FROM crashes
GROUP BY crashyear
ORDER BY num_crashes;
