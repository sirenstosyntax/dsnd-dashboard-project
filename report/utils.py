import pickle
from pathlib import Path

# report/utils.py is 2 levels deep, so .parent.parent reaches project root
project_root = Path(__file__).resolve().parent.parent

# model.pkl lives in assets/ at the project root
model_path = project_root / 'assets' / 'model.pkl'

def load_model():
    with model_path.open('rb') as file:
        model = pickle.load(file)
    return model