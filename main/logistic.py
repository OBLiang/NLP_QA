import numpy as np
from xgboost import XGBRegressor


def train_model(train_file, test_file, result_file):
    train_data = np.loadtxt('../data/train.data', delimiter=' ')
    test_data = np.loadtxt('../data/dev.data', delimiter=' ')
    train_x = train_data[:, 0: 3]
    train_y = train_data[:, 3]
    test_x = test_data[:, 0: 3]
    model2 = XGBRegressor(
        learn_rate=0.08,
        max_depth=7,
        min_child_weight=4,
        gamma=0,
        subsample=0.8,
        colsample_bytree=0.7,
        reg_alpha=1,
        # scale_pos_weight = 1,
        # reg_lambda= 1,
        objective='reg:logistic',
        n_estimators=120
    )
    # watchlist2 = [(X_train,y_train),(X_test,ytest)]
    trained_model = model2.fit(train_x, train_y)
    predict_train = trained_model.predict(train_x)
    predict_test = trained_model.predict(test_x)
    with open('../data/score_dev', 'w') as f:
        for i in predict_test:
            f.write(str(i) + '\n')
    with open('../data/score_train', 'w') as f:
        for i in predict_train:
            f.write(str(i) + '\n')