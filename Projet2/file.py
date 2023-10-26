def open_file(file_name):
    return open(file_name)


def close_file(file_name):
    file_name.close()


def read_file(file):
    print(file.read())


def readline_file(file):
    print(file.readline())


def search_5code_infile(file, recherche):
    code = []
    lines = file.readlines()
    for row in lines:
        for i in range(len(recherche)):
            if recherche[i] in row:
                code.append((row[6:])[:-1])
    return code
