-- 코드를 입력하세요
SELECT COUNT(USER_ID) FROM USER_INFO
WHERE DATE_FORMAT(JOINED, '%Y') = 2021 AND (20 <= AGE AND AGE <= 29)