from database import load_output_from_json
import matplotlib.pyplot as plt
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("title", help="Title of the plot")
    parser.add_argument("path", help="Path to the json file with data")
    parser.add_argument("--color", help="Color of the graph", default='blue')
    args = parser.parse_args()

    mean_values = load_output_from_json(args.path)
    words_numbers = [i*1000 for i in range(1, 11)]  # list [1000, ..., 10000]

    plt.plot(words_numbers, mean_values, args.color)
    plt.ylabel('mean time in sec')
    plt.xlabel('number of elements in list')
    plt.title(args.title)
    png_file = str(args.title) + '.png'
    plt.savefig(png_file)
