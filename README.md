# Assignment

- The code is present in the src folder. 
- app.py is the Flask api as a wrapper of the code scripts
- model.py and mongo_db.py are the code scripts containing the logic.
- .env file contains the environment variables 
- It reads the csv file as mentioned in the .env file and based on the target column mentioned in the .env file it generates a linear regression model and evaluates the model prediction. 
- The required results are then stored in the MongoDb

## Package Installation

Use the requirements.txt file present to install the packages required to run the project.

```bash
pip install -r requirements.txt
```
