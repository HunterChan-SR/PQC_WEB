import csv
import json

# 中文 → 英文字段映射表
key_map = {
    "算法名": "algorithmName",
    "算法用途": "purpose",
    "算法困难问题类型": "hardProblemType",
    "具体算法困难问题": "hardProblem",
    "作者团队": "author",
    "官网链接": "officialSite",
    "源代码链接": "sourceCode",
    "标准化文件链接": "standardDoc",
    "所有评论": "allComments",
    "算法特色简介": "description",
    "算法后续进展": "progress"
}

def csv_to_json(csv_file_path, json_file_path):
    with open(csv_file_path, 'r', encoding='utf-8-sig', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        data = []

        for row in reader:
            clean_row = {}
            for k, v in row.items():
                k = k.strip()
                v = v.strip() if v else ""
                # 将中文键名映射为英文
                new_key = key_map.get(k, k)
                clean_row[new_key] = v
            data.append(clean_row)

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print(f"✅ 已成功将 {csv_file_path} 转换为 {json_file_path}")


if __name__ == "__main__":
    csv_file_name = input("请输入 CSV 文件名（如 algorithms.csv）: ").strip()
    json_file_name = csv_file_name + '.json'
    csv_to_json(csv_file_name, json_file_name)
