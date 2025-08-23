Northeastern's 2025 Fed Challenge team git repo for data viz code.

# How to use this repo
0. Have Python and an IDE of your choice installed on your computer.

1. Make an empty local folder and clone this repo into it.

2. Open up the folder that has the repo and create a new venv in the folder. With the venv activate and navigated to the NEUFed2025 directory, run "pip install -r requirements.txt" to install the correct packages.

3. Go to https://fred.stlouisfed.org/ and make an account. Once you've done that click on the profile icon. Click "API Keys" and then request an API Key for personal use (delivery should be instantenous). Copy and paste the API key into the .txt file at "graph_code/fred_api_key.txt". Don't leave any spaces or extra text

4. Go to the example.ipynb and follow the steps for using the graph template! Happy graphing! 


FRED API docs are here: https://fred.stlouisfed.org/docs/api/fred/
fredapi.py docs are here: https://pypi.org/project/fredapi/