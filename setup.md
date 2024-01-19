# How to run this code

## Setup

### Install dependencies

```bash
conda create -n flx python=3.10 pip -y
conda activate flx
pip install -r requirements.txt
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia

```
### delete the environment

```bash
conda env remove -n flx
```
