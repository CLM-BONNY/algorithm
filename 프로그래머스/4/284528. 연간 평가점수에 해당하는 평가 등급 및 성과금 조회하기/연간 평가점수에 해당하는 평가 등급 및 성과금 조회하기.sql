-- 코드를 작성해주세요
WITH HR_AVG_GRADE AS (
    SELECT EMP_NO, AVG(SCORE) AVG_SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO
), HR_REAL_GRADE AS (
    SELECT EMP_NO, CASE
                      WHEN AVG_SCORE >= 96 THEN 'S'
                      WHEN AVG_SCORE >= 90 THEN 'A'
                      WHEN AVG_SCORE >= 80 THEN 'B'
                      ELSE 'C'
                   END AS GRADE
    FROM HR_AVG_GRADE
    GROUP BY EMP_NO
)

SELECT B.EMP_NO, A.EMP_NAME, B.GRADE, CASE
                                        WHEN B.GRADE = 'S' THEN A.SAL * 0.2
                                        WHEN B.GRADE = 'A' THEN A.SAL * 0.15
                                        WHEN B.GRADE = 'B' THEN A.SAL * 0.1
                                        ELSE 0
                                     END AS BONUS
FROM HR_EMPLOYEES A INNER JOIN HR_REAL_GRADE B ON A.EMP_NO = B.EMP_NO
ORDER BY EMP_NO