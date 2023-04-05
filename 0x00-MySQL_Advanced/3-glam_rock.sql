-- lists bands with glam rock stype
SELECT band_name, (IFNULL(split, YEAR(NOW())) - formed) AS lifespan FROM metal_bands WHERE STYLE LIKE '%Glam rock%' ORDER BY lifespan DESC;