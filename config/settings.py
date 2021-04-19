
import os
import os.path as osp
# -----------------------------------------------------------------------------
# Config definition
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Dataset
# -----------------------------------------------------------------------------
ROOT_DIR = osp.abspath(osp.join(osp.dirname(__file__), '..', '..'))
DATA_DIR = osp.abspath('/disk2/caoqinglong/') #data/VOC_new
# DATA_DIR = osp.abspath('/disk2/caoqinglong/VOC/') #data/VOC_new
# Dataloader
mean_vals = [0.485, 0.456, 0.406]
std_vals = [0.229, 0.224, 0.225]
size = 321

# -----------------------------------------------------------------------------
# model
# -----------------------------------------------------------------------------
LR = 8e-4
SNAPSHOT_DIR = os.path.join('snapshots')
