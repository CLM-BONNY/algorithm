-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, date_format(HIRE_YMD, '%Y-%m-%d')  FROM DOCTOR
WHERE (MCDP_CD = 'GS' || MCDP_CD = 'CS') ORDER BY HIRE_YMD DESC, DR_NAME ASC