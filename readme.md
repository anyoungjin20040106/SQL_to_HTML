# SQL-To-HTML FastAPI 서버

## 개요
이 프로젝트는 FastAPI를 사용하여 SQL 쿼리를 실행하고 결과를 HTML로 반환하는 서버입니다.

## API 사용법

### 엔드포인트

\`POST /api\`

이 엔드포인트는 데이터베이스 연결 정보를 받아 SQL 쿼리를 실행하고 결과를 HTML 테이블로 반환합니다.

### 요청

- **URL**: \`http://127.0.0.1:8000/api\`
- **HTTP 메서드**: \`POST\`
- **콘텐츠 타입**: \`application/x-www-form-urlencoded\`

### 요청 파라미터

다음 파라미터들을 \`form-data\` 형식으로 전송합니다:

- \`kind\`: 데이터베이스 종류 (예: \`mysql\`, \`postgresql\`, \`mssql\`, \`oracle\`)
- \`host\`: 데이터베이스 호스트 (예: \`localhost\`)
- \`db_name\`: 데이터베이스 이름
- \`user\`: 데이터베이스 사용자 이름
- \`password\`: 데이터베이스 비밀번호
- \`port\`: 데이터베이스 포트 (예: \`3306\` for MySQL)
- \`query\`: 실행할 SQL 쿼리

### 예시 요청

#### Postman을 사용한 요청

1. **새 요청 만들기**: Postman에서 새로운 \`POST\` 요청을 만듭니다.
2. **URL 설정**: 요청 URL을 \`http://127.0.0.1:8000/api\`로 설정합니다.
3. **Body 설정**: \`Body\` 탭에서 \`form-data\`를 선택합니다.
4. **파라미터 추가**:
    - \`kind\`: \`mysql\`
    - \`host\`: \`localhost\`
    - \`db_name\`: \`your_db\`
    - \`user\`: \`your_user\`
    - \`password\`: \`your_password\`
    - \`port\`: \`3306\`
    - \`query\`: \`SELECT * FROM your_table\`
5. **요청 보내기**: "Send" 버튼을 클릭하여 요청을 보냅니다.

#### curl을 사용한 요청

터미널에서 curl 명령어를 사용하여 요청을 보낼 수 있습니다:

\`\`\`sh
curl -X POST "http://127.0.0.1:8000/api" \\
     -F "kind=mysql" \\
     -F "host=localhost" \\
     -F "db_name=your_db" \\
     -F "user=your_user" \\
     -F "password=your_password" \\
     -F "port=3306" \\
     -F "query=SELECT * FROM your_table"
\`\`\`

### 응답

성공적인 요청에 대한 응답은 HTML 테이블 형식으로 SQL 쿼리 결과를 반환합니다. 오류가 발생하면 HTTP 상태 코드와 함께 오류 메시지를 반환합니다.

- **성공 응답 예시**:
    \`\`\`html
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th>column1</th>
          <th>column2</th>
          ...
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>value1</td>
          <td>value2</td>
          ...
        </tr>
        ...
      </tbody>
    </table>
    \`\`\`

- **오류 응답 예시**:
    \`\`\`json
    {
      "detail": "쿼리문을 확인해주세요 : [오류 메시지] (Database query failed: [error message])"
    }
    \`\`\`

## 서버 실행 방법

1. **필요한 패키지 설치**:
    \`\`\`sh
    pip install fastapi uvicorn sqlalchemy pandas pymysql
    \`\`\`

2. **FastAPI 서버 실행**:
    \`\`\`sh
    uvicorn main:app --reload
    \`\`\`

이제 FastAPI 서버가 실행 중이며, 위의 예시와 같이 API를 사용하여 SQL 쿼리를 실행하고 결과를 HTML로 받을 수 있습니다.
EOF
