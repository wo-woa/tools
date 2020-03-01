# encoding: utf-8
#
# core write by Wyatt Huang
# https://gitlab.com/wyatthuang
#
# open source follow GPL license
#

from cv2 import imread, imwrite


def txt2Img(photoDir, message, outputFile):
    photo_data = imread(photoDir)

    if outputFile.split('.')[-1].lower() != 'png':
        print()
        raise Exception('The output file type can only be png, or it will cause compress loss')

    def to_bin(inf):
        maxLen = 0
        new = ''
        for i in inf:
            treated = str(bin(ord(i))).replace('0b', '')
            if maxLen < len(treated):
                maxLen = len(treated)
            new += treated + ' '
        return [new[:-1], maxLen]

    def int_to_bin(inf):
        con = str(bin(int(str(inf), 10))).replace('0b', '')
        return con

    # analyze the total length of encode information
    totalLen = int_to_bin(len(message))
    # max length reach 1000000+
    totalLenPointer = int_to_bin(len(totalLen))
    # transfer the format into 5
    totalLenPointer = str(pow(10, 5 - len(totalLenPointer)))[1:] + totalLenPointer

    # transfer the encode information to binary form
    BinaryInf_temp = to_bin(message)
    maxLen = BinaryInf_temp[1]
    BinaryInf = BinaryInf_temp[0].split(' ')
    del BinaryInf_temp  # release memory

    # transfer all the item to have elements of the max one
    for index, nowInf in enumerate(BinaryInf):
        BinaryInf[index] = str(pow(10, maxLen - len(nowInf)))[1:] + nowInf

    # max ASCII length: 31
    # we use 5 length as universal
    lenPerInf = int_to_bin(maxLen)
    lenPerInf = str(pow(10, 5 - len(lenPerInf)))[1:] + lenPerInf

    # compose the write item
    composedInf = lenPerInf + totalLenPointer + totalLen + ''.join(BinaryInf)

    h, w = photo_data.shape[:2]

    flag = True

    # exam the size limit
    if h * w < len(composedInf):
        raise Exception('The picture cannot storage the text!')

    # write into photo
    for x in range(h):
        for y in range(w):
            nowAt = x * h + y
            if nowAt == len(composedInf):
                flag = False
                break
            # even as flat, odd as 1
            photo_data[x, y, 0] += photo_data[x, y, 0] % 2 - int(composedInf[nowAt])
        if not flag:
            break

    imwrite(outputFile, photo_data)


def img2Txt(photoDir):
    photo_data = imread(photoDir)

    if photoDir.split('.')[-1].lower() != 'png':
        raise Exception('Error will happen if the input file type is not png')

    def to_string(inf):
        return chr(int(inf, 2))

    def bin_to_int(inf):
        place = inf.find('1')
        if place == -1:
            return 0
        else:
            # print(inf[place:])
            return int(inf[place:], 2)

    h, w = photo_data.shape[:2]
    composeData = ''
    # for not call warning in program
    totalLenPointer = dataLen = lenPerInf = 1
    flag = False

    for x in range(h):
        for y in range(w):
            nowAt = x * h + y
            # for the none-data indexes
            if nowAt < 10:
                composeData += str(photo_data[x, y, 0] % 2)
                if nowAt == 9:
                    lenPerInf = bin_to_int(composeData[:5])
                    totalLenPointer = bin_to_int(composeData[5:])

            # for the dataLen parameter
            elif nowAt == 10 + totalLenPointer:
                dataLen = bin_to_int(composeData[10:])
                # empty the data container to prepared to contain binary data
                composeData = ''
                # yes, this line is ugly, but if not write like this, it will increase
                # the complex of the whole code
                composeData += str(photo_data[x, y, 0] % 2)

            else:
                if nowAt == dataLen * lenPerInf + totalLenPointer + 10:
                    flag = True
                    break
                composeData += str(photo_data[x, y, 0] % 2)
        if flag:
            break

    message = ''

    # transfer back to string
    for i in range(0, len(composeData), lenPerInf):
        message += to_string(composeData[i:i + lenPerInf])

    return message
