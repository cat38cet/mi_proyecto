#primero he abierto en window "MySQL Comand line client" y he introducido mi contraseña de MySQL
#después he abierto un nuevo terminal en visual studio code y he instalado las librerías que necesito

#ahora extraigo datos de la API
import requests
import pandas as pd

response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = response.json()
df_posts = pd.DataFrame(posts)

#en este paso se hace la transformación y análisis de datos
df_posts['title_length'] = df_posts['title'].apply(len)
post_count_by_user = df_posts.groupby('userId').size()
print(post_count_by_user)

#a continuación se cargan los datos en MySQL
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://pipeline_user:password@localhost/pipeline_data')
df_posts.to_sql('posts', con=engine, if_exists='replace', index=False)


