SELECT COUNT(*) FISH_COUNT, MAX(IF(LENGTH IS NULL, 10, LENGTH)) MAX_LENGTH, FISH_TYPE
FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING AVG(LENGTH) >= 33
ORDER BY FISH_TYPE
