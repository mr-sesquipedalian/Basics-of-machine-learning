<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Consolas'; font-size:10pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    self._make_engine(self.engine)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">1122</span>, in <span style=" color:#ff00ff;">_make_engine</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    self._engine = CParserWrapper(self.f, **self.options)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">1853</span>, in <span style=" color:#ff00ff;">__init__</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    self._reader = parsers.TextReader(src, **kwds)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;pandas/_libs/parsers.pyx&quot;</span>, line <span style=" color:#00ff00;">387</span>, in <span style=" color:#ff00ff;">pandas._libs.parsers.TextReader.__cinit__</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#4682b4;">  File </span><span style=" color:#006400;">&quot;pandas/_libs/parsers.pyx&quot;</span><span style=" color:#4682b4;">, line </span><span style=" color:#006400;">705</span><span style=" color:#4682b4;">, in </span><span style=" color:#9400d3;">pandas._libs.parsers.TextReader._setup_parser_source</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">FileNotFoundError:</span> [Errno 2] File b'Ads_CTR_Optimisation' does not exist: b'Ads_CTR_Optimisation'</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">5</span><span style=" color:#000080;">]:</span> </p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">5</span><span style=" color:#000080;">]:</span> dataset=pd.read_csv('Ads_CTR_Optimisation.csv')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">6</span><span style=" color:#000080;">]:</span> import pandas as pd</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> import matplotlib.pyplot as plt</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> import numpy as np</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> #importing dataset</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> dataset=pd.read_csv('Ads_CTR_Optimisation.csv')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> #implementing random selection</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> import random</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> n=10000</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> d=10</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> ads_selected=[]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> total_reward=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> for i in range(0,n):</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span>     ad=random.randrange(d)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span>     ads_selected.append(ad)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span>     reward=dataset.values[n,ad]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span>     total_reward=total_reward+reward</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> #Viusalising result-Histogram</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> plt.hist('Histogram of ads selection')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> plt.xlabel('AD Number')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> plt.ylabel('No. of times add selected')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> plt.show()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#4682b4;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#4682b4;">  File </span><span style=" color:#006400;">&quot;&lt;ipython-input-6-ff675bcf8b93&gt;&quot;</span><span style=" color:#4682b4;">, line </span><span style=" color:#006400;">17</span><span style=" color:#4682b4;">, in </span><span style=" color:#9400d3;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">    reward=dataset.values[n,ad]</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">IndexError:</span> index 10000 is out of bounds for axis 0 with size 10000</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">7</span><span style=" color:#000080;">]:</span> </p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">7</span><span style=" color:#000080;">]:</span> import random</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> n=10000</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> d=10</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> ads_selected=[]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> total_reward=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> for i in range(0,n):</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span>     ad=random.randrange(d)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span>     ads_selected.append(ad)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span>     reward=dataset.values[i,ad]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span>     total_reward=total_reward+reward</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">8</span><span style=" color:#000080;">]:</span> runfile('C:/Users/Apoorav Gupta/Desktop/Machine Learning/Reinforcement learning(Random Selection).py', wdir='C:/Users/Apoorav Gupta/Desktop/Machine Learning')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#4682b4;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;&lt;ipython-input-8-8bc9ecbbbffc&gt;&quot;</span>, line <span style=" color:#00ff00;">1</span>, in <span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    runfile('C:/Users/Apoorav Gupta/Desktop/Machine Learning/Reinforcement learning(Random Selection).py', wdir='C:/Users/Apoorav Gupta/Desktop/Machine Learning')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\spyder_kernels\customize\spydercustomize.py&quot;</span>, line <span style=" color:#00ff00;">827</span>, in <span style=" color:#ff00ff;">runfile</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    execfile(filename, namespace)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\spyder_kernels\customize\spydercustomize.py&quot;</span>, line <span style=" color:#00ff00;">110</span>, in <span style=" color:#ff00ff;">execfile</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    exec(compile(f.read(), filename, 'exec'), namespace)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;C:/Users/Apoorav Gupta/Desktop/Machine Learning/Reinforcement learning(Random Selection).py&quot;</span>, line <span style=" color:#00ff00;">9</span>, in <span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    dataset=pd.read_csv('Ads_CTR_Optimisation.csv')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">702</span>, in <span style=" color:#ff00ff;">parser_f</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    return _read(filepath_or_buffer, kwds)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">429</span>, in <span style=" color:#ff00ff;">_read</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    parser = TextFileReader(filepath_or_buffer, **kwds)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">895</span>, in <span style=" color:#ff00ff;">__init__</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    self._make_engine(self.engine)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">1122</span>, in <span style=" color:#ff00ff;">_make_engine</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    self._engine = CParserWrapper(self.f, **self.options)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">1853</span>, in <span style=" color:#ff00ff;">__init__</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    self._reader = parsers.TextReader(src, **kwds)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;pandas/_libs/parsers.pyx&quot;</span>, line <span style=" color:#00ff00;">387</span>, in <span style=" color:#ff00ff;">pandas._libs.parsers.TextReader.__cinit__</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#4682b4;">  File </span><span style=" color:#006400;">&quot;pandas/_libs/parsers.pyx&quot;</span><span style=" color:#4682b4;">, line </span><span style=" color:#006400;">705</span><span style=" color:#4682b4;">, in </span><span style=" color:#9400d3;">pandas._libs.parsers.TextReader._setup_parser_source</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">FileNotFoundError:</span> [Errno 2] File b'Ads_CTR_Optimisation.csv' does not exist: b'Ads_CTR_Optimisation.csv'</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">9</span><span style=" color:#000080;">]:</span> </p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">9</span><span style=" color:#000080;">]:</span> plt.hist('Histogram of ads selection')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> plt.xlabel('AD Number')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> plt.ylabel('No. of times add selected')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">   ...:</span> plt.show()</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
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
SOX+H4C4ezFx3+VHAAAAAElFTkSuQmCC
" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">10</span><span style=" color:#000080;">]:</span> import random</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> n=10000</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> d=10</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> ads_selected=[]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> total_reward=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> for i in range(0,n):</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     ad=random.randrange(d)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     ads_selected.append(ad)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     reward=dataset.values[i,ad]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     total_reward=total_reward+reward</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">11</span><span style=" color:#000080;">]:</span> plt.hist('Histogram of ads selection')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('AD Number')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.ylabel('No. of times add selected')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.show()</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
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
SOX+H4C4ezFx3+VHAAAAAElFTkSuQmCC
" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">12</span><span style=" color:#000080;">]:</span> plt.hist(ads_selected)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.title('Histogram of ADS selection')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('AD Number')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.ylabel('No. of times add selected')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.show()</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
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
ga2trb6+ZcuW4ezZsygsLMSUKVMwefJkFBUV1dtu5syZCAwMRGhoKBwdHfH2
22+jpqYGN27cQE1NDZRKJaytrWFtbY3XXnsNt2/frrePGzdu4NSpU/r1rK2t
8fnnn+OXX35BQUEB7t6926xrJr89lsD946nRaPTT3bp103/fsWPHRn8v1LoY
FtRq3N3dkZCQgNu3byMyMhIhISGoqKiATCart66joyNu3Lihn/75558hl8vR
tWtXKJVKqNVq/bKqqioUFhbW2f63+5w3bx769OmDzMxMlJaWYs2aNfqLw4+q
qVqlqNVqHD9+HDt27EC3bt3QrVs37N27FykpKU2ei8/NzcXZs2cxbNiwest+
DcOKigpkZ2fXW25ubo5Vq1bh0qVLOHnyJJKTk7Ft2zY4OzujXbt2KCgo0Id/
aWkpfvzxx3r7cHZ2xvDhw+v8R6G8vBx///vfYW9vj/bt2yMrK6vedg39rh/0
22MJ3D+e3bt3b3I7MjyGBbWaHTt2ID8/H2ZmZrC2tgYAPPXUU3BwcICZmRmu
X7+uX3fatGnYsGEDsrOzUV5ejmXLlmHq1KmQy+UICQnBwYMHcfLkSVRXV2PV
qlWSH/xlZWVQKBTo3Lkzrly5gr///e8t9nM1VauU7du34+mnn8bVq1dx/vx5
nD9/HteuXYOTkxMSEhLqrV9ZWYlvv/0W48ePx8CBAxEUFAQAeP/993HmzBlU
V1fj7t27iI6OhrW1NZ555pl6+/jmm2/www8/QKfTQaFQwNzcHE899RSUSiXG
jBmDt956C6WlpaitrUVWVha+/fbbevsYN24crl27hu3bt6OmpgY1NTU4c+YM
Ll++DDMzM8yZMweLFy/GzZs3odPpkJaWhnv37jX4u35QUFAQrl27hp07d0Kr
1WLXrl24dOkSxo0bJ3ksybAYFtRqvvrqK/Tr1w+dO3fGggULkJiYiPbt26Nj
x45Yvnw5hgwZAmtra6Snp2POnDmYOXMmnn/+efTs2RPt27fHxo0bAdx/0G/j
xo0IDQ2FUqmEpaUlunTpgnbt2jXa9l//+lfs3LkTlpaWePXVVzF16tQW+7ma
qlVKfHw8Xn/9dX2v4tevP/3pT3VORb3xxhuwtLRE165dsXDhQkyaNAlfffUV
zMzu/5OVyWQICwuDvb09HB0d8fXXX+PQoUPo3LlzvTZ/+eUXhISEQKFQwMPD
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
" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">13</span><span style=" color:#000080;">]:</span> plt.hist(ads_selected,ec='black')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.title('Histogram of ADS selection')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('AD Number')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.ylabel('No. of times add selected')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.show()</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
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
wbEAAAAASUVORK5CYII=
" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">14</span><span style=" color:#000080;">]:</span> runfile('C:/Users/Apoorav Gupta/Desktop/Machine Learning/Reinforcement learning(Random Selection).py', wdir='C:/Users/Apoorav Gupta/Desktop/Machine Learning')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#4682b4;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;&lt;ipython-input-14-8bc9ecbbbffc&gt;&quot;</span>, line <span style=" color:#00ff00;">1</span>, in <span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    runfile('C:/Users/Apoorav Gupta/Desktop/Machine Learning/Reinforcement learning(Random Selection).py', wdir='C:/Users/Apoorav Gupta/Desktop/Machine Learning')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\spyder_kernels\customize\spydercustomize.py&quot;</span>, line <span style=" color:#00ff00;">827</span>, in <span style=" color:#ff00ff;">runfile</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    execfile(filename, namespace)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\spyder_kernels\customize\spydercustomize.py&quot;</span>, line <span style=" color:#00ff00;">110</span>, in <span style=" color:#ff00ff;">execfile</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    exec(compile(f.read(), filename, 'exec'), namespace)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;C:/Users/Apoorav Gupta/Desktop/Machine Learning/Reinforcement learning(Random Selection).py&quot;</span>, line <span style=" color:#00ff00;">9</span>, in <span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    dataset=pd.read_csv('Ads_CTR_Optimisation.csv')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">702</span>, in <span style=" color:#ff00ff;">parser_f</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    return _read(filepath_or_buffer, kwds)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">429</span>, in <span style=" color:#ff00ff;">_read</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    parser = TextFileReader(filepath_or_buffer, **kwds)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">895</span>, in <span style=" color:#ff00ff;">__init__</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    self._make_engine(self.engine)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">1122</span>, in <span style=" color:#ff00ff;">_make_engine</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    self._engine = CParserWrapper(self.f, **self.options)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">1853</span>, in <span style=" color:#ff00ff;">__init__</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    self._reader = parsers.TextReader(src, **kwds)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;pandas/_libs/parsers.pyx&quot;</span>, line <span style=" color:#00ff00;">387</span>, in <span style=" color:#ff00ff;">pandas._libs.parsers.TextReader.__cinit__</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#4682b4;">  File </span><span style=" color:#006400;">&quot;pandas/_libs/parsers.pyx&quot;</span><span style=" color:#4682b4;">, line </span><span style=" color:#006400;">705</span><span style=" color:#4682b4;">, in </span><span style=" color:#9400d3;">pandas._libs.parsers.TextReader._setup_parser_source</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">FileNotFoundError:</span> [Errno 2] File b'Ads_CTR_Optimisation.csv' does not exist: b'Ads_CTR_Optimisation.csv'</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">15</span><span style=" color:#000080;">]:</span> </p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">15</span><span style=" color:#000080;">]:</span> import pandas as pd</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import matplotlib.pyplot as plt</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import numpy as np</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> #importing dataset</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> dataset=pd.read_csv('Ads_CTR_Optimisation.csv')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> #implementing random selection</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import random</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> n=10000</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> d=10</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> ads_selected=[]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> total_reward=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> for i in range(0,n):</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     ad=random.randrange(d)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     ads_selected.append(ad)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     reward=dataset.values[i,ad]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     total_reward=total_reward+reward</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> #Viusalising result-Histogram</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.hist(ads_selected,ec='black')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.title('Histogram of ADS selection')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('AD Number')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.ylabel('No. of times add selected')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.show()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#4682b4;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;&lt;ipython-input-15-06cd43b62d5a&gt;&quot;</span>, line <span style=" color:#00ff00;">6</span>, in <span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    dataset=pd.read_csv('Ads_CTR_Optimisation.csv')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">702</span>, in <span style=" color:#ff00ff;">parser_f</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    return _read(filepath_or_buffer, kwds)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">429</span>, in <span style=" color:#ff00ff;">_read</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    parser = TextFileReader(filepath_or_buffer, **kwds)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">895</span>, in <span style=" color:#ff00ff;">__init__</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    self._make_engine(self.engine)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">1122</span>, in <span style=" color:#ff00ff;">_make_engine</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    self._engine = CParserWrapper(self.f, **self.options)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">1853</span>, in <span style=" color:#ff00ff;">__init__</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    self._reader = parsers.TextReader(src, **kwds)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;pandas/_libs/parsers.pyx&quot;</span>, line <span style=" color:#00ff00;">387</span>, in <span style=" color:#ff00ff;">pandas._libs.parsers.TextReader.__cinit__</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#4682b4;">  File </span><span style=" color:#006400;">&quot;pandas/_libs/parsers.pyx&quot;</span><span style=" color:#4682b4;">, line </span><span style=" color:#006400;">705</span><span style=" color:#4682b4;">, in </span><span style=" color:#9400d3;">pandas._libs.parsers.TextReader._setup_parser_source</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">FileNotFoundError:</span> [Errno 2] File b'Ads_CTR_Optimisation.csv' does not exist: b'Ads_CTR_Optimisation.csv'</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">16</span><span style=" color:#000080;">]:</span> </p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">16</span><span style=" color:#000080;">]:</span> import pandas as pd</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import matplotlib.pyplot as plt</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import numpy as np</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> #importing dataset</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> dataset=pd.read_csv('Ads_CTR_Optimisation.csv')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> #implementing random selection</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import random</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> n=10000</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> d=10</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> ads_selected=[]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> total_reward=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> for i in range(0,n):</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     ad=random.randrange(d)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     ads_selected.append(ad)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     reward=dataset.values[i,ad]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     total_reward=total_reward+reward</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> #Viusalising result-Histogram</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.hist(ads_selected,ec='black')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.title('Histogram of ADS selection')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('AD Number')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.ylabel('No. of times add selected')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.show()</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
iVBORw0KGgoAAAANSUhEUgAAAYsAAAEWCAYAAACXGLsWAAAACXBIWXMAAAsS
AAALEgHS3X78AAAAOnpUWHRTb2Z0d2FyZQAACJnLTSwpyMkvyclMUihLLSrO
zM8z1jPUM9BRyCgpKbDS18+Fy+vlF6XrAwCbzxDQcvcyHQAAIABJREFUeJzt
3XtYVOW+B/Dv4OCdAbmog4MggoGKJRcvj5qkKW6OYQoqHk1CirJd3vJE20vm
yQwtNUp3bvZBRE1QycTwsk3N2iGoiFrekhTcMJIiyh2FGd7zh9u1JS4rEWZG
+X6eh0fW9f2xJvj2rsu7FEIIASIiogaYGbsAIiIyfQwLIiKSxbAgIiJZDAsi
IpLFsCAiIlkMCyIiksWwoCbVp08fHDlyxNhlGNXXX38NBwcHdOzYEadOnTJ2
OY22ceNGDB06tMn3++WXX2L06NFNvl9qXgwL+sOcnJxw8ODBGvN+/wfl3Llz
8PX1bXA/2dnZUCgU0Ol0zVGm0c2fPx9r165FaWkp+vfvX+c6Qgg4Ozujd+/e
tZb5+vqibdu2sLCwgEqlgpeXFyIjI3H37l1pncLCQsyYMQNdu3aFhYUFevXq
hRUrVjTbz9RYdX3WU6dOxYEDB4xYFTUGw4KeOMYOoatXr6JPnz4NrvPDDz/g
xo0buHLlCk6cOFFr+dq1a1FSUoK8vDysWrUKCQkJ8Pf3x/1naOfOnYvS0lJc
uHABRUVF2L17N3r27NksPw8RwLCgJvZg7+P48ePw9vaGSqVCly5dMG/ePADA
s88+CwCwsrJCx44dkZqaiurqaixbtgyOjo7o3Lkzpk+fjqKiImm/mzZtgqOj
I2xsbPDBBx/UaOf9999HUFAQpk2bBpVKhY0bN+L48eMYPHgwrKysoFar8eab
b6KyslLan0KhwF//+le4urrCwsICixcvxuXLlzF48GCoVCpMmjSpxvoPqq/W
u3fvomPHjtDr9Xj66acb/OMdFxeHcePGwd/fH3FxcfWu16FDB/j6+mL37t1I
TU3Fnj17AAAnTpzAf//3f6NTp04wMzODm5sbgoKC6tzHnTt3MG3aNNjY2MDK
ygo+Pj64fv06AKCoqAhhYWFQq9Xo1q0bFi1aBL1eX+d+Ll68iFGjRsHa2hpP
PfUUtm/fLi2rqKjA22+/DUdHR1haWmLo0KGoqKio87P+fW/06NGj8PHxgaWl
JXx8fHD06FFpma+vLxYvXowhQ4bAwsICo0ePxs2bN+s9XtSMBNEf5OjoKL79
9tsa82JjY8WQIUPqXGfQoEFi06ZNQgghSkpKRGpqqhBCiKysLAFAVFVVSdvF
xMSInj17isuXL4uSkhIxfvx4MW3aNCGEEOfOnRMdOnQQ//znP8Xdu3fF22+/
LZRKpdTOkiVLhFKpFF9//bXQ6/WivLxcpKeni9TUVFFVVSWysrKEm5ubWLNm
jdQeAPHCCy+IoqIicfbsWdG6dWsxYsQIcfnyZVFYWCjc3d3Fxo0b6zwODdV6
f9+ZmZn1HseysjJhYWEh9uzZIxITE4WNjY24e/eutHz48OHi73//e63thg0b
Jt555x0hhBBhYWGid+/eYsOGDeLSpUv1tiWEEOvXrxdjx44VZWVlQqfTifT0
dFFUVCSEEGLcuHEiPDxclJaWiuvXrwsfHx+xfv16IUTNz7a0tFRoNBqxYcMG
UVVVJU6ePClsbGzE2bNnhRBCvPHGG2L48OEiNzdX6HQ6kZKSIu7cuVPnZ/3g
fgsKCoSVlZXYtGmTqKqqElu3bhVWVlbi5s2b0rFwdnYWv/zyiygvLxfDhw8X
ERERDf681DwYFvSHOTo6ig4dOghLS0vpq127dvWGxbBhw8R7770n8vPza+yn
rj8gI0aMEOvWrZOmL168KJRKpaiqqhJLly4VwcHB0rKysjJhbm5eIyyGDRvW
YO1r1qwRL774ojQNQPz444/StKenp4iMjJSm582bJ2bPnl3nvhqq9f6+GwqL
zZs3C1tbW1FVVSXu3LkjLC0txc6dO6Xl9YXF5MmTxSuvvCKEEKK8vFx8+OGH
wtPTUyiVStGzZ0+xd+/eOtuLiYkRgwcPFmfOnKkx/7fffhOtW7cW5eXl0ryt
W7cKX19fIUTNP+oJCQli6NChNbYPDw8X77//vtDr9aJt27bi9OnTtdqWC4tN
mzYJHx+fGtsMGjRIxMbGSsfigw8+kJatW7dO+Pn51flzUvPiaSh6KLt27UJh
YaH09de//rXedWNiYnDp0iW4ubnBx8cHycnJ9a577do1ODo6StOOjo7Q6XS4
fv06rl27BgcHB2lZ+/btYWNjU2P7B5cDwKVLlzB27Fh07doVKpUKCxYsqHX6
okuXLtL37dq1qzVdWlr60LX+EXFxcZg0aRKUSiXatGmDCRMmNHgq6j6tVgtr
a2upvgULFuDkyZMoKCjApEmTMHHiRNy6davWdi+99BL8/PwQHBwMe3t7vPPO
O6iqqsLVq1dRVVUFtVoNKysrWFlZ4bXXXsONGzdq7ePq1as4duyYtJ6VlRW+
/PJL/Pbbb7h58ybu3LnTqGsmvz+WwL3jqdVqpemuXbtK37dv377ez4WaF8OC
mo2rqyvi4+Nx48YNREREICgoCGVlZVAoFLXWtbe3x9WrV6Xpf/3rX1AqlejS
pQvUajVyc3OlZRUVFSgoKKix/e/3OXPmTLi5uSEzMxPFxcVYvny5dHH4UTVU
q5zc3FwcPnwYW7ZsQdeuXdG1a1ckJiZi7969DZ6Lz8nJwcmTJzFs2LBay+6H
YVlZGbKysmotNzc3x5IlS3D+/HkcPXoUycnJ2LRpExwcHNCmTRvcvHlTCv/i
4mKcO3eu1j4cHBwwfPjwGv+jUFpaii+++AK2trZo27YtLl++XGu7uj7rB/3+
WAL3jme3bt0a3I4Mj2FBzWbLli3Iz8+HmZkZrKysAACtWrWCnZ0dzMzMcOXK
FWndKVOmYM2aNcjKykJpaSkWLFiAyZMnQ6lUIigoCN988w2OHj2KyspKLFmy
RPYPf0lJCVQqFTp27IiLFy/iiy++aLKfq6Fa5WzevBm9evXCL7/8gtOnT+P0
6dO4dOkSNBoN4uPja61fXl6O77//HuPGjcOAAQPg7+8PAPjggw9w4sQJVFZW
4s6dO4iKioKVlRWeeuqpWvv47rvv8PPPP0Ov10OlUsHc3BytWrWCWq3G6NGj
8fbbb6O4uBjV1dW4fPkyvv/++1r7GDt2LC5duoTNmzejqqoKVVVVOHHiBC5c
uAAzMzPMmDED8+bNw7Vr16DX65Gamoq7d+/W+Vk/yN/fH5cuXcLWrVuh0+mw
bds2nD9/HmPHjpU9lmRYDAtqNvv370efPn3QsWNHzJ49GwkJCWjbti3at2+P
hQsXYsiQIbCyskJaWhpmzJiBl156Cc8++yx69OiBtm3b4vPPPwdw70G/zz//
HMHBwVCr1bCwsEDnzp3Rpk2betv+5JNPsHXrVlhYWODVV1/F5MmTm+znaqhW
OXFxcXjjjTekXsX9r9dff73Gqag333wTFhYW6NKlC+bMmYPAwEDs378fZmb3
fmUVCgVCQ0Nha2sLe3t7fPvtt9izZw86duxYq83ffvsNQUFBUKlUcHd3x/Dh
wzFt2jQA9+4yq6ysRO/evdGpUycEBQUhLy+v1j4sLCxw4MABJCQkwN7eHl27
dkVERIT07Mcnn3wCDw8P+Pj4wNraGhEREaiurq7zs36QjY0NkpOTsWrVKtjY
2GDlypVITk6Gra3tH/swyGAUoqn65kQGUlpaCisrK2RmZqJHjx7GLoeoRWDP
gh4L33zzDcrLy1FWVob58+fDw8MDTk5Oxi6LqMVgWNBjISkpCfb29rC3t0dm
ZiYSEhJkL54SUdPhaSgiIpLFngUREcmSv9fvMWRra8vz2UREDyk7O7ve532e
yLBwcnJCenq6scsgInqseHt717uMp6GIiEgWw4KIiGQxLIiISBbDgoiIZDEs
iIhIFsOCiIhkMSyIiEgWw4KIiGQxLIiISBbDwoSoNd2hUCgM/qVs084o7SoU
Cqg13Y192A3OWJ9zSzzWxmKsz7g5P+cncriPx9Vv2hw4RiQbvN2rK8Yapd37
bbc0xvycyTCM9RkDzfc5N1vPYsaMGejcuTP69u0rzbt16xZGjRoFV1dXjBo1
Crdv3wYACCEwa9YsuLi4oF+/fsjIyJC2iYuLg6urK1xdXWu8dpKIiAyn2cLi
5Zdfxv79+2vMi4yMxMiRI5GZmYmRI0ciMjISALBv3z5kZmYiMzMT0dHRmDlz
JoB74bJ06VIcO3YMx48fx9KlS6WAISIiw2m2sHj22WdhbW1dY15SUhJCQkIA
ACEhIdi1a5c0f/r06VAoFBg0aBAKCwuRl5eHf/zjHxg1ahSsra3RqVMnjBo1
qlYAERFR8zPoNYvr169DrVYDANRqNW7cuAEA0Gq1cHBwkNbTaDTQarX1zq9L
dHQ0oqOjAQD5+fnN9SMQEbVIJnE3VF1vdlUoFPXOr0t4eDjS09ORnp4OOzu7
R6rHWHcyEFHT4u9y0zFoz6JLly7Iy8uDWq1GXl4eOnfuDOBejyEnJ0daLzc3
F/b29tBoNDhy5EiN+b6+vs1eJ+9WMaBW5kb55WrVui30lXcM3i4ZFn+Xm45B
wyIgIABxcXF49913ERcXh3Hjxknz165di+DgYBw7dgyWlpZQq9Xw8/PDggUL
pIvaBw4cwEcffWTIkqm56at4uzDRY6DZwmLKlCk4cuQIbt68CY1Gg6VLl+Ld
d9/FpEmTEBMTg+7du2PHjh0AAH9/f+zduxcuLi5o3749YmNjAQDW1tZYvHgx
fHx8AADvvfderYvmRETU/JotLOLj4+ucf+jQoVrzFAoF1q1bV+f6M2bMwIwZ
M5q0NiIiejgmcYGbiIhMG4f7IGopjHQzAcAbCp4EDAuilsJINxMAxruhgDcT
NB2ehiIiIlkMCyIiksWwICIiWQwLIiKSxbAgIiJZDAsiIpLFsCAiIlkMCyIi
ksWwICIiWQwLIiKSxbAgIiJZDAsiIpLFsCAiIlkMCyIiksWwICIiWQwLIiKS
xbAgIiJZDAsiIpLFsCAiIlkMCyIiksWwICIiWQwLIiKSxbAgIiJZyvoWeHh4
QKFQ1LvhTz/91CwFERGR6ak3LJKTkwEA69atAwC89NJLAIAvv/wS7du3N0Bp
RERkKuoNC0dHRwBASkoKUlJSpPmRkZEYMmQI3nvvveavjoiITILsNYuysjL8
+OOP0vTRo0dRVlbWrEUREZFpqbdncV9MTAxmzJiBoqIiKBQKWFpaYsOGDYao
jYiITIRsz8LLywtnzpzBTz/9hNOnT+P06dPw9PR8pEbXrFmDPn36oG/fvpgy
ZQru3LmDrKwsDBw4EK6urpg8eTIqKysBAHfv3sXkyZPh4uKCgQMHIjs7+5Ha
JiKihycbFtevX0dYWBgmT54MS0tLnD9/HjExMY1uUKvV4rPPPkN6ejrOnj0L
vV6PhIQEREREYO7cucjMzESnTp2kNmJiYtCpUyf8+uuvmDt3LiIiIhrdNhER
NY5sWLz88svw8/PDtWvXAAC9evXCp59++kiN6nQ6VFRUQKfToby8HGq1GocP
H0ZQUBAAICQkBLt27QIAJCUlISQkBAAQFBSEQ4cOQQjxSO0TEdHDkQ2Lmzdv
YtKkSTAzu7eqUqlEq1atGt1gt27dMH/+fHTv3h1qtRqWlpbw8vKClZUVlMp7
l1A0Gg20Wi2Aez0RBwcHqW1LS0sUFBTU2m90dDS8vb3h7e2N/Pz8RtdHRES1
yYZFhw4dUFBQID2gl5aWBktLy0Y3ePv2bSQlJSErKwvXrl1DWVkZ9u3bV2u9
++3V1Yuo62HB8PBwpKenIz09HXZ2do2uj4iIapO9G2r16tUICAjA5cuXMWTI
EOTn52PHjh2NbvDgwYPo0aOH9Ad9woQJOHr0KAoLC6HT6aBUKpGbmwt7e3sA
93oZOTk50Gg00Ol0KCoqgrW1daPbJyKihyfbs+jTpw++//57HD16FH/7299w
7tw5uLm5NbrB7t27Iy0tDeXl5RBC4NChQ+jduzeee+45JCYmAgDi4uIwbtw4
AEBAQADi4uIAAImJiRgxYkSDw5AQEVHTkw2LwYMHQ6lUSre6mpubY/DgwY1u
cODAgQgKCoKnpyc8PDxQXV2N8PBwrFixAqtXr4aLiwsKCgoQFhYGAAgLC0NB
QQFcXFywevVqREZGNrptIiJqnHpPQ/3222/QarWoqKjAqVOnpGsHxcXFKC8v
f6RGly5diqVLl9aY5+zsjOPHj9dat23bto902ouIiB5dvWHxj3/8Axs3bkRu
bi7mzZsnzVepVFi+fLlBiiMiItNQb1iEhIQgJCQEX331FQIDAw1ZExERmRjZ
axYnT55EYWGhNH379m0sWrSoWYsiIiLTIhsW+/btg5WVlTTdqVMn7N27t1mL
IiIi0yIbFnq9Hnfv3pWmKyoqakwTEdGTT/ahvGnTpmHkyJEIDQ2FQqHAhg0b
pLGaiIioZZANi3feeQf9+vXDwYMHIYTA4sWL4efnZ4jaiIjIRMiGBQC4u7tD
qVTi+eefR3l5OUpKSmBhYdHctRERkYmQvWbx97//HUFBQXjttdcA3BsF9sUX
X2z2woiIyHTIhsW6deuQkpIClUoFAHB1dcWNGzeavTAiIjIdsmHRpk0btG7d
WprW6XQcyI+IqIWRDYvhw4dj+fLlqKiowLfffouJEyfihRdeMERtRERkImTD
IjIyEnZ2dvDw8MDf/vY3+Pv7Y9myZYaojYiITITs3VBmZmZ49dVX8eqrrxqi
HiIiMkH1hoWHh0eD1yZ++umnZimIiIhMT71hkZycbMg6iIjIhNUbFo6OjtL3
V69eRWZmJp5//nlUVFRAp9MZpDgiIjIND/1QXm5uLh/KIyJqYfhQHhERyeJD
eUREJIsP5RERkSw+lEdERLIe6qG8W7duITc3l6ehiIhaGNmeha+vL4qLi3Hr
1i0888wzCA0Nxbx58wxRGxERmQjZsCgqKoJKpcLOnTsRGhqKkydP4uDBg4ao
jYiITIRsWOh0OuTl5WH79u0YO3asIWoiIiITIxsW7733Hvz8/ODi4gIfHx9c
uXIFrq6uhqiNiIhMhOwF7okTJ2LixInStLOzM7766qtmLYqIiEyLbM+CiIiI
YUFERLIYFkREJKveaxarV69ucEM+a0FE1HLU27MoKSlBSUkJ0tPT8cUXX0Cr
1UKr1WL9+vU4f/78IzVaWFiIoKAguLm5wd3dHampqbh16xZGjRoFV1dXjBo1
Crdv3wYACCEwa9YsuLi4oF+/fsjIyHiktomI6OHVGxZLlizBkiVLcPPmTWRk
ZGDVqlVYtWoVTp48idzc3EdqdPbs2RgzZgwuXryIM2fOwN3dHZGRkRg5ciQy
MzMxcuRIREZGAgD27duHzMxMZGZmIjo6GjNnznyktomI6OHJXrP417/+VWOI
8tatWyM7O7vRDRYXF+OHH35AWFiYtD8rKyskJSUhJCQEABASEoJdu3YBAJKS
kjB9+nQoFAoMGjQIhYWFyMvLa3T7RET08GSfs3jppZcwYMAAjB8/HgqFAl9/
/TWmT5/e6AavXLkCOzs7hIaG4syZM/Dy8kJUVBSuX78OtVoNAFCr1dILlrRa
LRwcHKTtNRoNtFqttO590dHRiI6OBgDk5+c3uj4iIqpNtmexcOFCxMbGolOn
TrCyskJsbCwWLFjQ6AZ1Oh0yMjIwc+ZMnDp1Ch06dJBOOdVFCFFrXl2j3oaH
hyM9PR3p6emws7NrdH1ERFRbvT2LW7duSd87OTnBycmpxjJra+tGNajRaKDR
aDBw4EAAQFBQECIjI9GlSxfk5eVBrVYjLy8PnTt3ltbPycmRts/NzYW9vX2j
2iYiosapt2fh5eUFb29veHl5wc7ODr169YKrqyvs7Ozg5eXV6Aa7du0KBwcH
/PLLLwCAQ4cOoXfv3ggICEBcXBwAIC4uDuPGjQMABAQEYNOmTRBCIC0tDZaW
lrVOQRERUfOqt2eRlZUFAHj99dcREBAAf39/APfuTnrUIco///xzTJ06FZWV
lXB2dkZsbCyqq6sxadIkxMTEoHv37tixYwcAwN/fH3v37oWLiwvat2+P2NjY
R2qbiIgenuwF7hMnTmD9+vXS9J/+9CcsXrz4kRp95plnkJ6eXmv+oUOHas1T
KBRYt27dI7VHRESPRjYsbG1tsWzZMkybNg0KhQJbtmyBjY2NIWojIiITIXs3
VHx8PPLz8zF+/Hi8+OKLuHHjBuLj4w1RGxERmQjZnoW1tTWioqIMUQsREZko
2bDIz8/HypUrce7cOdy5c0eaf/jw4WYtjIiITIfsaaipU6fCzc0NWVlZWLJk
CZycnODj42OI2oiIyETIhkVBQQHCwsJgbm6O4cOHY8OGDUhLSzNEbUREZCJk
T0OZm5sDuDde0549e2Bvb//Io84SEdHjRTYsFi1ahKKiIqxatQpvvfUWiouL
sWbNGkPURkREJkI2LMaOHQsAsLS0xHfffdfsBRERkenhO7iJiEgWw4KIiGQx
LIiISJZsWERFRaG4uBhCCISFhcHT0xMHDhwwRG1ERGQiZMNiw4YNUKlUOHDg
APLz8xEbG4t3333XELUREZGJkA2L+6813bt3L0JDQ/H000/X+apTIiJ6csmG
hZeXF0aPHo29e/fCz88PJSUlMDPjpQ4iopZE9jmLmJgYnD59Gs7Ozmjfvj0K
Cgr4tjoiohZGtougUChw/vx5fPbZZwCAsrKyGqPPEhHRk082LN544w2kpqZK
LzyysLDAn//852YvjIiITIfsaahjx44hIyMD/fv3BwB06tQJlZWVzV4YERGZ
Dtmehbm5OfR6PRQKBYB7L0PiBW4iopZF9q/+rFmzMH78eNy4cQMLFy7E0KFD
sWDBAkPURkREJkL2NNTUqVPh5eWFQ4cOQQiBXbt2wd3d3RC1ERGRiZANCwDo
0qULhg0bBp1Oh4qKCmRkZMDT07O5ayMiIhMhGxaLFy/Gxo0b0bNnT+m6hUKh
wOHDh5u9OCIiMg2yYbF9+3ZcvnwZrVu3NkQ9RERkgmQvcPft2xeFhYWGqIWI
iEyUbM/iL3/5C/r374++ffuiTZs20vzdu3c3a2FERGQ6ZMMiJCQEERER8PDw
4PMVREQtlGxY2NraYtasWYaohYiITJRsWHh5eeEvf/kLAgICapyG4q2zREQt
h2xYnDp1CgCQlpYmzWuKW2f1ej28vb3RrVs3JCcnIysrC8HBwbh16xY8PT2x
efNmtG7dGnfv3sX06dNx8uRJ2NjYYNu2bXBycnqktomI6OHIhsV3333XLA1H
RUXB3d0dxcXFAICIiAjMnTsXwcHBeP311xETE4OZM2ciJiYGnTp1wq+//oqE
hARERERg27ZtzVITERHVrd4r1lu2bAEArF69us6vR5Gbm4s9e/bglVdeAXDv
1a2HDx9GUFAQgHsX1Xft2gUASEpKQkhICAAgKChIGnaEiIgMp96eRVlZGQCg
pKSk1rL7T3I31pw5c7By5Upp3wUFBbCysoJSea8cjUYDrVYLANBqtXBwcLhX
rFIJS0tLFBQUwNbWtsY+o6OjER0dDeDeyLhERNR06g2L1157DQDw/PPPY8iQ
ITWWpaSkNLrB5ORkdO7cGV5eXjhy5AgA1NlTuB9IDS17UHh4OMLDwwEA3t7e
ja6PiIhqk31w4q233vpD8/6olJQU7N69G05OTggODsbhw4cxZ84cFBYWQqfT
Abh3msre3h7AvV5GTk4OAECn06GoqAjW1taNbp+IiB5evT2L1NRUHD16FPn5
+TWuURQXF0Ov1ze6wY8++ggfffQRAODIkSP45JNP8OWXX2LixIlITExEcHAw
4uLiMG7cOABAQEAA4uLiMHjwYCQmJmLEiBGPfBqMiIgeTr09i8rKSpSWlkKn
06GkpET6UqlUSExMbPJCVqxYgdWrV8PFxQUFBQUICwsDAISFhaGgoAAuLi5Y
vXo1IiMjm7xtIiJqWL09i+HDh2P48OF4+eWX4ejo2CyN+/r6wtfXFwDg7OyM
48eP11qnbdu22LFjR7O0T0REf4zsNYvmCgoiInp8cGRAIiKSVW9YREREAABP
ARERUf1hsXfvXlRVVUl3LhERUctV7wXuMWPGwNbWFmVlZVCpVBBCQKFQSP/e
H9OJiIiefPX2LD7++GMUFRXhv/7rv1BcXIySkpIa/xIRUcshO+psUlISrl+/
jhMnTgAABg4cCDs7u2YvjIiITIfs3VA7duzAgAEDsGPHDmzfvh0DBgxolofy
iIjIdMn2LJYtW4YTJ06gc+fOAO6N6Pr8889Lw4kTEdGTT7ZnUV1dLQUFANjY
2KC6urpZiyIiItMi27MYM2YM/Pz8MGXKFADAtm3b4O/v3+yFERGR6ZANi48/
/hg7d+7Ejz/+CCEEwsPDMX78eEPURkREJkI2LABgwoQJmDBhQnPXQkREJopj
QxERkSyGBRERyWJYEBGRrEaFxfvvv9/EZRARkSlrVFh4eXk1dR1ERGTCGhUW
L7zwQlPXQUREJkw2LHJzczF+/HjY2dmhS5cuCAwMRG5uriFqIyIiEyEbFqGh
oQgICEBeXh60Wi1eeOEFhIaGGqI2IiIyEbJhkZ+fj9DQUCiVSiiVSrz88svI
z883RG1ERGQiZMPC1tYWW7ZsgV6vh16vx5YtW2BjY2OI2oiIyETIhsWGDRuw
fft2dO3aFWq1GomJidiwYYMhaiMiIhMhOzZU9+7dsXv3bkPUQkREJqresPjf
//3fejdSKBRYvHhxsxRERESmp96w6NChQ615ZWVliImJQUFBAcOCiKgFqTcs
3n77ben7kpISREVFITY2FsHBwTWWERHRk6/BC9y3bt3CokWL0K9fP+h0OmRk
ZGDFihU1XrNKRERPvnp7Fv/zP/+DnTt3Ijw8HD///DM6duxoyLqIiMiE1Nuz
WLVqFa5du4Zly5bB3t4eKpUKKpUKFhYWUKlUhqyRiIiMrN6wqK6uRkVFBUpK
SlBcXCx93Z9urJycHDz33HNwd3dHnz59EBUVBeDeKa9Ro0bB1dUVo0aNwu3b
twEAQgjMmjULLi4u6NevHzIyMhrdNhERNY7BX36kVCqxatUqXLhwAWlpaVhF
oYtsAAAJ3ElEQVS3bh3Onz+PyMhIjBw5EpmZmRg5ciQiIyMBAPv27UNmZiYy
MzMRHR2NmTNnGrpkIqIWz+BhoVar4enpCQCwsLCAu7s7tFotkpKSEBISAgAI
CQnBrl27AABJSUmYPn06FAoFBg0ahMLCQuTl5Rm6bCKiFs2or1XNzs7GqVOn
MHDgQFy/fh1qtRrAvUC5ceMGAECr1cLBwUHaRqPRQKvV1tpXdHQ0vL294e3t
zYEOiYiamNHCorS0FIGBgfj0008bvGAuhKg1T6FQ1JoXHh6O9PR0pKenw87O
rklrJSJq6YwSFlVVVQgMDMTUqVMxYcIEAECXLl2k00t5eXnSsxwajQY5OTnS
trm5ubC3tzd80URELZjBw0IIgbCwMLi7u2PevHnS/ICAAMTFxQEA4uLiMG7c
OGn+pk2bIIRAWloaLC0tpdNVRERkGLKjzja1lJQUbN68GR4eHnjmmWcAAMuX
L8e7776LSZMmISYmBt27d8eOHTsAAP7+/ti7dy9cXFzQvn17xMbGGrpkIqIW
z+BhMXTo0DqvQwDAoUOHas1TKBRYt25dc5dFREQNMOrdUERE9HhgWBARkSyG
BRERyWJYEBGRLIYFERHJYlgQEZEshgUREcliWBARkSyGBRERyWJYEBGRLIYF
ERHJYlgQEZEshgUREcliWBARkSyGBRERyWJYEBGRLIYFERHJYlgQEZEshgUR
EcliWBARkSyGBRERyWJYEBGRLIYFERHJYlgQEZEshgUREcliWBARkSyGBRER
yWJYEBGRLIYFERHJYlgQEZEshgUREcliWBARkazHJiz279+Pp556Ci4uLoiM
jDR2OURELcpjERZ6vR5//vOfsW/fPpw/fx7x8fE4f/68scsiImoxHouwOH78
OFxcXODs7IzWrVsjODgYSUlJxi6LiKjFUAghhLGLkJOYmIj9+/fj//7v/wAA
mzdvxrFjx7B27VppnejoaERHRwMALl68CDc3t0a3l5+fDzs7u0cr+gnBY1ET
j8d/8FjU9CQcj+zsbNy8ebPOZUoD19IodeWZQqGoMR0eHo7w8PAmac/b2xvp
6elNsq/HHY9FTTwe/8FjUdOTfjwei9NQGo0GOTk50nRubi7s7e2NWBERUcvy
WISFj48PMjMzkZWVhcrKSiQkJCAgIMDYZRERtRiPxWkopVKJtWvXws/PD3q9
HjNmzECfPn2arb2mOp31JOCxqInH4z94LGp60o/HY3GBm4iIjOuxOA1FRETG
xbAgIiJZDIsHcEiR/8jJycFzzz0Hd3d39OnTB1FRUcYuyej0ej369++PsWPH
GrsUoyssLERQUBDc3Nzg7u6O1NRUY5dkVGvWrEGfPn3Qt29fTJkyBXfu3DF2
SU2OYfFvHFKkJqVSiVWrVuHChQtIS0vDunXrWvTxAICoqCi4u7sbuwyTMHv2
bIwZMwYXL17EmTNnWvRx0Wq1+Oyzz5Ceno6zZ89Cr9cjISHB2GU1OYbFv3FI
kZrUajU8PT0BABYWFnB3d4dWqzVyVcaTm5uLPXv24JVXXjF2KUZXXFyMH374
AWFhYQCA1q1bw8rKyshVGZdOp0NFRQV0Oh3Ky8ufyOfAGBb/ptVq4eDgIE1r
NJoW/cfxQdnZ2Th16hQGDhxo7FKMZs6cOVi5ciXMzPgrc+XKFdjZ2SE0NBT9
+/fHK6+8grKyMmOXZTTdunXD/Pnz0b17d6jValhaWmL06NHGLqvJ8b/8f/sj
Q4q0RKWlpQgMDMSnn34KlUpl7HKMIjk5GZ07d4aXl5exSzEJOp0OGRkZmDlz
Jk6dOoUOHTq06Gt8t2/fRlJSErKysnDt2jWUlZVhy5Ytxi6ryTEs/o1DitRW
VVWFwMBATJ06FRMmTDB2OUaTkpKC3bt3w8nJCcHBwTh8+DCmTZtm7LKMRqPR
QKPRSD3NoKAgZGRkGLkq4zl48CB69OgBOzs7mJubY8KECTh69Kixy2pyDIt/
45AiNQkhEBYWBnd3d8ybN8/Y5RjVRx99hNzcXGRnZyMhIQEjRox4Iv/P8Y/q
2rUrHBwc8MsvvwAADh06hN69exu5KuPp3r070tLSUF5eDiEEDh069ERe8H8s
hvswBEMPKWLqUlJSsHnzZnh4eOCZZ54BACxfvhz+/v5GroxMweeff46pU6ei
srISzs7OiI2NNXZJRjNw4EAEBQXB09MTSqUS/fv3fyKH/uBwH0REJIunoYiI
SBbDgoiIZDEsiIhIFsOCiIhkMSyIiEgWw4IIwNdffw2FQoGLFy9K87Kzs9Gu
XTv0798f7u7uGDBgAOLi4urc/siRI1AoFPjmm2+keWPHjsWRI0eapD4nJyfc
vHmzSfZF1BgMCyIA8fHxGDp0aK3RQnv27IlTp07hwoULSEhIwJo1a+p9pkCj
0eDDDz80RLkPRafTGbsEegIwLKjFKy0tRUpKCmJiYhocWtrZ2RmrV6/GZ599
Vufyp59+GpaWlvj2229rLXuwZ5Ceng5fX18AwPvvv4+QkBCMHj0aTk5O2Llz
J9555x14eHhgzJgxqKqqkvbx8ccfY8CAARgwYAB+/fVXAEB+fj4CAwPh4+MD
Hx8fpKSkSPsNDw/H6NGjMX369EYdF6IHMSyoxdu1axfGjBmDXr16wdrausFx
jjw9PWucqvq9RYsWYdmyZQ/V/uXLl7Fnzx4kJSVh2rRpeO655/Dzzz+jXbt2
2LNnj7SeSqXC8ePH8eabb2LOnDkA7r1XYu7cuThx4gS++uqrGkOonzx5EklJ
Sdi6detD1UNUFw73QS1efHy89Mc3ODgY8fHx0rs8fk9uwINhw4YBAP75z3/+
4fb/9Kc/wdzcHB4eHtDr9RgzZgwAwMPDA9nZ2dJ6U6ZMkf6dO3cugHuD2D34
Uqri4mKUlJQAAAICAtCuXbs/XAdRQxgW1KIVFBTg8OHDOHv2LBQKBfR6PRQK
BVauXFnn+qdOnZIdJG7hwoX48MMPoVT+59dLqVSiuroaAGq9crNNmzYAADMz
M5ibm0tD45uZmdW43vDgkPn3v6+urkZqamqdodChQ4cG6yR6GDwNRS1aYmIi
pk+fjqtXryI7Oxs5OTno0aMHfvzxx1rrZmdnY/78+Xjrrbca3Ofo0aNx+/Zt
nDlzRprn5OSEkydPAgC++uqrRtW6bds26d/BgwdLba1du1Za5/Tp043aN5Ec
hgW1aPHx8Rg/fnyNeYGBgdJ5/suXL0u3zk6aNAlvvfUWQkNDZfe7cOFC5Obm
StNLlizB7NmzMWzYMLRq1apRtd69excDBw5EVFQU1qxZAwDSu5/79euH3r17
Y/369Y3aN5EcjjpLRESy2LMgIiJZDAsiIpLFsCAiIlkMCyIiksWwICIiWQwL
IiKSxbAgIiJZ/w8qjyYWy2DXtQAAAABJRU5ErkJggg==
" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">17</span><span style=" color:#000080;">]:</span> import pandas as pd</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import matplotlib.pyplot as plt</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import numpy as np</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> #importing dataset</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> dataset=pd.read_csv('Ads_CTR_Optimisation.csv')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">18</span><span style=" color:#000080;">]:</span> N=10000</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> d=10</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> ads_selected=[]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> numbers_of_selections= [0]*d</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> sums_of_rewards= [0]*d</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> total_reward=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> for n in range(0,N):</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     ad=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     max_upper_bound=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     for i in range(0,d):</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         if numbers_of_selections[i]&gt;0:</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             average_reward=sums_of_rewards[i]/numbers_of_selections[i]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             delta_i=math.sqrt(1.5*math.log(n+1)/numbers_of_selections[i])</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             upper_bound=average_reward+delta_i</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         else:</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             upper_bound=1e400</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         if upper_bound&gt;max_upper_bound:</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             max_upper_bound=upper_bound</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             ad=i</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     ads_selected.append(ad)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     numbers_of_selections[ad]=numbers_of_selections[ad]+1</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     reward=dataset.values[n,ad]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     sums_of_rewards[ad]=sums_of_rewards[ad]+reward</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     total_reward=total_reward+reward</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#4682b4;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#4682b4;">  File </span><span style=" color:#006400;">&quot;&lt;ipython-input-18-e2f322c9bd58&gt;&quot;</span><span style=" color:#4682b4;">, line </span><span style=" color:#006400;">14</span><span style=" color:#4682b4;">, in </span><span style=" color:#9400d3;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">    delta_i=math.sqrt(1.5*math.log(n+1)/numbers_of_selections[i])</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">NameError:</span> name 'math' is not defined</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">19</span><span style=" color:#000080;">]:</span> </p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">19</span><span style=" color:#000080;">]:</span> import pandas as pd</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import matplotlib.pyplot as plt</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import numpy as np</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import math</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">20</span><span style=" color:#000080;">]:</span> dataset=pd.read_csv('Ads_CTR_Optimisation.csv')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">21</span><span style=" color:#000080;">]:</span> N=10000</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> d=10</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> ads_selected=[]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> numbers_of_selections= [0]*d</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> sums_of_rewards= [0]*d</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> total_reward=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> for n in range(0,N):</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     ad=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     max_upper_bound=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     for i in range(0,d):</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         if numbers_of_selections[i]&gt;0:</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             average_reward=sums_of_rewards[i]/numbers_of_selections[i]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             delta_i=math.sqrt(1.5*math.log(n+1)/numbers_of_selections[i])</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             upper_bound=average_reward+delta_i</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         else:</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             upper_bound=1e400</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         if upper_bound&gt;max_upper_bound:</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             max_upper_bound=upper_bound</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             ad=i</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     ads_selected.append(ad)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     numbers_of_selections[ad]=numbers_of_selections[ad]+1</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     reward=dataset.values[n,ad]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     sums_of_rewards[ad]=sums_of_rewards[ad]+reward</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     total_reward=total_reward+reward</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">22</span><span style=" color:#000080;">]:</span> plt.hist(numbers_of_selections,ec='black')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.title('Histogram of Ads')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xtitle('AD NO.')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.ylabel('No. of selections')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.show()</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#4682b4;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#4682b4;">  File </span><span style=" color:#006400;">&quot;&lt;ipython-input-22-91e056c2adb7&gt;&quot;</span><span style=" color:#4682b4;">, line </span><span style=" color:#006400;">3</span><span style=" color:#4682b4;">, in </span><span style=" color:#9400d3;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">    plt.xtitle('AD NO.')</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">AttributeError:</span> module 'matplotlib.pyplot' has no attribute 'xtitle'</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
iVBORw0KGgoAAAANSUhEUgAAAWoAAAEICAYAAAB25L6yAAAACXBIWXMAAAsS
AAALEgHS3X78AAAAOnpUWHRTb2Z0d2FyZQAACJnLTSwpyMkvyclMUihLLSrO
zM8z1jPUM9BRyCgpKbDS18+Fy+vlF6XrAwCbzxDQcvcyHQAAGPNJREFUeJzt
3Xts1fX9x/FXacELbenEFlqLvVFsKZcCByoREUnK3GQ6oEAZ1U3njtMtwznU
xGUrZEacmUGHuKWTCWIoS8icAsJUcF6gWI8UM3AgKS2j4KCUa1tKT9v37w/0
/KgUTt16Dp/C85E04Zzz7fe8P3D69Pj9ntMTYWYmAICzelzsAQAAF0aoAcBx
hBoAHEeoAcBxhBoAHEeoAcBxhBpdIicnR//4xz8u9hgX1auvvqoBAwYoOjpa
FRUV//P+5s2bp6Kioi6YDN0doUZQqampevvtt9tdt3TpUo0bNy5weceOHZow
YcIF91NdXa2IiAi1tLSEYsyLbu7cuXr++edVX1+vESNGdLiNmSk9PV2DBw8O
83Tozgg1LhkX+z8Ae/fuVU5OzgW3ee+993To0CHt2bNHH330UZgmQ3dHqNEl
zn7WXV5eLo/Ho9jYWPXr108PP/ywJGn8+PGSpLi4OEVHR6usrExtbW164okn
lJKSooSEBN199906fvx4YL8vv/yyUlJS1LdvX/3mN79pdz/z5s1TQUGBioqK
FBsbq6VLl6q8vFxjx45VXFycEhMT9dOf/lTNzc2B/UVEROiFF15QZmamYmJi
9Ktf/UqVlZUaO3asYmNjNWPGjHbbn+18s54+fVrR0dFqbW3V8OHDlZGRcd6/
p2XLlunOO+/Ut7/9bS1btqzdbVVVVbrlllsUExOj/Px8HT58OHBbU1OTioqK
1LdvX8XFxWn06NE6ePDg1/knQndmQBApKSn21ltvtbvupZdesptuuqnDbW68
8UZ7+eWXzczs5MmTVlZWZmZmVVVVJsn8fn/g+5YsWWIZGRlWWVlpJ0+etClT
plhRUZGZme3YscN69+5t77//vp0+fdp+8YtfWFRUVOB+iouLLSoqyl599VVr
bW21xsZG8/l8VlZWZn6/36qqqiwrK8sWLlwYuD9J9p3vfMeOHz9u27dvt169
etnEiROtsrLSjh07ZtnZ2bZ06dIO/x4uNOuX+969e/d5/x4bGhosJibG1q5d
a6tWrbK+ffva6dOnA7ffeOON9vOf/9yamprs3XfftejoaJs9e7aZmf3xj3+0
yZMnW0NDg7W0tJjP57Pjx4+f975waSHUCColJcV69+5tffr0CXxdddVV5w31
zTffbL/+9a+ttra23X46CvXEiRNt8eLFgcs7d+60qKgo8/v9Nn/+fCssLAzc
1tDQYD179mwX6ptvvvmCsy9cuNC++93vBi5Lsg8++CBweeTIkfbUU08FLj/8
8MM2Z86cDvd1oVm/3PeFQr18+XK79tprze/3W1NTk/Xp08f++te/mpnZ3r17
LTIy0urr6wPbz5o1KxDqJUuW2NixY+2TTz654HpxaeLQBzrlb3/7m44dOxb4
euGFF8677ZIlS/TZZ58pKytLo0eP1po1a8677YEDB5SSkhK4nJKSopaWFh08
eFAHDhzQgAEDArddffXV6tu3b7vvP/t2Sfrss880efJk9e/fX7GxsXr88cfb
HUKQpH79+gX+fNVVV51zub6+/mvP2hnLli3TjBkzFBUVpSuuuEJTp04NHP44
cOCAvvGNb6h3797t9v+lu+66S9/85jdVWFiopKQkPfroo/L7/Z26X3R/hBpd
LjMzU6WlpTp06JAee+wxFRQUqKGhQREREedsm5SUpL179wYu//vf/1ZUVJT6
9eunxMRE1dTUBG47deqU6urq2n3/V/f5wAMPKCsrS7t379aJEyf05JNPyrro
F0ReaNZgampqtHHjRr3yyivq37+/+vfvr1WrVumNN97Q4cOHlZiYqKNHj6qh
oaHd/r/Us2dPFRcX69NPP9XmzZu1Zs0avfzyy12yLriPUKPLvfLKK6qtrVWP
Hj0UFxcnSYqMjFR8fLx69OihPXv2BLadNWuWFi5cqKqqKtXX1+vxxx/XzJkz
FRUVpYKCAq1evVqbN29Wc3OziouLg0b35MmTio2NVXR0tHbu3Kk//OEPXbau
C80azPLlyzVo0CDt2rVL27Zt07Zt2/TZZ58pOTlZpaWlSklJkcfjUXFxsZqb
m/XBBx9o9erVge9/55139M9//lOtra2KjY1Vz549FRkZ2WVrg9sINbrc+vXr
lZOTo+joaM2ZM0crV67UlVdeqauvvlq//OUvddNNNykuLk5btmzRvffeq7vu
ukvjx49XWlqarrzySi1atEjSmTfRLFq0SIWFhUpMTFRMTIwSEhJ0xRVXnPe+
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
paXhmAMAcB4c+gAAxxFqAHAcoQYAxxFqAHAcoQYAxxFqAHAcoQYAxxFqAHAc
oQYAxxFqAHAcoQYAxxFqAHAcoQYAxxFqAHAcoQYAxxFqAHAcoQYAx3Uq1OvX
r9cNN9yggQMH6qmnngr1TACAswQNdWtrq37yk59o3bp1+vTTT1VaWqpPP/00
HLMBANSJUJeXl2vgwIFKT09Xr169VFhYqNdeey0cswEAJEWYmV1og1WrVmn9
+vV68cUXJUnLly/Xhx9+qOeff77ddiUlJSopKZEk7dy5U1lZWR3ur7a2VvHx
8V0x+0V1KayDNbjjUlgHa/jfVFdX6/Dhwx3eFvRTyDvqeERExDnXeb1eeb3e
oMN4PB75fL6g27nuUlgHa3DHpbAO1hA6QQ99JCcna9++fYHLNTU1SkpKCulQ
AID/FzTUo0eP1u7du1VVVaXm5matXLlSd9xxRzhmAwBIipw3b968C23Qo0cP
ZWZmqqioSIsWLVJRUZGmTZv2P93pqFGj/qfvd8WlsA7W4I5LYR2sITSCnkwE
AFxcvDMRABxHqAHAcWENtctvRb/33nuVkJCgIUOGBK47cuSI8vPzlZmZqfz8
fB09elTSmZcs/uxnP9PAgQM1bNgwbd26NfA9y5YtU2ZmpjIzM7Vs2bKwrmHf
vn269dZblZ2drZycHD333HPdch1NTU0aM2aMhg8frpycHBUXF0uSqqqqlJeX
p8zMTM2cOVPNzc2SpNOnT2vmzJkaOHCg8vLyVF1dHdjXggULNHDgQN1www36
+9//HtZ1SGfe2TtixAhNnjy5W64hNTVVQ4cOVW5urjwej6Tu93g6duyYCgoK
lJWVpezsbJWVlXW7NcjCpKWlxdLT062ystJOnz5tw4YNsx07doTr7oN69913
7eOPP7acnJzAdY888ogtWLDAzMwWLFhgjz76qJmZrV271m677TZra2uzsrIy
GzNmjJmZ1dXVWVpamtXV1dmRI0csLS3Njhw5ErY1HDhwwD7++GMzMztx4oRl
Zmbajh07ut062tra7OTJk2Zm1tzcbGPGjLGysjKbPn26lZaWmpnZ/fffby+8
8IKZmS1evNjuv/9+MzMrLS21GTNmmJnZjh07bNiwYdbU1GR79uyx9PR0a2lp
Cds6zMyeeeYZmzVrlt1+++1mZt1uDSkpKVZbW9vuuu72eLr77rvtT3/6k5mZ
nT592o4ePdrt1hC2UG/evNkmTZoUuPzkk0/ak08+Ga6775Sqqqp2oR40aJAd
OHDAzM5EcNCgQWZm5vV6bcWKFedst2LFCvN6vYHrv7pduN1xxx325ptvdut1
NDQ02IgRI2zLli3Wt29f8/v9Ztb+8TRp0iTbvHmzmZn5/X7r27evtbW1nfMY
O3u7cNi3b59NnDjRNmzYYLfffru1tbV1uzV0FOru9Hg6fvy4paamWltbW7vr
u9MazMzCduhj//79GjBgQOBycnKy9u/fH667/68cPHhQiYmJkqTExEQdOnRI
0vnX4tIaq6urVVFRoby8vG65jtbWVuXm5iohIUH5+fnKyMhQXFycoqKizpnp
7HmjoqLUp08f1dXVXfR1PPTQQ3r66afVo8eZH7O6urput4aIiAhNmjRJo0aN
CvyKiO70eNqzZ4/i4+N1zz33aMSIEbrvvvvU0NDQrdYghfEYtXXyrejdwfnW
4soa6+vrNW3aND377LOKjY0973YuryMyMlLbtm1TTU2NysvL9a9//eu8M7m4
jjVr1ighIaHda3IvNI+La5CkTZs2aevWrVq3bp0WL16s995777zburiGlpYW
bd26VQ888IAqKirUu3fvC54fc3ENUhhD3R3fit6vXz99/vnnkqTPP/9cCQkJ
ks6/FhfW6Pf7NW3aNM2ePVtTp06V1D3X8aW4uDhNmDBBW7Zs0bFjx9TS0nLO
TGfP29LSouPHj+uaa665qOvYtGmTXn/9daWmpqqwsFAbN27UQw891K3WIClw
XwkJCZoyZYrKy8u71eMpOTlZycnJysvLkyQVFBRo69at3WoNksJ3MtHv91ta
Wprt2bMncDJx+/bt4br7TvnqMeq5c+e2O+HwyCOPmJnZmjVr2p1wGD16tJmd
OeGQmppqR44csSNHjlhqaqrV1dWFbf62tja76667bM6cOe2u727rOHTokB09
etTMzBobG23cuHG2evVqKygoaHcibvHixWZm9vzzz7c7ETd9+nQzM9u+fXu7
E3FpaWlhP5loZvbOO+8ETiZ2pzXU19fbiRMnAn8eO3asrVu3rts9nsaNG2c7
d+40M7Pi4mKbO3dut1tD2EJtduaMamZmpqWnp9sTTzwRzrsOqrCw0Pr3729R
UVF23XXX2YsvvmiHDx+2iRMn2sCBA23ixImBf5i2tjZ78MEHLT093YYMGWIf
ffRRYD9LliyxjIwMy8jIsD//+c9hXcP7779vkmzo0KE2fPhwGz58uK1du7bb
reOTTz6x3NxcGzp0qOXk5Nj8+fPNzKyystJGjx5tGRkZVlBQYE1NTWZmdurU
KSsoKLCMjAwbPXq0VVZWBvb1xBNPWHp6ug0aNMjeeOONsK7jS2eHujutobKy
0oYNG2bDhg2zwYMHB35mu9vjqaKiwkaNGmVDhw61O++8044cOdLt1sBbyAHA
cbwzEQAcR6gBwHGEGgAcR6gBwHGEGgAcR6gBwHGEGgAc938z9SFgWbMYhAAA
AABJRU5ErkJggg==
" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">23</span><span style=" color:#000080;">]:</span> </p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">23</span><span style=" color:#000080;">]:</span> plt.hist(numbers_of_selections,ec='black')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.title('Histogram of Ads')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('AD NO.')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.ylabel('No. of selections')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.show()</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
iVBORw0KGgoAAAANSUhEUgAAAXgAAAEWCAYAAABsY4yMAAAACXBIWXMAAAsS
AAALEgHS3X78AAAAOnpUWHRTb2Z0d2FyZQAACJnLTSwpyMkvyclMUihLLSrO
zM8z1jPUM9BRyCgpKbDS18+Fy+vlF6XrAwCbzxDQcvcyHQAAIABJREFUeJzt
3XtUlHX+B/D3CGrJRRJBIZSbGIgX1FFyM1MKc1MzYFRczdS1Mdt1dY3qnKzU
1qKy1sy0DmV4Syg9Wt43k8pUTCfQTU10ua2Iq8hFYRAZmM/vD3/Nkesg8ADz
+H6dMyefZ575fj9fHN4+fZ+bRkQERESkOu1auwAiIlIGA56ISKUY8EREKsWA
JyJSKQY8EZFKMeCJiFSKAU+tKjg4GD/88ENrl9Gqtm/fjh49esDR0RGpqalN
bm/JkiWYNm1aM1RGto4BT4rx8fHBd999V2XdunXrMHz4cMvy6dOnMXLkyHrb
ycrKgkajQUVFhRJltrqYmBh89NFHKCkpwcCBA2vdRkTg5+eHPn36tHB1ZMsY
8HTXa+1/OLKzsxEcHFzvNgcPHsSVK1eQkZGB48ePt1BlZOsY8NSqbt/LP3bs
GLRaLZydndGtWzcsXLgQADBixAgAgIuLCxwdHZGcnAyz2Yxly5bB29sb7u7u
mD59Oq5du2Zpd8OGDfD29oarqyv+8Y9/VOlnyZIl0Ol0mDZtGpydnbFu3Toc
O3YMw4YNg4uLCzw8PPDXv/4V5eXllvY0Gg3WrFmDgIAAODk54bXXXkN6ejqG
DRsGZ2dnTJo0qcr2t6ur1ps3b8LR0RGVlZUYMGAA/P396/w5rV+/HhMmTMAT
TzyB9evXV3kvMzMTjzzyCJycnBAeHo6rV69a3isrK8O0adPg6uoKFxcXDBky
BJcvX76TvyKyZUKkEG9vb9m/f3+VdfHx8fLQQw/Vus2DDz4oGzZsEBGR4uJi
SU5OFhGRzMxMASAmk8nyubVr14q/v7+kp6dLcXGxREREyLRp00RE5PTp0+Lg
4CA//fST3Lx5U1544QWxt7e39LN48WKxt7eX7du3S2VlpZSWlorBYJDk5GQx
mUySmZkpgYGBsmLFCkt/AGT8+PFy7do1OXXqlHTo0EHCwsIkPT1dioqKJCgo
SNatW1frz6G+Wn9v+/z583X+HI1Gozg5Ocnu3btl69at4urqKjdv3rS8/+CD
D8rf//53KSsrkx9//FEcHR1l6tSpIiLyySefyLhx48RoNEpFRYUYDAa5du1a
nX2RujDgSTHe3t7i4OAgnTt3trzuvffeOgP+4Ycfltdff13y8vKqtFNbwIeF
hcnq1asty2fPnhV7e3sxmUyydOlSiY6OtrxnNBqlffv2VQL+4Ycfrrf2FStW
yFNPPWVZBiCHDh2yLA8aNEjefvtty/LChQtl/vz5tbZVX62/t11fwG/cuFG6
du0qJpNJysrKpHPnzrJt2zYREcnOzhY7OzspKSmxbD9lyhRLwK9du1aGDRsm
J0+erHe8pE6coiFFff311ygqKrK81qxZU+e2a9euxblz5xAYGIghQ4Zg165d
dW6bm5sLb29vy7K3tzcqKipw+fJl5ObmokePHpb3OnXqBFdX1yqfv/19ADh3
7hzGjRuH7t27w9nZGa+88kqVqQ4A6Natm+XP9957b43lkpKSO661IdavX49J
kybB3t4eHTt2RGRkpGWaJjc3F/fddx8cHByqtP+7p59+Go8//jiio6Ph6emJ
l156CSaTqUH9ku1jwFObERAQgISEBFy5cgUvv/wydDodjEYjNBpNjW09PT2R
nZ1tWf7vf/8Le3t7dOvWDR4eHsjJybG8d+PGDeTn51f5fPU2586di8DAQJw/
fx7Xr1/HW2+9BWmmG63WV6s1OTk5SEpKwqZNm9C9e3d0794dW7duxZ49e3D1
6lV4eHigsLAQRqOxSvu/a9++PRYvXowzZ87gyJEj2LVrFzZs2NAs46K2jwFP
bcamTZuQl5eHdu3awcXFBQBgZ2cHNzc3tGvXDhkZGZZtp0yZghUrViAzMxMl
JSV45ZVXMHnyZNjb20On02Hnzp04cuQIysvLsXjxYqthXVxcDGdnZzg6OuLs
2bP4+OOPm21c9dVqzcaNG9G7d2+kpaXhxIkTOHHiBM6dOwcvLy8kJCTA29sb
Wq0WixcvRnl5OQ4dOoSdO3daPv/999/j119/RWVlJZydndG+fXvY2dk129io
bWPAU5uxb98+BAcHw9HREfPnz0diYiLuuecedOrUCYsWLcJDDz0EFxcXHD16
FLNmzcLTTz+NESNGwNfXF/fccw9WrVoF4NbFU6tWrUJ0dDQ8PDzg5OQEd3d3
dOzYsc6+33vvPWzevBlOTk549tlnMXny5GYbV321WrN+/Xo8//zzlr3331/P
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
NWq6vV57e3t07twZ+fn5rT6OBQsW4N1330W7drd+PfPz821uDBqNBqNHj8bg
wYMttyKxpe9TRkYG3NzcMHPmTAwcOBCzZ8+G0Wi0qTEANjAHLw285YEtqGss
bWWMJSUliIqKwgcffABnZ+c6t2vL47Czs8OJEyeQk5ODY8eO4bfffquzprY4
jl27dsHd3b3KOdX11dMWxwAAhw8fRkpKCvbu3YvVq1fj4MGDdW7bFsdQUVGB
lJQUzJ07F6mpqXBwcKj3+F9bHANgAwFvi7c86NatGy5dugQAuHTpEtzd3QHU
PZa2MEaTyYSoqChMnToVkZGRAGxzHL9zcXHByJEjcfToURQVFaGioqJGTbfX
W1FRgWvXrqFLly6tOo7Dhw9jx44d8PHxQXR0NJKSkrBgwQKbGgMAS1/u7u6I
iIjAsWPHbOr75OXlBS8vL4SGhgIAdDodUlJSbGoMANr+QVaTySS+vr6SkZFh
Och66tSp1i6riupz8DExMVUOxLz44osiIrJr164qB2KGDBkiIrcOxPj4+EhB
QYEUFBSIj4+P5Ofnt1j9ZrNZnn76aZk/f36V9bY2jitXrkhhYaGIiJSWlsrw
4cNl586dotPpqhygXL16tYiIfPTRR1UOUE6cOFFERE6dOlXlAKWvr2+LH2QV
Efn+++8tB1ltaQwlJSVy/fp1y5+HDRsme/futbnv0/Dhw+Xs2bMiIrJ48WKJ
iYmxuTG0+YAXuXWEOiAgQPz8/GTZsmWtXU4V0dHR0r17d7G3t5f7779fPvvs
M7l69aqEhYVJr169JCwszPIXajab5fnnnxc/Pz/p27evHD9+3NLO2rVrxd/f
X/z9/eXzzz9v0TH89NNPAkD69esnAwYMkAEDBsju3bttbhwnT56UkJAQ6dev
nwQHB8vSpUtFRCQ9PV2GDBki/v7+otPppKysTEREbty4ITqdTvz9/WXIkCGS
np5uaWvZsmXi5+cnvXv3lj179rToOH53e8Db0hjS09Olf//+0r9/f+nTp4/l
d9bWvk+pqakyePBg6devn0yYMEEKCgpsbgy8VQERkUq1+Tl4IiJqHAY8EZFK
MeCJiFSKAU9EpFIMeCIilWLA011h+/bt0Gg0OHv2rGVdVlYW7r33XgwcOBBB
QUEYOnRonXf7++GHH6DRaLBz507LunHjxuGHH34AAJSXl2PBggXw9/dHQEAA
JkyYgJycHEXHRGQNA57uCgkJCRg+fDgSExOrrPf390dqaip+++03JCYmYsWK
FYiPj6+1DS8vL7z55pu1vvfKK6+guLgY586dw/nz5/HUU08hMjKy1kvViVoK
A55Ur6SkBIcPH8batWtrBPzt/Pz88M9//hMffvhhre8PGDAAnTt3xv79+6us
Ly0tRXx8PFasWAE7OzsAwMyZM9GxY0ckJSU130CI7hADnlTv66+/xpgxY9C7
d2906dKlysMYqhs0aFCVaZzqXn31VSxbtqzKuv/85z/o2bNnjRu0abVanD4F
9RdOAAABYElEQVR9umnFEzUBA55ULyEhAdHR0QCA6OhoJCQk1LmttSmVhx9+
GADw008/VflMbXcIrGs9UUuxb+0CiJSUn5+PpKQknDp1ChqNBpWVldBoNHj3
3Xdr3T41NRVBQUH1trlo0SK8+eablvuz9+rVC9nZ2SguLoaTk5Nlu5SUFIwf
P775BkN0h7gHT6q2detWTJ8+HdnZ2cjKysKFCxfg6+uLQ4cO1dg2KysLMTEx
mDdvXr1tjh49GoWFhTh58iQAwMHBAc888wwWLlyIyspKAMCGDRtQWlqKsLCw
5h8UUQMx4EnVEhISEBERUWVdVFQUNm/eDABIT0+3nCY5adIkzJs3DzNnzrTa
7qJFi6qcBhkbG4t77rkHvXv3RkBAALZs2WI5NRMAnnjiCeTm5jbjyIis490k
iYhUinvwREQqxYAnIlIpBjwRkUox4ImIVIoBT0SkUgx4IiKVYsATEanU/wEC
DbgWDw9a5QAAAABJRU5ErkJggg==
" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">24</span><span style=" color:#000080;">]:</span> plt.hist(numbers_of_selections,ec='black')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.title('Histogram of Ads')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.ylabel('AD NO.')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('No. of selections')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.show()</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
iVBORw0KGgoAAAANSUhEUgAAAXgAAAEWCAYAAABsY4yMAAAACXBIWXMAAAsS
AAALEgHS3X78AAAAOnpUWHRTb2Z0d2FyZQAACJnLTSwpyMkvyclMUihLLSrO
zM8z1jPUM9BRyCgpKbDS18+Fy+vlF6XrAwCbzxDQcvcyHQAAIABJREFUeJzt
3XtUVXX6P/D3Ebwk1xFBQIy7gcj9IDqaFxrsRjUoKiZaaZ6yaY2OaU61vpHT
RUdtMG8zw0QKOoKNZSleMtHRVIxOimvUUONioqVHFAUUOMDz+8OfZ3E7mMrm
sn2/1mItz96f83mejx3envY+Z2+NiAiIiEh1urR3A0REpAwGPBGRSjHgiYhU
igFPRKRSDHgiIpViwBMRqRQDntpVQEAA/vvf/7Z3G+1q06ZN6NevH6ytrXHk
yJF7nu+dd95BQkJCK3RGnR0DnhTj4eGBXbt2Ndi2Zs0aDBs2zPT4+PHjGDly
ZIvzFBUVQaPRoKamRok2292cOXOwYsUKlJeXIzQ0tNkxIgIvLy8MGDCgjbuj
zowBT/e99v6H48yZMwgICGhxzL59+3Dx4kUUFBTgu+++a6POqLNjwFO7qv8u
PycnB1qtFra2tujTpw9mz54NABg+fDgAwN7eHtbW1sjOzkZdXR3ee+89uLu7
w8nJCVOmTMHVq1dN86alpcHd3R0ODg549913G9R55513EBcXh4SEBNja2mLN
mjXIycnBkCFDYG9vDxcXF7z66quorq42zafRaLBq1Sr4+vrCxsYG//d//4f8
/HwMGTIEtra2GD9+fIPx9ZnrtaqqCtbW1qitrUVwcDC8vb3N/j2lpqbimWee
wRNPPIHU1NQG+woLCzFixAjY2NggOjoaly5dMu2rrKxEQkICHBwcYG9vj4iI
CFy4cOFO/hNRZyZECnF3d5evv/66wbbVq1fL0KFDmx0zePBgSUtLExGRsrIy
yc7OFhGRwsJCASBGo9H0vJSUFPH29pb8/HwpKyuT2NhYSUhIEBGR48ePi5WV
lXzzzTdSVVUlr732mlhaWprqJCYmiqWlpWzatElqa2vl+vXrotfrJTs7W4xG
oxQWFoqfn58kJSWZ6gGQp556Sq5evSrHjh2Tbt26SVRUlOTn50tpaan4+/vL
mjVrmv17aKnXW3OfPn3a7N9jRUWF2NjYyNatW2Xjxo3i4OAgVVVVpv2DBw+W
P/3pT1JZWSl79+4Va2trmTRpkoiI/OMf/5CYmBipqKiQmpoa0ev1cvXqVbO1
SF0Y8KQYd3d3sbKyEjs7O9PPAw88YDbgH374YXn77bfFYDA0mKe5gI+KipKV
K1eaHufl5YmlpaUYjUaZP3++xMfHm/ZVVFRI165dGwT8ww8/3GLvSUlJ8vvf
/970GIDs37/f9DgsLEwWLlxoejx79myZOXNms3O11OutuVsK+LVr10rv3r3F
aDRKZWWl2NnZyeeffy4iImfOnBELCwspLy83jZ84caIp4FNSUmTIkCFy9OjR
FtdL6sRDNKSoL774AqWlpaafVatWmR2bkpKCU6dOwc/PDxEREcjMzDQ79vz5
83B3dzc9dnd3R01NDS5cuIDz58+jX79+pn09e/aEg4NDg+fX3w8Ap06dQkxM
DJydnWFra4s333yzwaEOAOjTp4/pzw888ECTx+Xl5Xfc66+RmpqK8ePHw9LS
Et27d8eYMWNMh2nOnz+P3/zmN7Cysmow/y2TJ0/Go48+ivj4eLi6uuL111+H
0Wj8VXWp82PAU4fh6+uL9PR0XLx4EfPmzUNcXBwqKiqg0WiajHV1dcWZM2dM
j3/66SdYWlqiT58+cHFxQXFxsWnfjRs3UFJS0uD5jeecMWMG/Pz8cPr0aVy7
dg0ffPABpJUutNpSr7dTXFyM3bt3Y926dXB2doazszM2btyIbdu24dKlS3Bx
ccGVK1dQUVHRYP5bunbtisTERJw4cQIHDx5EZmYm0tLSWmVd1PEx4KnDWLdu
HQwGA7p06QJ7e3sAgIWFBRwdHdGlSxcUFBSYxk6cOBFJSUkoLCxEeXk53nzz
TUyYMAGWlpaIi4vDli1bcPDgQVRXVyMxMfG2YV1WVgZbW1tYW1sjLy8Pf//7
31ttXS31ejtr165F//79cfLkSeTm5iI3NxenTp2Cm5sb0tPT4e7uDq1Wi8TE
RFRXV2P//v3YsmWL6fl79uzB//73P9TW1sLW1hZdu3aFhYVFq62NOjYGPHUY
O3bsQEBAAKytrTFz5kxkZGSgR48e6NmzJ9566y0MHToU9vb2OHToEKZOnYrJ
kydj+PDh8PT0RI8ePbB8+XIAN788tXz5csTHx8PFxQU2NjZwcnJC9+7dzdZe
smQJ1q9fDxsbG0yfPh0TJkxotXW11OvtpKam4pVXXjG9e7/18/LLL5sO06xf
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
Bwepq6tr8hqrP64tnD17VqKioiQrK0uefPJJqaur63RraC7gO9Pr6erVq+Lh
4SF1dXUNtnemNYiIdPhDNOfOnUO/fv1Mj93c3HDu3Ll27Oj2Lly4ABcXFwCA
i4sLLl68CMD8WjrSGouKinDkyBFERkZ2ynXU1tYiJCQETk5OiI6Ohre3N+zt
7WFpadmkp/r9Wlpaws7ODiUlJe2+jlmzZmHRokXo0uXmr2dJSUmnW4NGo8Ho
0aMRHh5uuhRJZ3o9FRQUwNHRES+88AJCQ0Px4osvoqKiolOtAegEx+DlV17y
oDMwt5aOssby8nKMHTsWS5cuha2trdlxHXkdFhYWyM3NRXFxMXJycvDDDz+Y
7akjriMzMxNOTk4NPlPdUj8dcQ0AcODAARw+fBjbt2/HypUrsW/fPrNjO+Ia
ampqcPjwYcyYMQNHjhyBlZVVi+f/OuIagE4Q8J3xkgd9+vTBzz//DAD4+eef
4eTkBMD8WjrCGo1GI8aOHYtJkyZhzJgxADrnOm6xt7fHyJEjcejQIZSWlqKm
pqZJT/X7rampwdWrV9GrV692XceBAwewefNmeHh4ID4+Hrt378asWbM61RoA
mGo5OTkhNjYWOTk5ner15ObmBjc3N0RGRgIA4uLicPjw4U61BgAd/ySr0WgU
T09PKSgoMJ1kPXbsWHu31UDjY/Bz5sxpcCJm7ty5IiKSmZnZ4ERMRESEiNw8
EePh4SGXL1+Wy5cvi4eHh5SUlLRZ/3V1dTJ58mSZOXNmg+2dbR0XL16UK1eu
iIjI9evXZdiwYbJlyxaJi4trcIJy5cqVIiKyYsWKBicox40bJyIix44da3CC
0tPTs81PsoqI7Nmzx3SStTOtoby8XK5du2b685AhQ2T79u2d7vU0bNgwycvL
ExGRxMREmTNnTqdbQ4cPeJGbZ6h9fX3Fy8tL3nvvvfZup4H4+HhxdnYWS0tL
6du3r3z88cdy6dIliYqKEh8fH4mKijL9B62rq5NXXnlFvLy8ZODAgfLdd9+Z
5klJSRFvb2/x9vaWTz75pE3X8M033wgACQwMlODgYAkODpatW7d2unUcPXpU
QkJCJDAwUAICAmT+/PkiIpKfny8RERHi7e0tcXFxUllZKSIiN27ckLi4OPH2
9paIiAjJz883zfXee++Jl5eX9O/fX7Zt29am67ilfsB3pjXk5+dLUFCQBAUF
yYABA0y/s53t9XTkyBEJDw+XwMBAeeaZZ+Ty5cudbg28VAERkUp1+GPwRER0
dxjwREQqxYAnIlIpBjwRkUox4ImIVIoBTx2CRqPBa6+9Znq8ZMkSKHGzsblz
5yIgIABz5869p3msra3v6nlffPEFTpw4YXr89ttvY9euXffUC5E5lu3dABEA
dO/eHZ9//jneeOMN9O7dW7E6//znP2EwGNC9e3fFarTkiy++QExMDAYMGAAA
+Mtf/tIufdD9ge/gqUOwtLSETqdDUlJSk31nzpzBI488gqCgIDzyyCP46aef
WpxLRDB37lwMHDgQgYGB2LBhAwDg6aefRkVFBSIjI03bbtm7dy9CQkIQEhKC
0NBQlJWVAQAWL16MiIgIBAUFma4v35i5MWlpaQgKCkJwcDAmT56MgwcPYvPm
zZg7dy5CQkKQn5+P559/Hhs3bgQAZGVlITQ0FIGBgZg6dSqqqqoA3Ly2emJi
IsLCwhAYGIi8vLwWeyYyadOvVRGZYWVlJVevXhV3d3cpLS2VxYsXS2JiooiI
xMTEyJo1a0Tk5rcCn3nmmRbn2rhxo/zud7+Tmpoa+eWXX6Rfv36mS7xaWVk1
+5yYmBjZv3+/iIiUlZWJ0WiUr776SqZPny51dXVSW1srTz75pOzdu7fBPObG
HDt2TPr372+6ZO6tbzw+99xz8p///MdU99bjGzduiJubm5w8eVJERCZPnixJ
SUkicvPSu8uWLRORm9d/nzZtmtmeierjO3jqMGxtbTFlyhQsW7aswfbs7Gw8
++yzAIDJkydj//79Lc6zf/9+TJw4ERYWFujTpw9GjBiB7777rsXnDB06FLNn
z8ayZctQWloKS0tL7Ny5Ezt37kRoaCjCwsKQl5eH06dPN3ieuTG7d+9GXFyc
6XBTr169Wqx/8uRJeHp6on///gCA5557rsEVGG9dAC48PNx016bmeiaqjwFP
HcqsWbOQkpKCiooKs2Nud7lVuYurb/z5z3/Gxx9/jBs3bmDw4MHIy8uDiOCN
N95Abm4ucnNz8eOPP2LatGlNajU3RkTu6LKwt+v51jkDCwsL01Ulm+uZqD4G
PHUovXr1wvjx45GSkmLa9tvf/hYZGRkAgH//+98YNmxYi3MMHz4cGzZsQG1t
LQwGA/bt24dBgwa1+Jz8/HwEBgZi3rx50Gq1yMvLw6OPPopPPvkE5eXlAG7e
1OHWDR5uMTfmkUcewaeffoqSkhIAN+9HCgA2NjbNHiv38/NDUVERfvzxRwDA
2rVrMWLEiDvumag+/j8ddTivvfYaVqxYYXq8bNkyTJ06FYsXL4ajoyNWr14N
ANi8eTP0en2TT6LExsYiOzsbwcHB0Gg0WLRoEZydnVusuXTpUuzZswcWFhYY
MGAAHn/8cXTv3h0//PADhgwZAuDmRyPXrVtnugY4AIwePbrZMQEBAXjrrbcw
YsQIWFhYIDQ0FGvWrEF8fDymT5+OZcuWmU6uAkCPHj2wevVqjBs3DjU1NYg0
p/I8AAAAPklEQVSIiMDLL798xz0T1cerSRIRqRQP0RARqRQDnohIpRjwREQq
xYAnIlIpBjwRkUox4ImIVIoBT0SkUv8PMH9wk6gAWRoAAAAASUVORK5CYII=

" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">25</span><span style=" color:#000080;">]:</span> plt.hist(ads_selected,ec='black')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.title('Histogram of Ads')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('Ads')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('No. of selections')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.show()</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
iVBORw0KGgoAAAANSUhEUgAAAX0AAAEWCAYAAACKSkfIAAAACXBIWXMAAAsS
AAALEgHS3X78AAAAOnpUWHRTb2Z0d2FyZQAACJnLTSwpyMkvyclMUihLLSrO
zM8z1jPUM9BRyCgpKbDS18+Fy+vlF6XrAwCbzxDQcvcyHQAAIABJREFUeJzt
3X9U1XWex/HnjVs2/uDHLdDLgGhdSiRN7BK2zeQke6N1WdyKRRx/MKPFGds9
lVZr80ON3T1FNXMsy9ldzrB6tZmYlTMDZYps2uRqInOP2tky7GZggKSkYEr+
APrsH57uhPLLAi7xfT3O4Rzv536+3+/781Vf3+/9fu/3g80YYxAREUu4ItgF
iIjIwFHoi4hYiEJfRMRCFPoiIhai0BcRsRCFvoiIhSj0ZdBJTEzkT3/6U7DL
CKo//vGPxMbGMnLkSPbt2/eN1/fkk08yb968PqhMvu0U+jKgxo0bxxtvvNGh
bd26dXzve98LvH7vvff4wQ9+0O16ampqsNlstLW19UeZQffYY4/x0ksvcfr0
aZKSkjrtY4zhuuuuY+LEiQNcnXybKfRFOhHsg8nhw4dJTEzsts+OHTs4duwY
H330EX/+858HqDL5tlPoy6Dz1U8DlZWVuN1uQkNDGT16NEuXLgXgjjvuACA8
PJyRI0eye/duvvjiC/7t3/6NuLg4oqKiWLBgASdPngysd/369cTFxXHNNdfw
r//6rx228+STT5KZmcm8efMIDQ1l3bp1VFZWcttttxEeHo7T6eSf/umfOH/+
fGB9NpuNX//618THxzNq1CiWL1/OoUOHuO222wgNDSUrK6tD/6/qqtZz584x
cuRI2tvbufnmm7n++uu73E9er5dZs2Yxc+ZMvF5vh/eqq6uZPn06o0aNwuPx
8OmnnwbeO3v2LPPmzeOaa64hPDyc5ORkjh49ejl/RfJtZkQGUFxcnPmf//mf
Dm1r1641t99+e6d9pk2bZtavX2+MMebUqVNm9+7dxhhjqqurDWBaW1sDyxUW
Fprrr7/eHDp0yJw6dcrcc889Zt68ecYYY9577z0zYsQI87//+7/m3Llz5tFH
HzV2uz2wnZUrVxq73W7++Mc/mvb2dvP5558bn89ndu/ebVpbW011dbWZMGGC
WbVqVWB7gPm7v/s7c/LkSfPuu++aq666ysyYMcMcOnTINDc3m4SEBLNu3bpO
90N3tX65br/f3+V+bGlpMaNGjTKvv/66KS4uNtdcc405d+5c4P1p06aZJUuW
mLNnz5q33nrLjBw50sydO9cYY8x//Md/mPT0dNPS0mLa2tqMz+czJ0+e7HJb
MrQo9GVAxcXFmREjRpiwsLDAz3e+850uQ//73/++WbFihWlsbOywns5Cf8aM
GWbNmjWB11VVVcZut5vW1laTl5dnsrOzA++1tLSYK6+8skPof//73++29lWr
Vpm///u/D7wGzM6dOwOvp06davLz8wOvly5dah5++OFO19VdrV+uu7vQ37Bh
g7n22mtNa2urOXv2rAkLCzN/+MMfjDHGHD582ISEhJjTp08H+s+ZMycQ+oWF
hea2224z77zzTrfjlaFJl3dkwJWUlNDc3Bz4+fWvf91l38LCQj744AMmTJhA
cnIymzZt6rLvkSNHiIuLC7yOi4ujra2No0ePcuTIEWJjYwPvDR8+nGuuuabD
8l99H+CDDz4gPT2dMWPGEBoays9+9rMOl0kARo8eHfjzd77znUtenz59+rJr
7Q2v10tWVhZ2u51hw4Zx7733Bi7xHDlyhIiICEaMGNFh/V+aP38+aWlpZGdn
Ex0dzT//8z/T2traq+3Kt59CXwa1+Ph4XnnlFY4dO8ayZcvIzMykpaUFm812
Sd/o6GgOHz4ceP3xxx9jt9sZPXo0TqeTurq6wHtnzpzh+PHjHZa/eJ2LFy9m
woQJ+P1+PvvsM5566ilMH01K212tPamrq2P79u28/PLLjBkzhjFjxlBcXMzm
zZv59NNPcTqdNDU10dLS0mH9X7ryyitZuXIlBw4c4O2332bTpk2sX7++T8Yl
g59CXwa1l19+mcbGRq644grCw8MBCAkJITIykiuuuIKPPvoo0HfOnDmsWrWK
6upqTp8+zc9+9jNmz56N3W4nMzOT1157jbfffpvz58+zcuXKHgP81KlThIaG
MnLkSKqqqvj3f//3PhtXd7X2ZMOGDdxwww0cPHiQ/fv3s3//fj744ANiYmJ4
5ZVXiIuLw+12s3LlSs6fP8/OnTt57bXXAsu/+eab/N///R/t7e2EhoZy5ZVX
EhIS0mdjk8FNoS+DWllZGYmJiYwcOZKHH36YoqIirr76aoYPH87Pf/5zbr/9
dsLDw6moqGDhwoXMnz+fO+64g/Hjx3P11Vfz4osvAhce+HrxxRfJzs7G6XQy
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
/u3fmrfeeqvDerrq8+6775obbrjBNDY2GmOMOX78uDHGmJycHLNx48bAdr98
febMGRMTE2MOHjxojDFm/vz5ZtWqVcYYY+Li4szq1auNMcasWbPGLFq0qMua
RS6mM30ZtEJDQ1mwYAGrV6/u0L57925++MMfAjB//nx27tzZ7Xp27tzJnDlz
CAkJYfTo0UyfPp0///nP3S5z++23s3TpUlavXk1zczN2u53y8nLKy8tJSkpi
6tSpVFVV4ff7OyzXVZ/t27eTmZkZuFTlcDi63f7BgwcZP348N9xwAwA5OTlf
d85FAAAB60lEQVTs2LEj8P6XE+fdcsst1NTUdFmzyMUU+jKoPfLIIxQWFnY7
z3tPU2ebrzHTyBNPPMFvfvMbzpw5w7Rp06iqqsIYw09/+lP279/P/v37+fDD
DwO/gOSr2+qsjzHmsqb47qnmL+9BhISE0NbW1mXNIhdT6Mug5nA4yMrKorCw
MND2V3/1V4FfY/fb3/6W733ve92u44477uD3v/897e3tNDY2smPHDm699dZu
lzl06BCTJk1i2bJluN1uqqqqSEtL47/+6784ffo0cOEX9hw7dqzDcl31SU1N
5b//+785fvw4ACdOnAAu/Dazzq69T5gwgZqaGj788EMANmzYwPTp0y+7ZpGL
6fOfDHqPPvooL730UuD16tWrWbhwIc899xyRkZGBmSFfffVVfD7fJd+Aueee
e9i9ezc333wzNpuNZ599ljFjxnS7zeeff54333yTkJAQJk6cyN/8zd8wbNgw
3n//fW677Tbgwtc0X375ZaKiogLL3XXXXZ32SUxM5Oc//znTp08nJCSEpKQk
1q1bR3Z2Ng888ACrV68O3MAFuPrqq1m7di3/8A//QFtbG8nJyfzkJz+57JpF
LqZZNkVELESXd0RELEShLyJiIQp9ERELUeiLiFiIQl9ExEIU+iIiFqLQFxGx
kP8HXO9VmhYLxkIAAAAASUVORK5CYII=
" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">26</span><span style=" color:#000080;">]:</span> runfile('C:/Users/Apoorav Gupta/Desktop/Machine Learning/untitled1.py', wdir='C:/Users/Apoorav Gupta/Desktop/Machine Learning')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Traceback <span style=" color:#4682b4;">(most recent call last)</span>:</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;&lt;ipython-input-26-ebea11894835&gt;&quot;</span>, line <span style=" color:#00ff00;">1</span>, in <span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    runfile('C:/Users/Apoorav Gupta/Desktop/Machine Learning/untitled1.py', wdir='C:/Users/Apoorav Gupta/Desktop/Machine Learning')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\spyder_kernels\customize\spydercustomize.py&quot;</span>, line <span style=" color:#00ff00;">827</span>, in <span style=" color:#ff00ff;">runfile</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    execfile(filename, namespace)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\spyder_kernels\customize\spydercustomize.py&quot;</span>, line <span style=" color:#00ff00;">110</span>, in <span style=" color:#ff00ff;">execfile</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    exec(compile(f.read(), filename, 'exec'), namespace)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;C:/Users/Apoorav Gupta/Desktop/Machine Learning/untitled1.py&quot;</span>, line <span style=" color:#00ff00;">10</span>, in <span style=" color:#ff00ff;">&lt;module&gt;</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    dataset=pd.read_csv('Ads_CTR_Optimisation.csv')</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">702</span>, in <span style=" color:#ff00ff;">parser_f</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    return _read(filepath_or_buffer, kwds)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">429</span>, in <span style=" color:#ff00ff;">_read</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    parser = TextFileReader(filepath_or_buffer, **kwds)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">895</span>, in <span style=" color:#ff00ff;">__init__</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    self._make_engine(self.engine)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">1122</span>, in <span style=" color:#ff00ff;">_make_engine</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    self._engine = CParserWrapper(self.f, **self.options)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;F:\Coding\lib\site-packages\pandas\io\parsers.py&quot;</span>, line <span style=" color:#00ff00;">1853</span>, in <span style=" color:#ff00ff;">__init__</span></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">    self._reader = parsers.TextReader(src, **kwds)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">  File <span style=" color:#00ff00;">&quot;pandas/_libs/parsers.pyx&quot;</span>, line <span style=" color:#00ff00;">387</span>, in <span style=" color:#ff00ff;">pandas._libs.parsers.TextReader.__cinit__</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#4682b4;">  File </span><span style=" color:#006400;">&quot;pandas/_libs/parsers.pyx&quot;</span><span style=" color:#4682b4;">, line </span><span style=" color:#006400;">705</span><span style=" color:#4682b4;">, in </span><span style=" color:#9400d3;">pandas._libs.parsers.TextReader._setup_parser_source</span></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#8b0000;">FileNotFoundError:</span> [Errno 2] File b'Ads_CTR_Optimisation.csv' does not exist: b'Ads_CTR_Optimisation.csv'</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">27</span><span style=" color:#000080;">]:</span> </p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">27</span><span style=" color:#000080;">]:</span> import pandas as pd</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import matplotlib.pyplot as plt</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import numpy as np</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import random</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> #importing dataset</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> dataset=pd.read_csv('Ads_CTR_Optimisation.csv')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> #Implementing UCB</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> N=10000</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> d=10</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> ads_selected=[]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> numbers_of_rewards_1=[0]*d</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> numbers_of_rewards_0=[0]*d</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> total_reward=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> for n in range(0,N):</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     ad=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     max_random=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     for i in range(0,d):</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         random_beta=random.betavariate(numbers_of_rewards_1[i]+1 , numbers_of_rewards_0[i]+1)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         if random_beta&gt;max_random:</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             max_random=random_beta</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             ad=i</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     ads_selected.append(ad)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     reward=dataset.values[n,ad]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     if reward==1:</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         numbers_of_rewards_1[ad]=numbers_of_rewards_1[ad]+1</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     else:</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         numbers_of_rewards_0[ad]=numbers_of_rewards_0[ad]+1</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     total_reward=total_reward+reward</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">28</span><span style=" color:#000080;">]:</span> import pandas as pd</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import matplotlib.pyplot as plt</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import numpy as np</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> import random</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> #importing dataset</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> dataset=pd.read_csv('Ads_CTR_Optimisation.csv')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> #Implementing UCB</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> N=10000</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> d=10</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> ads_selected=[]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> numbers_of_rewards_1=[0]*d</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> numbers_of_rewards_0=[0]*d</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> total_reward=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> for n in range(0,N):</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     ad=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     max_random=0</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     for i in range(0,d):</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         random_beta=random.betavariate(numbers_of_rewards_1[i]+1 , numbers_of_rewards_0[i]+1)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         </p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         if random_beta&gt;max_random:</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             max_random=random_beta</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>             ad=i</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     ads_selected.append(ad)</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     reward=dataset.values[n,ad]</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     if reward==1:</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         numbers_of_rewards_1[ad]=numbers_of_rewards_1[ad]+1</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     else:</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>         numbers_of_rewards_0[ad]=numbers_of_rewards_0[ad]+1</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span>     total_reward=total_reward+reward</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">29</span><span style=" color:#000080;">]:</span> plt.hist(ads_selected,ec='black')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.title('Histogram of Ads')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('Ads')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.xlabel('No. of selections')</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">    ...:</span> plt.show()</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="data:image/png;base64,
iVBORw0KGgoAAAANSUhEUgAAAX0AAAEWCAYAAACKSkfIAAAACXBIWXMAAAsS
AAALEgHS3X78AAAAOnpUWHRTb2Z0d2FyZQAACJnLTSwpyMkvyclMUihLLSrO
zM8z1jPUM9BRyCgpKbDS18+Fy+vlF6XrAwCbzxDQcvcyHQAAHfxJREFUeJzt
3XlU1XXi//HnjauWCyCGCoGoQYmkiWLot8VRh2yMwUkZxXFhEvNkMyeXdGjV
nJmTth1za2Y4MYpa0cQpMXMbtclx7x61M2oYKpigKSmo4MLS+/eHP++Esdgk
XOL9epzDOd3P/Szvzyd53g+fy/3gMMYYRETECjd5egAiIlJ/FH0REYso+iIi
FlH0RUQsouiLiFhE0RcRsYiiLw1OREQE//rXvzw9DI/68MMPCQ4OpmXLluzZ
s+dHr+/FF19k9OjRN2Bk8lOn6Eu96tixIxs2bKg0bcmSJdx3333ux/v37+dn
P/tZjevJzc3F4XBQXl5eF8P0uGnTprFw4UKKi4uJjIysch5jDJ07d6Zr1671
PDr5KVP0Rarg6ReTo0ePEhERUeM8mzdv5tSpUxw5coTPPvusnkYmP3WKvjQ4
3/1pYNeuXURFReHt7U27du2YOnUqAA888AAAvr6+tGzZku3bt/Ptt9/y5z//
mZCQENq2bcvYsWM5e/ase71Lly4lJCSENm3a8Kc//anSdl588UXi4+MZPXo0
3t7eLFmyhF27dtG3b198fX0JCAjg97//PaWlpe71ORwO3nzzTcLCwmjVqhUv
vPAChw8fpm/fvnh7ezN8+PBK839XdWO9fPkyLVu2pKKigrvvvpvbb7+92uOU
lpbGkCFDGDx4MGlpaZWey8nJoV+/frRq1YqYmBi++eYb93OXLl1i9OjRtGnT
Bl9fX3r37s3Jkyd/yP8i+SkzIvUoJCTE/POf/6w0bfHixebee++tcp4+ffqY
pUuXGmOMOX/+vNm+fbsxxpicnBwDmLKyMvdyqamp5vbbbzeHDx8258+fN488
8ogZPXq0McaY/fv3mxYtWph///vf5vLly+app54yTqfTvZ2ZM2cap9NpPvzw
Q1NRUWEuXLhgXC6X2b59uykrKzM5OTmmS5cuZu7cue7tAeaXv/ylOXv2rNm3
b59p2rSpGTBggDl8+LApKioy4eHhZsmSJVUeh5rGenXd2dnZ1R7HkpIS06pV
K/Pxxx+bjIwM06ZNG3P58mX383369DFTpkwxly5dMp9++qlp2bKlGTVqlDHG
mL/+9a8mNjbWlJSUmPLycuNyuczZs2er3ZY0Loq+1KuQkBDTokUL4+Pj4/66
5ZZbqo3+/fffb2bMmGEKCgoqraeq6A8YMMAsWrTI/TgrK8s4nU5TVlZmZs2a
ZRISEtzPlZSUmCZNmlSK/v3331/j2OfOnWt+9atfuR8DZsuWLe7HPXv2NHPm
zHE/njp1qpk0aVKV66pprFfXXVP0ly1bZm699VZTVlZmLl26ZHx8fMwHH3xg
jDHm6NGjxsvLyxQXF7vnHzlypDv6qamppm/fvubzzz+vcX+lcdLlHal3K1as
oKioyP315ptvVjtvamoqX375JV26dKF3796sWrWq2nmPHz9OSEiI+3FISAjl
5eWcPHmS48ePExwc7H6uefPmtGnTptLy330e4MsvvyQ2Npb27dvj7e3Ns88+
W+kyCUC7du3c/33LLbd873FxcfEPHuv1SEtLY/jw4TidTpo1a8bQoUPdl3iO
Hz9O69atadGiRaX1XzVmzBgGDRpEQkICgYGB/OEPf6CsrOy6tis/fYq+NGhh
YWG8++67nDp1iuTkZOLj4ykpKcHhcHxv3sDAQI4ePep+/NVXX+F0OmnXrh0B
AQHk5eW5n7t48SKnT5+utPy165w4cSJdunQhOzubc+fO8dJLL2Fu0E1paxpr
bfLy8ti0aRPLly+nffv2tG/fnoyMDFavXs0333xDQEAAhYWFlJSUVFr/VU2a
NGHmzJkcOHCAbdu2sWrVKpYuXXpD9ksaPkVfGrTly5dTUFDATTfdhK+vLwBe
Xl74+/tz0003ceTIEfe8I0eOZO7cueTk5FBcXMyzzz7LiBEjcDqdxMfH89FH
H7Ft2zZKS0uZOXNmrQE/f/483t7etGzZkqysLP7yl7/csP2qaay1WbZsGXfc
cQcHDx5k79697N27ly+//JKgoCDeffddQkJCiIqKYubMmZSWlrJlyxY++ugj
9/KffPIJ//nPf6ioqMDb25smTZrg5eV1w/ZNGjZFXxq0tWvXEhERQcuWLZk0
aRLp6encfPPNNG/enOeee457770XX19fduzYwbhx4xgzZgwPPPAAnTp14uab
b2bBggXAlQ98LViwgISEBAICAmjVqhVt27alWbNm1W77tdde45133qFVq1Y8
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
" /></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000080;">In [</span><span style=" font-weight:600; color:#000080;">30</span><span style=" color:#000080;">]:</span> </p></body></html>