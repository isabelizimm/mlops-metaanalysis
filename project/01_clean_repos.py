import json

def make_file_list() -> list:
    files = list()
    i = 1
    while i < 11:
        files.append('../data/repos/topic_mlops_pg_'+str(i)+'.json')
        if i < 2:
            files.append('../data/repos/topic_modelmanagement_pg_'+str(i)+'.json')
        i += 1
    return files

def merge_files(files: list):
    result = list()
    for file in files:
        with open(file, 'r') as input_file:
            result.extend(json.load(input_file).get("items"))

    with open('../data/repos/topic_combined.json', 'w') as output_file:
        json.dump(result, output_file)


merge_files(make_file_list())

with open("../data/repos/topic_combined.json", "r") as read_file:
    raw = json.load(read_file)
