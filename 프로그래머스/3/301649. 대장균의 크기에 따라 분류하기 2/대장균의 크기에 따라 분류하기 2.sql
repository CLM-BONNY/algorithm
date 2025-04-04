WITH COLONY_RANK AS (
    SELECT ID, (RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) * 100.0 / (SELECT COUNT(*) FROM ECOLI_DATA)) RANK_OF_COLONY
    FROM ECOLI_DATA
)
    
SELECT ID, CASE
            WHEN RANK_OF_COLONY <= 25 THEN 'CRITICAL'
            WHEN RANK_OF_COLONY > 25 AND RANK_OF_COLONY <= 50 THEN 'HIGH'
            WHEN RANK_OF_COLONY > 50 AND RANK_OF_COLONY <= 75 THEN 'MEDIUM'
            ELSE 'LOW'
           END AS COLONY_NAME
FROM COLONY_RANK
ORDER BY ID