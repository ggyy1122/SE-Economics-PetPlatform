import re

input_file = "schema_dbdiagram.sql"
output_file = "schema_dbdiagram_final.sql"

with open(input_file, "r", encoding="utf-8") as f:
    sql = f.read()

# 替换类型
sql = re.sub(r'\bbigint\b', 'int', sql, flags=re.IGNORECASE)
sql = re.sub(r'\bsmallint unsigned\b', 'int', sql, flags=re.IGNORECASE)
sql = re.sub(r'\bchar\(32\)', 'varchar(32)', sql, flags=re.IGNORECASE)
sql = re.sub(r'\btext\b', 'varchar(255)', sql, flags=re.IGNORECASE)

# 字段级 UNIQUE 转为表级
def unique_to_table_level(match):
    field = match.group(1)
    return f"{field},"

sql = re.sub(r'(\w+ [\w\(\)]+)\s+UNIQUE', unique_to_table_level, sql)
# 收集所有 UNIQUE 字段
unique_fields = re.findall(r'(\w+) [\w\(\)]+,?\s+UNIQUE', sql)
for field in unique_fields:
    sql = sql.replace(f"{field} UNIQUE", f"{field}")
    sql = sql.replace(");", f",\n  UNIQUE ({field})\n);")

# 去掉多余空行
sql = re.sub(r'\n+', '\n', sql)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(sql)

print("已生成适合 dbdiagram.io 的 schema_dbdiagram_final.sql 文件！")