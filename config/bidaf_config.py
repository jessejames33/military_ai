# coding = utf-8
from config import base_config


class ConfigBidaf1(base_config.ConfigBase):
	# model
	algo = 'BIDAF'
	suffix = '_h200'

	# model
	hidden_size = 200

	# loss_type = 'pointer'
	loss_type = 'mrl_mix'
	# loss_type = 'mrl_soft'
	# loss_type = 'mrl_hard'
	# loss_type = 'log_mrl_mix'
	# loss_type = 'log_mrl_soft'
	# loss_type = 'log_mrl_hard'



class ConfigBidaf2(base_config.ConfigBase):
	# model
	algo = 'BIDAF'
	suffix = '_h150'

	# model
	hidden_size = 150

	# loss_type = 'mrl_mix'
	loss_type = 'pointer'


config_1 = ConfigBidaf1()
config_2 = ConfigBidaf2()