import os,hashlib
import numpy as np
from PIL import Image
# from PIL import Image,UnidentifiedImageError
from PIL.Image import DecompressionBombError
from rich import print
from time import time
 
 
print("""[#00CED1]待清理的文件夹内如果还包含了文件夹也同样可以清理![/#00CED1][#0000FF]
@@@@@@@@  @@@  @@@  @@@  @@@  @@@  @@@   @@@@@@   @@@       @@@  @@@   @@@@@@        @@@  @@@  @@@  @@@  
@@@@@@@@  @@@  @@@  @@@  @@@  @@@  @@@  @@@@@@@@  @@@       @@@  @@@  @@@@@@@@       @@@  @@@  @@@@ @@@  
@@!       @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!  @@@  @@!  @@@       @@!  @@!  @@!@!@@@  
!@!       !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!  @!@  !@!  @!@       !@!  !@!  !@!!@!@!  
@!!!:!    @!@  !@!  @!@!@!@!  @!@  !@!  @!@!@!@!  @!!       @!@  !@!  @!@  !@!       !!@  !!@  @!@ !!@!  
!!!!!:    !@!  !!!  !!!@!!!!  !@!  !!!  !!!@!!!!  !!!       !@!  !!!  !@!  !!!       !!!  !!!  !@!  !!!  
!!:       !!:  !!!  !!:  !!!  !!:  !!!  !!:  !!!  !!:       !!:  !!!  !!:  !!!       !!:  !!:  !!:  !!!  
:!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!   :!:      :!:  !:!  :!:  !:!  !!:  :!:  :!:  :!:  !:!  
 ::       ::::: ::  ::   :::  ::::: ::  ::   :::   :: ::::  ::::: ::  ::::: ::  ::: : ::   ::   ::   ::  
 :         : :  :    :   : :   : :  :    :   : :  : :: : :   : :  :    : :  :    : :::    :    ::    :  
[/#0000FF]                                                                  [#00CED1]待清理的文件夹内还包含文件夹也可清理![/#00CED1]""")
path = input(r"输入图片文件夹路径,例如 D:\python\tupian:")
try:
    file = os.walk(path)    # 遍历目录；
except FileNotFoundError:   # 捕获路径不存在异常；
    print('抱歉，没有这个路径！')
else:
    temp = set()    # 创建临时集合；
    del_count = 0   # 删除图片计数；
    pass_count = 0  # 非图片计数；
    file_count = 0  # 总文件计数；
    time1 = time()
    for path_name, dir_name, file_name in file:     # 遍历walk返回3个元素；
        for n in file_name:                         # 获得每个文件名字；
            full_path = os.path.join(path_name, n)  # 拼接路径和文件名，获得文件完整路径；
            file_count += 1                         # 文件计数+1；
            print(full_path)
            try:
                with Image.open(full_path) as t:    # 打开图片；
                    array = np.array(t)             # 转为数组；
            # except (UnidentifiedImageError,DecompressionBombError): # 捕获不是图片，像素炸弹异常；
            #     pass_count += 1                                     # 非图片计数+1；
            #     pass
            except Exception as e:
                print(e)
                pass
            else:
                md5 = hashlib.md5()                                 # 创建MD5对象；
                md5.update(array)                                   # 获取当前图片MD5；
                if md5.hexdigest() not in temp:                     # 如果哈希值没有在集合中；
                    temp.add(md5.hexdigest())                       # 就把哈希值添加到集合中；
                else:
                    os.remove(full_path)                            # 如果在集合中就删除当前图片；
                    print(full_path+'------------------已删除')
                    del_count += 1                                  # 删除计数+1；
 
    time2 = time()
    time3 = time2-time1
    if pass_count != 0:
        print('[#7CFC00]非图片数据：[/#7CFC00][#800000]{0}[/#800000] 个.'.format(pass_count))
    print('[#800080]一共读取图片：[/#800080][#800000]{0}[/#800000] 张.'.format(file_count - pass_count))
    print('[#3CB371]删除重复图片：[/#3CB371][#800000]{0}[/#800000] 张.'.format(del_count))
    print('[#0000FF]总耗时为：[/#0000FF][#800000]{:.4f}[/#800000] 秒.'.format(time3))
input('按任意键结束!!!')  # 此条为了编译成EXE或在命令行运行脚本时能看见上面统计后数据所添加，如果在IDE中运行可删除；
exit()                  # 如果在IDE中运行可删除；