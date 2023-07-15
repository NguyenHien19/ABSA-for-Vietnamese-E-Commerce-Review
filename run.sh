#!/bin/bash
# * laptop

# * SSEGCN
#python ./train.py --model_name ssegcn --dataset laptop --seed 1000 --num_epoch 40 --vocab_dir ./dataset/Laptops_corenlp --cuda 0  

python ./train.py --model_name ssegcn --dataset ViSFD --seed 1000 --num_epoch 40 --vocab_dir ./dataset/UIT-ViSFD --cuda 0 --max_length 200
# python ./train.py --model_name ssegcn --dataset ViSD4SA --seed 1000 --num_epoch 40 --vocab_dir ./dataset/UIT-ViSD4SA --cuda 0 --max_length 200


# * SSEGCN with Bert
# python ./train.py --model_name ssegcn_bert --dataset laptop --seed 1000 --bert_lr 2e-5 --num_epoch 10 --hidden_dim 768 --max_length 100 --cuda 0  

