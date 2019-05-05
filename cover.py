import os
import shutil


class cover():
    def __init__(self, path):
        self.path = path
        self.save_path = path + '\\封面'

    def listdir(self):
        files = os.listdir(self.path)
        files.remove('封面')
        for each in files:
            fi = os.path.join(self.path, each)
            if os.path.isdir(fi):
                self.copy(each, os.path.join(self.path, each))

    def copy(self, name, path):
        files = os.listdir(path)
        for each in files:
            if not os.path.isdir(os.path.join(path, each)) and (each.find('jpg') > 0 or each.find('png') > 0):
                shutil.copy(os.path.join(path, each), os.path.join(self.save_path, name + each[-4:]))
                print(name + '-----保存成功')
                return

        print(name + "\033[31;49m没有符合的\033[0m")


path = input('请输入路径')
if not os.path.exists(path + '/封面'):
    os.chdir(path)
    os.mkdir('封面')
cover = cover(path)
cover.listdir()
input('运行完成，按任意键退出')
