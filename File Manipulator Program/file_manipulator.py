
import sys

#reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
def reverse_inputpath_outputpath(inputpath, outputpath):

    contents = ''

    with open(inputpath) as f:
        contents = f.read()
    
    with open(outputpath, 'w') as f:
        f.write(''.join(list(reversed(contents))))

#copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。
def copy_inputpath_outputpath(inputpath, outputpath):

    contents = ''

    with open(inputpath) as f:
        contents = f.read()

    with open(outputpath, 'w') as f:
        f.write(contents)

#duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
def duplicate_contents_inputpath(inputpath, outputpath, n):

    contens = ''

    with open(inputpath) as f:
        contents = f.read()
    
    with open(outputpath, 'w') as f:
        for i in range(0, int(n)):
            f.write(contents)

#replace-string inputpath needle newstring: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
def replace_string_inputpath_needle_newstring(inputpath):

    with open(inputpath) as f:
        content = f.read()

    with open(inputpath, 'w') as f:
        f.write(content.replace('needle', 'newstring'))


def __main__(argv):

    type = argv[1]

    if type == 'reverse':
        reverse_inputpath_outputpath(argv[2], argv[3])
    elif type == 'copy':
        copy_inputpath_outputpath(argv[2], argv[3])
    elif type == 'duplicate':
        duplicate_contents_inputpath(argv[2], argv[3], argv[4])
    elif type == 'replace':
        replace_string_inputpath_needle_newstring(argv[2])


if __name__ == "__main__":
    __main__(sys.argv)
