import os
import argparse
import json
import numpy as np
import pandas as pd

"""
Computes evaluation metrics on roofnet data and writes them to a json file.

The expected input is a directory including one or .csv files with that contain at least
two columns with the names: transition_true,transition_predicted

"""


def compute_metrics(data):
    """ Computes the average error and true fraction of a dataframe
    Args:
        data: a Pandas dataframe with columns 'transition_true' and 'transition_predicted'
    returns:
        true fraction and avg error
    num_true = 0.0
    total = 0.0
    error = 0.0
    for index, row in data.iterrows():
        total += 1
        true = row['transition_true']
        pred = row['transition_predicted']
        if true == pred:
            num_true += 1
        error += np.abs(float(true) - float(pred))
    fraction_true = float(num_true) / float(total)
    avg_error = error / float(total)

    return fraction_true, avg_error


def main(args):
    results = {}
    results_path = os.path.join(args.csv_dir, 'results.json')
    for f in os.listdir(args.csv_dir):
        if '.csv' in f:
            csv_path = os.path.join(args.csv_dir, f)
            data = pd.read_csv(csv_path)
            frac_true, avg_error = compute_metrics(data)
            metrics = {}
            metrics['fraction_true'] = frac_true
            metrics['avg_error'] = avg_error
            results[str(f)] = metrics
            print(results)
    with open(results_path, 'w+') as result_file:
        json.dump(results, result_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'csv_dir', type=str, help='A directory containing one or more csv files with results')
    args = parser.parse_args()
    main(args)
