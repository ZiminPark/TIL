- Sample Table
```SQL
WITH items AS
  (SELECT 
    3 as id,
    '["coffee", "tea", "milk" ]' as list,
    4 as st,
    6 as en
  UNION ALL
  SELECT 
    6 as id,
    '["coffee", "icf", "don", "milk"]' as list,
    0 as st,
    3 as en
)
SELECT 
    *
FROM 
    items

```

#### 1. JSON column 처리 [방법](https://cloud.google.com/bigquery/docs/reference/standard-sql/json_functions#jsonpath_format)
- JSONPath 형식 : $, ., [] 뜻 알기


#### 2. UNNES와 CROSS JOIN 으로 이벤트 파라미터 [처리하기](https://medium.com/firebase-developers/using-the-unnest-function-in-bigquery-to-analyze-event-parameters-in-analytics-fb828f890b42#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImQ0Y2JhMjVlNTYzNjYwYTkwMDlkODIwYTFjMDIwMjIwNzA1NzRlODIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2MDczMTMzODQsImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwOTkzMDYwMTQzOTE0Nzk0NDQ3MCIsImhkIjoid2F0Y2hhLmNvbSIsImVtYWlsIjoiaG9sZGVuQHdhdGNoYS5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXpwIjoiMjE2Mjk2MDM1ODM0LWsxazZxZTA2MHMydHAyYTJqYW00bGpkY21zMDBzdHRnLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwibmFtZSI6ImhvbGRlbiBQYXJrIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS8tSDQ1RzlwWnM2REUvQUFBQUFBQUFBQUkvQUFBQUFBQUFBQUEvQU1adXVjbXE1Z3lWQklHT1BvYXRMejNKUjFOQkVSRmFEUS9zOTYtYy9waG90by5qcGciLCJnaXZlbl9uYW1lIjoiaG9sZGVuIiwiZmFtaWx5X25hbWUiOiJQYXJrIiwiaWF0IjoxNjA3MzEzNjg0LCJleHAiOjE2MDczMTcyODQsImp0aSI6ImYyMjhlMGU2MjA1MmNjZGIwMzNmOTc3YTBhYzUwZTgyZDI3ODdlZjYifQ.F3kQW23ov8MWfv7Mg8VGSarnzLqvoWCBiQCYEOQ35Ghr-SCeA89whXSRWdvcdCVskeqQS-Cw51fUegq2zCfz8PDCROsCSoF_SIGEps5zVrJZaNDmVk4km0OUlT9jNiCz_FGpzM2BTp0YlHBawr0QFtK43d0IKLzRYHbHY2foLF-uOCRfQBFGWMwGphzImM1eYUl_bOiPpAd2U7dtCyqFz4R7G56Udrwb8YaoFttn1zpqJSteaaEGGdbIs95zrj3S0iQrK_Afu4VXw6lvYlPtB2WkpQwhSjiq9SP4LMCKMdn88mgY6gVkB3UTquzqhkayi4F6w9Kod86l7T6HXHrwMg)
- SQL에서 Array 개념 알기

#### 3. User Define Function [BQ](https://cloud.google.com/bigquery/docs/reference/standard-sql/user-defined-functions?hl=ko)
```SQL
CREATE TEMP FUNCTION json2array(json STRING)
RETURNS ARRAY<STRING>
LANGUAGE js AS """
  return JSON.parse(json).map(x=>JSON.stringify(x));
"""; 
WITH `project.dataset.table` AS (
  SELECT 'bla' id, '[{"user": "a@a.de", "timestamp": 0, "status": 1}, {"user": "a@a.de", "timestamp": 1, "status": 2}]' json
)
SELECT id, 
  JSON_EXTRACT_SCALAR(x, '$.user') AS user,
  JSON_EXTRACT_SCALAR(x, '$.timestamp') AS `timestamp`,
  JSON_EXTRACT_SCALAR(x, '$.status') AS status
FROM `project.dataset.table`,
  UNNEST(json2array(JSON_EXTRACT(json, '$'))) x  
```

#### 4. Generate Array And UNNEST [BQ](https://cloud.google.com/bigquery/docs/reference/standard-sql/array_functions#generate_array)
```SQL
WITH A as (
    SELECT 
        4 as a,
        5 as b,
        8 as c
)
, B as (
    SELECT 
        GENERATE_ARRAY(A.a, A.c) as f
    FROM
        A
)
SELECT
    A.a,
    x
FROM 
    A,
    B,
    UNNEST(B.f) as x
```

#### 5. UNNEST TWO COLUMNS [BQ](https://stackoverflow.com/questions/54404360/advanced-unnest-across-multiple-array-columns-in-bigquery/54408733#54408733)
- Use OFFSET
- 제일 좋은 방법인지는 모르겠다.

