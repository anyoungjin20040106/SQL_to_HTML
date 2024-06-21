from fastapi import FastAPI, HTTPException, Form, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine
import pandas as pd

app = FastAPI()

class DBinfo(BaseModel):
    kind: str
    host: str
    db_name: str
    user: str
    password: str
    port: int
    query: str

    @classmethod
    def as_form(cls, kind: str = Form(...), host: str = Form(...), db_name: str = Form(...), user: str = Form(...), password: str = Form(...), port: int = Form(...), query: str = Form(...)):
        return cls(kind=kind, host=host, db_name=db_name, user=user, password=password, port=port, query=query)

@app.post("/api")
def api(info: DBinfo = Depends(DBinfo.as_form)):
    # 데이터베이스 연결 문자열 생성
    sql = {
        "postgresql": f"postgresql://{info.user}:{info.password}@{info.host}:{info.port}/{info.db_name}",
        "mysql": f"mysql+pymysql://{info.user}:{info.password}@{info.host}:{info.port}/{info.db_name}",
        "mssql": f"mssql+pyodbc://{info.user}:{info.password}@{info.host}:{info.port}/{info.db_name}?driver=ODBC+Driver+17+for+SQL+Server",
        "oracle": f"oracle+cx_oracle://{info.user}:{info.password}@{info.host}:{info.port}/?service_name={info.db_name}",
    }

    if info.kind not in sql:
        raise HTTPException(status_code=400, detail=f"해당 API는 {', '.join(sql.keys())}만 가능합니다. (This API only supports {', '.join(sql.keys())})")

    # 데이터베이스 연결 및 쿼리 실행
    try:
        engine = create_engine(sql[info.kind])
        with engine.connect() as con:
            df = pd.read_sql(info.query, con)
        html_table = df.to_html(index=False)
        return html_table
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"쿼리문을 확인해주세요 : {str(e)} (Database query failed: {str(e)})")
