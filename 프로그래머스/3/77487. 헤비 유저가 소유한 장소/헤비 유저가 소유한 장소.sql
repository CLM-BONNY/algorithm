-- 코드를 입력하세요
WITH TEMP AS (
    SELECT HOST_ID FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(HOST_ID) >= 2
)

SELECT * FROM PLACES
WHERE HOST_ID IN (SELECT HOST_ID FROM TEMP)
ORDER BY ID