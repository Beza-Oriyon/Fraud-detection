from xgboost import XGBClassifier
import joblib

def train_xgboost(X_train, y_train, params=None):
    if params is None:
        params = {
            'n_estimators': 300,
            'max_depth': 6,
            'learning_rate': 0.1,
            'random_state': 42,
            'eval_metric': 'logloss'
        }
    model = XGBClassifier(**params)
    model.fit(X_train, y_train)
    return model

def save_model(model, path='../models/best_model.pkl'):
    joblib.dump(model, path)
    print(f"Model saved to {path}")