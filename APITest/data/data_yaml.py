import yaml

def add_yaml_data(file, key=None, values=None,):
    """
    追加内容
    :return:
    """
    data = {key: values}
    with open(file=file, mode='a', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True)
        f.close()

def rand_yaml_data(file, key=None):
    """
    读取
    :return:
    """
    with open(file=file, mode='r', encoding='utf-8') as f:
        data = yaml.load(f)
        # print(type(test_data), test_data)
        f.close()
        return data[key]

if __name__ == "__main__":
    # add_yaml_data()
    print(rand_yaml_data(file='config_data.yaml', key='db'))
    pass
