# DeepLearning API with pytorch and flask
基于flask打造的深度学习API，帮助你快速发布部署神经网络，
实现训练或测试模型， 框架目前支持多种机器学习与深度学习模型的构建。

## 1. 模型训练
### 可用模型

|  模型    |    接口 |
| ---- | ---- |
|  随机森林 | http://127.0.0.1:5000/model/random_forest |   
|  XGBoost    | http://127.0.0.1:5000/model/xgboost   |
|  K-Means    | http://127.0.0.1:5000/model/k_means   |
|  KNN    | http://127.0.0.1:5000/model/knn   |

### 通用可选参数
#### 必要参数
|  POST参数    |    具体值 |  
| ---- | ---- |
|  dataset | 数据集文件名（str） |    
|  parameter | 模型的入参（dict） |   

#### 可选参数
| 模型的入参（dict） |  具体值 |
| ---- | ---- |
| predict |   预测的属性（表格字段名） |
| learning_rate |   学习率（1 - 0.01） |
| test_data_ratio |   测试集的比例（1 - 0.01） |
| batch_size |   batch大小（512 - 16） |
### 训练范例
***Endpoint:***

```bash
Method: POST
Type: RAW
URL: http://127.0.0.1:5000/model/xgboost
```


***Body:***

```json        
{
    "dataset": "diabetes_binary_health_indicators_BRFSS2015.csv",
    "parameter": {
        "predict": "Diabetes_binary",
        "learning_rate": 0.1
    }
}
```




## 2. 预测



***Endpoint:***

### 通用预测接口
```bash
Method: GET
Type: RAW
URL: http://127.0.0.1:5000/model/predict
```

### 测试样例
```json        
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
### 返回结果
```json
{
    "data": {
        "0": {
            "precision": 0.0,
            "recall": 0.0,
            "f1-score": 0.0,
            "support": 0
        },
        "1": {
            "precision": 1.0,
            "recall": 0.6443878633566731,
            "f1-score": 0.783741935483871,
            "support": 14139
        },
        "accuracy": 0.6443878633566731,
        "macro avg": {
            "precision": 0.5,
            "recall": 0.32219393167833654,
            "f1-score": 0.3918709677419355,
            "support": 14139
        },
        "weighted avg": {
            "precision": 1.0,
            "recall": 0.6443878633566731,
            "f1-score": 0.783741935483871,
            "support": 14139
        }
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

