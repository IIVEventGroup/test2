class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/test4/code/EventBenchmark/lib/sotas/OSTrack'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/home/test4/code/EventBenchmark/lib/sotas/OSTrack/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/home/test4/code/EventBenchmark/lib/sotas/OSTrack/pretrained_networks'
        self.lasot_dir = '/home/test4/code/EventBenchmark/data/lasot'
        self.got10k_dir = '/home/test4/code/EventBenchmark/data/got10k/train'
        self.got10k_val_dir = '/home/test4/code/EventBenchmark/data/got10k/val'
        self.lasot_lmdb_dir = '/home/test4/code/EventBenchmark/data/lasot_lmdb'
        self.got10k_lmdb_dir = '/home/test4/code/EventBenchmark/data/got10k_lmdb'
        self.trackingnet_dir = '/home/test4/code/EventBenchmark/data/trackingnet'
        self.trackingnet_lmdb_dir = '/home/test4/code/EventBenchmark/data/trackingnet_lmdb'
        self.coco_dir = '/home/test4/code/EventBenchmark/data/coco'
        self.coco_lmdb_dir = '/home/test4/code/EventBenchmark/data/coco_lmdb'
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = '/home/test4/code/EventBenchmark/data/vid'
        self.imagenet_lmdb_dir = '/home/test4/code/EventBenchmark/data/vid_lmdb'
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = ''
        self.youtubevos_dir = ''
        self.fe240_dir = '/media/group2/data/zhangzikai/FE108/pre_VoxelGrid'
        self.visEvent_dir = '/home/test4/code/EventBenchmark/data/VisEvent'
        self.eventcarla_dir = '/home/test4/code/EventBenchmark/data/EventSOT/EventCARLA/VoxelGrid'
        self.esot500_dir = '/home/test4/code/EventBenchmark/data/EventSOT/EventSOT500/EventSOT500/pre500'
        self.esot2_dir = '/home/test4/code/EventBenchmark/data/EventSOT/EventSOT2'