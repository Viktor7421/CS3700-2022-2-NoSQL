

conda-update:
	conda env update --prune -f environment.yml

pip-tools:
	python -m pip install pip-tools
	# python -m pip install torch==1.8.1+cu101 torchvision==0.9.1+cu101 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
	pip-compile --find-links=https://download.pytorch.org/whl/torch_stable.html requirements/prod.in && pip-compile requirements/dev.in
	pip-sync requirements/prod.txt requirements/dev.txt

train:
	python training/run_experiment.py --max_epochs=3 --gpus='1,' --data_class=CASIA --model_class=CNN

lint:
	tasks/lint.sh