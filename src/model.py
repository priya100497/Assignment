import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from decouple import config
from mongo_db import insert_into_mongodb


def model_eval_and_store():

    # Load dataset
    data_path = config("CSV_FILE_PATH")
    target_column = config("TARGET_COLUMN")

    dataset = pd.read_csv(data_path)

    # Data processing
    X = dataset.drop([target_column], axis=1)
    y = dataset[target_column]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Generate model
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    # Model evaluation
    y_train_pred = lr.predict(X_train)
    y_test_pred = lr.predict(X_test)

    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)

    # Result prep 
    tenant_detail = {"file_location": data_path,
                     "data": dataset.to_dict(orient='records')}
    project_metadata_detail = {"file_location": data_path, "model_eval_result": {
        "train_mse": train_mse, "test_mse": test_mse}}

    # # Store to MongoDb 
    # insert_into_mongodb(payload=tenant_detail,
    #                     db_name="lr_model", collection_name="tenant")
    # insert_into_mongodb(payload=project_metadata_detail,
    #                     db_name="lr_model", collection_name="project_metadata")

    return {"tenant": tenant_detail,
            "project_metadata": project_metadata_detail}
