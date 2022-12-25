class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
path_args = AttrDict(
    {
        # testing result data
        "test_result_direct": "/home/xdzhang/data/apollo7/{}",
        "debug_result_direct": "/home/xdzhang/data/apollo7/debug/{}",
        "spec_path": "Specification/violation_formulae.json",
        # data for training
        "train_data_path": "generator/data/testset/a_testset_for_{}.json",
        # template for generating scenarios quickly
        "template_path": "generator/data/templates/template_for_{}.json",
        # GFlownet model path
        "ckpt": "generator/ckpt/{}_gfn.pkl",
        # proxy path
        "proxy_path": "generator/proxy/model/{}",
        # result path from gfl model
        "in_process_dataset_path": "generator/result/action_sequence_{}.json",
        "new_batch_path": "generator/result/new_action_sequence_{}.json",
        "space_path": "generator/data/action_space/space_for_{}.json"
    }
)