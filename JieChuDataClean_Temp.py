import os
import shutil

data_020_path = "/home/test4/code/EventBenchmark/data/EventSOT500/020"
data_20_w2ms_path = "/home/test4/code/EventBenchmark/data/EventSOT500/20_w2ms"

# 使用 os.listdir() 列出目录下的所有文件和子目录
seqs_names = os.listdir(data_020_path)
for seq_name in seqs_names:
    target_data = os.path.join(data_020_path, seq_name, "groundtruth.txt")
    source_data = os.path.join(data_20_w2ms_path, seq_name, "groundtruth.txt")
    
    # 使用 shutil.copyfile() 复制文件
    shutil.copyfile(source_data, target_data)