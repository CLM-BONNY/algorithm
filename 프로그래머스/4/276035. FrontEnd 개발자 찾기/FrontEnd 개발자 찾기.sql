WITH FRONTEND AS (
    SELECT SUM(CODE) TOTAL_FRONTEND_CODE
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End'
)

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS A JOIN FRONTEND B ON 1=1
WHERE (A.SKILL_CODE & B.TOTAL_FRONTEND_CODE) > 0
ORDER BY ID