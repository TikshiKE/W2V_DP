# W2V_DP
### This repository is a solution to the problem for the Galatyx team using W2V processing.

#### The application works in two modes:
1. Batch processing - to do this, you need to run the application with following parametrs:
```python
python main.py batch
```
2. Processing on-fly user input - for this you need to run:
```python
python main.py user
```

### To create deploy the app with help of Docker do the following:
1. Create an image:
docker build -t g_task_img:latest .
2. Create containter from image:
docker create -it --name g_task_container g_task_img:latest
3. Run the container:
docker start g_task_container
4. Enter bash terminal
docker exec -it g_task_container bash

### NOTE: App works with data that was provided by Galatyx team, to be specific: GoogleNews-vectors-negative300.bin.gz
Archive itself is NOT INCLUDED in the git reposiroty.
However small script load_w2v_gensim_to_csv.py was created for process archive if needed.
To create the CSV file from GoogleNews-vectors-negative300.bin.gz please do the following:
1. Download the GoogleNews-vectors-negative300.bin.gz
   https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM
2. Add downloaded archive to src folder
3. Run the load_w2v_gensim_to_csv.py by:
```python
python load_w2v_gensim_to_csv.py
```
