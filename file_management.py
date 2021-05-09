import json


def load_output_from_json(path):
    with open(path, 'r') as file_handle:
        data = json.load(file_handle)
        mean_values = []
        for benchmark in data["benchmarks"]:
            mean = benchmark["stats"]['mean']
            mean = float("{:.4f}".format(mean))
            mean_values.append(mean)

        return mean_values
