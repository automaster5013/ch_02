from pathlib import Path
import pandas as pd
from step_1 import IN_DIR, OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

result = []
for xlsx_path in Path(IN_DIR).glob("2024년*월.xlsx"):
    df_raw = pd.read_excel(xlsx_path, sheet_name="Sheet1", 
                            usecols="B:E", skiprows=2)
    result.append(df_raw)
result

df_concat = pd.concat(result)
df_concat.to_excel(OUT_DIR / f"{Path(__file__).stem}.xlsx", index=False)

#################################################(데이터_취합1_취합2_소스코드)

