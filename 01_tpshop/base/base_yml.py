
import yaml

def yaml_data_with_file(file_name, key):
    with open("./data/" + file_name + ".yml", "r") as f:

        data = yaml.safe_load(f)[key]
        # print(data)
        case_data_list = []

        for case_data in data.values():
            # print(case_data)
            case_data_list.append(case_data)

        return case_data_list








