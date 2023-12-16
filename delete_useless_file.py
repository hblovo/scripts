import os

def get_folder_size(folder_path):
    total_size = 0
    for path, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(path, file)
            total_size += os.path.getsize(file_path)
    return total_size

def convert_size(size_in_bytes):
    # 1 KB = 1024 bytes
    # 1 MB = 1024 KB
    # 1 GB = 1024 MB
    size_units = ['bytes', 'KB', 'MB', 'GB']
    index = 0
    while size_in_bytes > 1024 and index < len(size_units) - 1:
        size_in_bytes /= 1024
        index += 1
    return f"{size_in_bytes:.2f} {size_units[index]}"

#计算给定地址处所有文件夹的大小并排序输出
def cal_files_size(address):
    for root, dirs, files in os.walk(address):
        for name in files:
            size = os.path.getsize(os.path.join(root, name))
            # size > 100MB
            if size > 300 * 1024 * 1024:
                print(os.path.join(root, name))
                print(size / (1024 * 1024))
def get_sorted_folder_sizes(address):
    folder_sizes = []

    for folder_name in os.listdir(address):
        folder_path = os.path.join(address, folder_name)
        if os.path.isdir(folder_path):
            size = get_folder_size(folder_path)
            folder_sizes.append((folder_name, size))

    sorted_folder_sizes = sorted(folder_sizes, key=lambda x: x[1], reverse=True)
    return sorted_folder_sizes

address = r"G:/"
sorted_sizes = get_sorted_folder_sizes(address)
for folder, size in sorted_sizes:
    if size > 0:
        print(f"SizeOf {folder} = {convert_size(size)}")
while True:
    user_input = input("输入地址（输入 'exit' 退出）: ")

    if user_input == "exit":
        break

    address += "/" + user_input
    sorted_sizes = get_sorted_folder_sizes(address)
    for folder, size in sorted_sizes:
        if size > 0:
            print(f"SizeOf {folder} = {convert_size(size)}")


