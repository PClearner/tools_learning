deepspeed���Ҫ��װ���е�����Բ���������ﵽʱ���Լ���װ��
pip install deepspeed torch torchvision torchaudio 

ֱ������CNN_train.py�ͺ��ˣ�����ʵ��һ���򵥵�CNN����ȥѵ��MNIST��demo�����к������data��deepspeedʵ�ֲַ�ʽѵ������Ҫ��װmpi4py�Լ���Ϊ�˹�����������Ҫ��ϵͳ������
sudo apt-get update 
sudo apt-get install -y libopenmpi-dev python3-dev build-essential
pip install mpi4py

�Ǹ�ds_config.json�����ļ����ǻ�������һЩ����ѵ���������ݶ��ۼƲ�������������һ���Ż���֮��ģ���Ҫ˵��һ�º����������ã�zero��֪���ǲ�����ΪӲ������Ķ����������õ���cpu���ܵ���stageд1���Ͼͻ�����ʧ�ܣ�����zeroĿǰ�˽⵽��Ҳֻ�������Ż��ڴ�ģ������ֺ�С��ģ��ѵ����stage = 0ҲûɶӰ�졣fp16�ǰ븡�������ݣ����������֧���������ݽṹ����Ҳ�ص��ˣ�logging����ǿ�ҽ������һ�����ã���INFO�������־̫���ˣ�ĿǰҲû�п��ı�Ҫ��Ӱ��۸С�