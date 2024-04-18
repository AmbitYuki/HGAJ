from shared_configs import ModelConfig, DataConfig

e = 2.71828


class HGSLConfig(ModelConfig):
    def __init__(self, dataset, seed=12):
        super(HGSLConfig, self).__init__('HGSL')
        default_settings = \
            {'acm': {'alpha': 1, 'dropout': 0.0, 'fgd_th': 0.8, 'fgh_th': 0.2, 'sem_th': 0.6,
                     'mp_list': ['psp', 'pap', 'pspap']},
             'dblp': {'alpha': 0.2, 'dropout': 0.6, 'fgd_th': 0.99, 'fgh_th': 0.99, 'sem_th': 0.4, 'mp_list': ['apcpa','semantic']}, #4.5
             'yelp': {'alpha': 0.5, 'dropout': 0.2, 'fgd_th': 0.8, 'fgh_th': 0.1, 'sem_th': 0.2,
                      'mp_list': ['bub', 'bsb', 'bublb', 'bubsb']}
             }
        self.dataset = dataset
        self.__dict__.update(default_settings[dataset])
        # ! Model settings
        self.lr = 0.001     #0.01
        self.seed = seed
        self.save_model_conf_list()  # * Save the model config list keys
        self.conv_method = 'gcn'
        self.gat_nheads= 2 # GAT模型中head的数量 2
        self.gat_alpha= 0.2  # GAT模型中leaky_relu中alpha的大小
        self.num_head = 8   # 8
        self.early_stop = 1000
        self.adj_norm_order = 1
        self.feat_norm = -1
        self.emb_dim = 64
        self.com_feat_dim = 16          #16
        self.weight_decay = 5e-4
        self.model = 'HGSL'
        self.epochs = 100000
        self.exp_name = 'debug'
        self.save_weights = False
        d_conf = DataConfig(dataset)
        self.__dict__.update(d_conf.__dict__)
