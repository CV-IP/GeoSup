
""" Data preparation script for training depth completion on VISMA2 dataset.
Requirements: vlslam_pb2 generated by vlslam.proto and ROS.
Make sure you have the raw rosbag recorded and dataset file generated by vlslam.
Author: Xiaohan Fei
"""
import argparse, os, sys, glob
sys.path.insert(0, 'setup')
import numpy as np
from absl import logging

# all sequences
sequences = [
        # 'birthplace_of_internet',
        # 'cabinet0',
        # 'classroom0', 'classroom1', 'classroom2', 'classroom3', 'classroom4', 'classroom5', 'classroom6',
        'copyroom0', 'copyroom1', 'copyroom2', 'copyroom3', 'copyroom4',
        # 'corner0', 'corner1', 'corner2', 'corner3', 'corner4',
        # 'couch0', 'couch1',
        # 'desktop0', 'desktop1', 'desktop2',
        # 'kitchen0', 'kitchen1',
        # 'mechanical_lab0', 'mechanical_lab1', 'mechanical_lab2', 'mechanical_lab3', 'mechanical_lab4',
        # 'meeting_area4', 'meeting_area5',
        # 'model',
        # 'office0', 'office1', 'office3',
        # 'pillar0', 'pillar1',
        # 'plants0', 'plants1', 'plants2', 'plants3',
        # 'printers0', 'printers1',
        # 'seasnet0',
        # 'stairs0',
        # 'stairs1',
        # 'stairs3', 'stairs4',
        # 'statues0',
        # 'trashbins0', 'trashbins1',
        # 'visionlab0', 'visionlab1',
        # 'workbench0'
        ]

# testing = ['classroom6', 'copyroom4',
#         'corner3', 'desktop2',
#         'mechanical_lab3', 'office3',
#         'plants3', 'stairs4']


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--recording-dir', default='/local2/Data/rs_d435i_recording',
            help='directory of raw realsense d435i recordings')
    parser.add_argument('--output-root', default='/local2/Data/VISMA2_parsed',
            help='output root for VISMA2')
    parser.add_argument('--debug', default=False, action='store_true',
            help='turn on to visualize saved items')
    parser.add_argument('--temporal-interval', type=int, default=5,
            help='temporal interval (how many frames apart) between consecutive items in the triplets')
    parser.add_argument('--spatial-interval', type=float, default=0.01,
            help='spatial interval (least translation) between consecutive items in the triplets')
    args = parser.parse_args()

    logging.set_verbosity(logging.INFO)

    from setup_one_sequence_visma2 import process_one_sequence
    for seq in sequences:
        args.work_dir = os.path.join(args.recording_dir, seq)
        args.output_dir = os.path.join(args.output_root, seq)
        try:
            process_one_sequence(opt=args)
        except StopIteration:
            logging.warn('StopIteration caught in processing {}'.format(seq))