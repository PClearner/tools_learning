river直接pip下载就好了，假如是在云上的话可能会有限制不给下载，我目前是这种情况，这时候可以选择建立虚拟环境：
python3 -m venv river_env
source river_env/bin/activate
我自己取名字叫river_env，自己可以看喜好取名，第一行命令之后会在当前目录创建river_env文件夹，里面是关于虚拟环境的文件，运行里面的activate就好了（用source启动估计是脚本文件，但后缀没有.sh，看不懂），然后再pip下载river就好了。
下面是做了一个简易的demo，训练一个商品房模型，输入是面积，卧室数量，厕所数量，输出是价格,代码和输入格式都在里面，自己看就好了，不过输出的结果不是很满意。