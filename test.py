import pandas as pd
import os

# Excelファイルを読み込む
excel_file = r"C:\Users\tachi\OneDrive\ドキュメント\GitHub\jquants_checker\out_st.xlsx"
df = pd.read_excel(excel_file, sheet_name='1301')

# B列のデータを抽出
column = df.loc[:, ['DisclosedDate', 'TypeOfDocument']]

# 抽出したデータをDataFrameに変換してHTML形式で出力する
df = pd.DataFrame(column)
html_output = df.to_html()

output_folder = r"C:\Users\tachi\OneDrive\ドキュメント\GitHub\jquants_checker\output_folder"
output_file_path = os.path.join(output_folder, 'output.html')

# HTMLファイルに書き出す
with open(output_file_path, 'w') as f:
    f.write(html_output)
