import os
import shutil  # 导入 shutil 模块


def delete_files_in_directory(directory):
    # 检查指定的路径是否是文件夹
    if not os.path.isdir(directory):
        print("指定的路径不是一个文件夹")
        return

    # 遍历文件夹中的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # 删除文件或链接
                print(f"已删除文件：{file_path}")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # 删除文件夹及其内容
                print(f"已删除文件夹：{file_path}")
        except Exception as e:
            print(f"删除 {file_path} 失败。原因：{e}")
