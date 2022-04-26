import os
n_gpus = 1
os.environ["CUDA_VISIBLE_DEVICES"] = ','.join(map(str, [0]))
os.system("python3 -m torch.distributed.launch --nproc_per_node={} trainet.py".format(n_gpus))

