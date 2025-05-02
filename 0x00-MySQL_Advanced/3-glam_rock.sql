-- List Glam rock bands ranked by their longevity (lifespan)
SELECT
    band_name,
    (CASE 
        WHEN split IS NULL OR split = 0 THEN 2022 - formed
        ELSE split - formed
     END) AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;
