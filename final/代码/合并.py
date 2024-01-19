import os

# 设置要合并的文件夹路径
folder_path = "D:/songs/lyrics"

# 设置合并后的文件名
output_filename = 'D:/total_lyric.txt'

# 获取文件夹中所有txt文件的文件名
txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

# 合并文件内容
with open(output_filename, 'w', encoding='utf-8') as output_file:
    for txt_file in txt_files:
        file_path = os.path.join(folder_path, txt_file)
        with open(file_path, 'r', encoding='utf-8-sig') as input_file:
            content = input_file.read()
            output_file.write(content)

print(f'Merged files saved to: {output_filename}')
