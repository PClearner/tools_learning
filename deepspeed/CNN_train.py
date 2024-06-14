import torch
import torch.nn as nn
from torchvision import datasets, transforms
import deepspeed

#继承module的类，做简单的CNN卷积，初始化为两层卷积两层全连接。前向传播的方式是卷积完通过激活函数再过一层池化层，然后再重复一边前面的操作，再来一波全连接层最后输出。
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(64*7*7, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.max_pool2d(x, 2)
        x = torch.relu(self.conv2(x))
        x = torch.max_pool2d(x, 2)
        x = x.view(-1, 64*7*7)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return torch.log_softmax(x, dim=1)

# 定义预处理步骤，转换为张量再归一化处理
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# 下载并加载MNIST训练数据，data数据集设置了download为true，当前目录没有数据集它会直接下载的
train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)

# 定义训练函数，将数据集中的数据放进去训练，先清除梯度，然后将数据放入模型训练再输出，计算损失并将损失反馈回来，更新参数。每当有超过100个数据加入训练就打印当前情况
def train(model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = nn.functional.nll_loss(output, target)
        loss.backward()
        optimizer.step()  # 这里是DeepSpeed的优化器步骤
        if batch_idx % 100 == 0:
            print(f'Train Epoch: {epoch} [{batch_idx * len(data)}/{len(train_loader.dataset)} ({100. * batch_idx / len(train_loader):.0f}%)]\tLoss: {loss.item():.6f}')

# 主函数，设置硬件方面之后就deepspeed初始化模型，再训练。我当前用的云服务器没有弄NVIDIA， 看了一下估计是核显，cuda这边就别想了，都是用cpu跑，估计会很慢，所以epoch就搞一次，看看效果就好了
def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SimpleCNN().to(device)

    # DeepSpeed 初始化
    model, optimizer, _, _ = deepspeed.initialize(model=model, model_parameters=model.parameters(), config='ds_config.json')

    for epoch in range(1, 2):  # 这里只训练一个epoch
        train(model, device, train_loader, optimizer, epoch)

if __name__ == '__main__':
    main()
