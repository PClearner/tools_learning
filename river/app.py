from flask import Flask, request, jsonify
from river import linear_model, preprocessing

# 初始化Flask应用
app = Flask(__name__)

# 创建一个标准化器和线性回归模型的管道
model = preprocessing.StandardScaler() | linear_model.LinearRegression()

@app.route('/predict', methods=['POST'])
def predict():
    # 从请求中获取数据
    data = request.json
    x = data['features']

    # 进行预测
    y_pred = model.predict_one(x)

    return jsonify({'prediction': y_pred})

@app.route('/learn', methods=['POST'])
def learn():
    # 从请求中获取数据
    data = request.json
    x = data['features']
    y = data['label']

    # 更新模型
    model.learn_one(x, y)

    return jsonify({'status': 'Model updated'})

if __name__ == '__main__':
    app.run(debug=True)
