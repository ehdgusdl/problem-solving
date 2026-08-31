# 2022년 1월의 카테고리 별 도서 판매량을 합산하고, 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트를 출력하는 SQL문을 작성해주세요.

# 결과는 카테고리명을 기준으로 오름차순 정렬해주세요.

SELECT
    CATEGORY, sum(SALES) as TOTAL_SALES
FROM
    BOOK b
JOIN 
    BOOK_SALES s ON b.BOOK_ID = s.BOOK_ID
WHERE
    s.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY
    CATEGORY
ORDER BY 
    CATEGORY ASC;