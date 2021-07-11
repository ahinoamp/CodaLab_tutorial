#!/usr/bin/env python
import sys
import os
import os.path
import pandas as pd
import numpy as np

input_dir = sys.argv[1]
output_dir = sys.argv[2]

submit_dir = os.path.join(input_dir, 'res')
truth_dir = os.path.join(input_dir, 'ref')

if not os.path.isdir(submit_dir):
    print "%s doesn't exist" % submit_dir

if os.path.isdir(submit_dir) and os.path.isdir(truth_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_filename = os.path.join(output_dir, 'scores.txt')
    output_file = open(output_filename, 'wb')

    truth_file = os.path.join(truth_dir, "test_ref.csv")

    submission_answer_file = os.path.join(submit_dir, "predictions.csv")

    truth = pd.read_csv(truth_file)
    pred = pd.read_csv(submission_answer_file)
    merged = truth.merge(pred, on='data_index', suffixes=('_true', '_pred'), how='left')
	
    result = np.mean(np.abs(merged['target_true'].values-merged['target_pred'].values))

    output_file.write("mae:"+str(result))

    output_file.close()
