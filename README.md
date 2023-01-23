# sojern-task
### Tasks are written in Python

## 1. Comparing versions task is in 'compare_versions' folder and 'solve.py' file. You can run it 'python3 solve.py' easily. It will show result with test cases.

## 2. On math api service used Django framework, so please set up python environment
In your python environment please install requirements as pip install -r requirements.txt
Then you can simply run server as 'python3 manage.py runserver'

Each server is post server and get JSON data like:
`
    {
        "numbers": [1, 2, 3, -4],
        "percentile": 100
    }
`

## 3. For the favorite dogs task, I have to write the simplest pure Javascript code. So I wrote separate 2 index.html and favorites.html files.
When you click any media on index.html, It will add the URL to local storage and you can find it at favorites.html.