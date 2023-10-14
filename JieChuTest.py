import os

# 指定文件夹路径
folder_path = '/home/test4/code/EventBenchmark/lib/pytracking/ltr/checkpoints/checkpoints/ltr/tomp/JieChu_tomp101_esot500'

# 定义要删除的文件范围
start_num = 1
end_num = 80

# 遍历指定范围内的文件
for num in range(start_num, end_num + 1):
    # 构建文件名
    file_name = f'ToMPnet_ep{num:04}.pth.tar'
    
    # 构建文件的完整路径
    file_path = os.path.join(folder_path, file_name)
    
    # 检查文件是否存在，然后删除
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f'Deleted: {file_name}')
    else:
        print(f'File not found: {file_name}')