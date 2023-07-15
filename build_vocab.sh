#!/bin/bash
# build vocab for different datasets

python ./prepare_vocab.py --data_dir dataset/UIT-ViSFD --vocab_dir dataset/UIT-ViSFD
python ./prepare_vocab.py --data_dir dataset/UIT-ViSD4SA --vocab_dir dataset/UIT-ViSD4SA
