SELECT B.ID, B.EMAIL, B.FIRST_NAME, B.LAST_NAME
FROM SKILLCODES A INNER JOIN DEVELOPERS B ON A.CODE = B.SKILL_CODE