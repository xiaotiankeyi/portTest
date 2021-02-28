import yaml


def add_yaml_data(key, value):
    public = {key: value}

    with open(file='yaml_Configdata.yaml', mode='a', encoding='utf-8') as f:
        yaml.dump(public, f, allow_unicode=True)

        f.close()


def rand_yaml_data():
    """
    读取
    :return:
    """
    with open(file='yaml_Configdata.yaml', mode='r', encoding='utf-8') as f:
        data = yaml.load(f)
        print(type(data), data['mysql'])
        f.close()


if __name__ == "__main__":
    # add_yaml_data(key='mysql', value=3306)
    rand_yaml_data()
