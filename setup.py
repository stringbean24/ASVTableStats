## `setup.py`

```python
from setuptools import setup, find_packages

setup(
    name='qiime2-seqlen',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'qiime2',
        'pandas',
        'biopython',
        'seaborn',
        'matplotlib',
        'numpy'
    ],
    entry_points={
        'qiime2.plugins': ['seqlen=seqlen_plugin.plugin_setup:plugin']
    }
)
