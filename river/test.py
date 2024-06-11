from river import linear_model, preprocessing, metrics, compose
import re

# 创建一个标准化器和线性回归模型的管道
model = (
    compose.Select('area', 'bedrooms', 'bathrooms') |
    preprocessing.StandardScaler() |
    linear_model.LinearRegression()
)
metric = metrics.MAE()

def predict(input):
    for i in input.values():
        # 从请求中获取数据
        x = i
        # 进行预测
        y_pred = model.predict_one(x)
        print(f'input data {x},predict: {y_pred}')


def learn(input):
    # 从请求中获取数据
    global metric
    for label, feature in input.items():
        x = feature
        y = label
        # 更新模型
        model.learn_one(x, y)
        y_pred = model.predict_one(x)
        metric.update(y, y_pred)
        print(f'input feature:{x}, input label:{y}, predict:{y_pred}, metric:{metric}')
    print("model update")


def read_data(filename):
    res = {}
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            a = line
            b = line
            res_a = {}
            pattern = r"\{([^{}]*)\}"
            a = re.findall(pattern, a)
            pattern = r'"(.*?)"'
            matchs = re.findall(pattern, a[0])
            pattern = r":(.*?),"
            temp = re.findall(pattern, a[0])
            values = []
            for i in temp:
                values.append(int(i))
            for k in range(0, len(matchs)):
                res_a[matchs[k]] = values[k]

            pattern = r":(.*?),"
            b = re.findall(pattern, b)
            label = int(b[len(b) - 1])
            res[label] = res_a
    return res


def read_input(filename):
    res = {}
    index = 0
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            a = line
            res_a = {}
            pattern = r"\{([^{}]*)\}"
            a = re.findall(pattern, a)
            pattern = r'"(.*?)"'
            matchs = re.findall(pattern, a[0])
            pattern = r":(.*?),"
            temp = re.findall(pattern, a[0])
            values = []
            for i in temp:
                values.append(int(i))
            for k in range(0, len(matchs)):
                res_a[matchs[k]] = values[k]

            res[index] = res_a
            index = index + 1
    return res


if __name__ == "__main__":
    filename = "./data.txt"
    input1 = read_data(filename)
    filename = "./input.txt"
    input2 = read_input(filename)
    learn(input1)
    predict(input2)
    
    
