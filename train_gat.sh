
# GAT

nohup python train.py --dataset='yelp' --conv_method='gat' --gat_alpha=0.01 --gat_nheads=1  >./log_yelp_gat_0.01_1.txt 2>&1 &
nohup python train.py --dataset='yelp' --conv_method='gat' --gat_alpha=0.01 --gat_nheads=1  >./log_yelp_gat_0.01_1.txt 2>&1 &

nohup python train.py --dataset='dblp' --conv_method='gat' --gat_alpha=0.01 --gat_nheads=1  >./log_dblp_gat_0.01_1.txt 2>&1 &
nohup python train.py --dataset='dblp' --conv_method='gat' --gat_alpha=0.01 --gat_nheads=8  >./log_dblp_gat_0.01_8.txt 2>&1 &

nohup python train.py --dataset='acm' --conv_method='gat' --gat_alpha=0.01 --gat_nheads=1  >./log_acm_gat_0.01_1.txt 2>&1 &
nohup python train.py --dataset='acm' --conv_method='gat' --gat_alpha=0.01 --gat_nheads=8  >./log_acm_gat_0.01_8.txt 2>&1 &