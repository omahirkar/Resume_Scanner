# -*- coding: utf-8 -*-
"""Resume Scanner.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bsgKXdWGjAovSME0hWGicCjhOXYNamNn
"""



!pip install docx2txt

import docx2txt

job_description = docx2txt.process('/content/Shubham RESUME.docx')
resume=docx2txt.process('/content/Shubham RESUME.docx')

print(resume)

content= [job_description,resume]

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
matrix= cv.fit_transform(content)

from sklearn.metrics.pairwise import cosine_similarity
similarity_matrix= cosine_similarity(matrix)

print(similarity_matrix)

print("Resume matches by: "+ str(similarity_matrix[1][0]*100)+"%")

