import os
from files.settings import files_base_dir as fb
from files.utils.system_sep import seq

#

# 生成文件服务器中的 content
def get_content(context, info):
    print("info:::", info)
    print(fb)
    print(context["request"].url)
    files_base_dir = fb
    if "static" in files_base_dir.split(seq):
        # todo 需要进一步调整
        # 最后时候
        if files_base_dir.endswith("static"):
            if info.startswith(".."):
                new_path = files_base_dir + seq + info
            else:
                new_path = files_base_dir + seq + info
        else:
            pass
    else:
        pass
    if info.endswith("txt"):
        context.update(content=open(new_path, 'r', encoding="utf-8").read())
        context.update(file={"status": True})
        print(context)
    elif info in os.listdir(files_base_dir):
        print("ppppp",new_path)
        files = os.listdir(new_path)
        show_files = [_file for _file in files]
        print([files_base_dir + seq + _file for _file in show_files])
        # todo 默认是根文件夹
        info_item = [
            {"msg": _file, "url": _file, "type": os.path.isdir(files_base_dir + seq + _file)} for _file in show_files
        ]
        context.update(info=info_item)
        context.update(file={"status": False})
    else:
        current_path = files_base_dir
        files = os.listdir(current_path)
        show_files = [_file for _file in files]
        print([files_base_dir + seq + _file for _file in show_files])
        # todo 默认是根文件夹
        info_item = [
            {"msg": _file, "url": _file, "type": os.path.isdir(files_base_dir + seq + _file)} for _file in show_files
        ]
        context.update(info=info_item)
        context.update(file={"status": False})
    print(context)
    return context

if __name__ == '__main__':
    os.chdir("../")
    print(seq)
    get_content({},"/tettt")