import pandas as pd

# Excelファイルを読み込む
excel_file = r"C:\Users\tachi\OneDrive\ドキュメント\GitHub\jquants_checker\out_st.xlsx"
df = pd.read_excel(excel_file, sheet_name='1301')

# HTML形式で出力する
html_output = df.to_html()

# HTMLファイルに書き出す
with open('output.html', 'w') as f:
    f.write(html_output)
