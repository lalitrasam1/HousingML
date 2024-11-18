# HousingML

git clone https://github.com/lalitrasam1/HousingML.git

cd "E:\Study\Machine learning\GitCodes\HousingML"

conda create -p housing python=3.11.5 -y

. C:/Users/lalit/anaconda3/etc/profile.d/conda.sh init bash

conda activate "E:\Study\Machine learning\GitCodes\HousingML\housing"

conda deactivate

uvicorn main:app --reload

python setup.py build
 pip install -r requirements.txt
python setup.py install
pip install ipykernel
git add .
 git commit -m "first"
  git push origin main

  https://www.kaggle.com/code/harshwalia/end-to-end-ml-project-all-steps-in-detail