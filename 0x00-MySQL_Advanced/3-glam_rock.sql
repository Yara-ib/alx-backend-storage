-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
-- Column names must be: band_name and lifespan (in years until 2022 - please use 2022 instead of YEAR(CURDATE()))
-- You should use attributes formed and split for computing the lifespan
SELECT
    `band_name`,
    IF(`split` IS NOT NULL, `split` - `formed`, 2022 - `formed`) AS `lifespan`
FROM
    `metal_bands`
WHERE
    `style` LIKE '%Glam rock%'
ORDER BY
    `lifespan` DESC,
    `band_name` DESC;
