from qiime2.plugin import Plugin, Visualizer, Str
from seqlen_plugin.visualize import sequence_length_visualizer

plugin = Plugin(
    name='seqlen',
    version='0.1.0',
    website='https://github.com/YOUR_USERNAME/qiime2-seqlen',
    package='seqlen_plugin',
    description='A plugin to analyze and visualize sequence length distribution.',
    short_description='Visualizes sequence length distribution from QIIME2 data.'
)

plugin.visualizers.register_function(
    function=sequence_length_visualizer,
    inputs={
        'table': 'FeatureTable[Frequency]',
        'sequences': 'FeatureData[Sequence]'
    },
    parameters={},
    input_descriptions={
        'table': 'Feature table containing the ASVs.',
        'sequences': 'Representative sequences corresponding to the ASVs.'
    },
    name='Sequence Length Visualizer',
    description='Generates statistics and a histogram of sequence lengths.',
    outputs=[('visualization', 'Visualization')]
)
