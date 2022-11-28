# DeepLearning API with pytorch and flask
基于flask打造的深度学习API，帮助你快速发布部署神经网络，
实现训练或测试模型， 框架目前支持多种机器学习与深度学习模型的构建。

## 1. 模型训练


***Endpoint:***

```bash
Method: POST
Type: RAW
URL: http://127.0.0.1:5000/model/xgboost
```


***Body:***

```js        
{
    "dataset": "diabetes_binary_health_indicators_BRFSS2015.csv",
    "parameter": {
        "predict": "Diabetes_binary"
    }
}
```



## 2. 预测



***Endpoint:***

```bash
Method: GET
Type: RAW
URL: http://127.0.0.1:5000/model/predict
```



***Body:***

```js        
{
    "data": {
        "HighBP": 1,
        "HighChol": 1,
        "CholCheck": 1,
        "BMI": 30,
        "Smoker": 1,
        "Stroke": 1,
        "HeartDiseaseorAttack": 1,
        "PhysActivity": 1,
        "Fruits": 0,
        "Veggies": 0,
        "HvyAlcoholConsump": 0,
        "AnyHealthcare": 1,
        "NoDocbcCost": 0,
        "GenHlth": 4,
        "MentHlth": 0,
        "PhysHlth": 20,
        "DiffWalk": 1,
        "Sex": 1,
        "Age": 7,
        "Education": 3,
        "Income": 1
    }
}
```

## 3. 上传数据集



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: http://127.0.0.1:5000/dataset
```



***Body:***

```js        
{
    "name": "test.csv",
    "data": [
        {
            "address": "华山路31号",
            "addressExtend": "屯溪老街"
        },
        {
            "address": "金城镇 珠山82号",
            "addressExtend": "101"
        }
    ]
}
```

##
