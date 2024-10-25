import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.graph_objs as px

import pydeck


#@st.cache_df_encuesta
df_encuesta = pd.read_excel(r'data/AI_Chatbots_Students.xlsx')


df_encuesta['Q2']= df_encuesta['Q2'].str.strip()
print(df_encuesta)



df_limpia = df_encuesta.drop(index=99)

st.sidebar.markdown('<h3 style="color :#17202a"><center>ÉTICA</h3></center>', unsafe_allow_html=True)
st.sidebar.markdown('<h3 style="color :#17202a"><center>INTEGRIDAD</h3></center>', unsafe_allow_html=True)
st.sidebar.markdown('<h3 style="color :#17202a"><center>RESPONSABILIDAD</h3></center>', unsafe_allow_html=True)
st.sidebar.markdown('<h3 style="color :#17202a"><center>RENDICIÓN DE CUENTAS</h3></center>', unsafe_allow_html=True)
st.sidebar.markdown('<h3 style="color :#17202a"><center>PROTECCIÓN DE DATOS</h3></center>', unsafe_allow_html=True)
st.sidebar.markdown('<h3 style="color :#17202a"><center>DERECHOS HUMANOS</h3></center>', unsafe_allow_html=True)

st.sidebar.markdown('<h4 style="color :#17202a"><center>!La IA generativa se ha convertido en una de las mejores herramientas como apoyo a la educación, es cuestión de educar y formar a los estudiantes en un uso responsable!</h4></center>', unsafe_allow_html=True)


st.markdown('<h3 style="color :#17202a"><center>𝘌𝘓 𝘋𝘌𝘚𝘈𝘍𝘐𝘖 𝘌𝘛𝘐𝘊𝘖 𝘋𝘌 𝘓𝘈 𝘐𝘈 𝘠 𝘚𝘜 𝘜𝘚𝘖 𝘌𝘕 𝘌𝘚𝘛𝘜𝘋𝘐𝘈𝘕𝘛𝘌𝘚 𝘜𝘕𝘐𝘝𝘌𝘙𝘚𝘐𝘛𝘈𝘙𝘐𝘖𝘚</h3></center>', unsafe_allow_html=True)



                 
tab1, tab2, tab3, tab4,tab5, tab6, tab7, tab8, tab9= st.tabs(['Datos','Formación','Género','Uso de lA ','Sesgos en la IA','La IA/Educación','T&Valores','Cuestiones Eticas','Analisis de Correlación'])

  
with tab1:    
     

     #DataFrame

     df_encuestadefinitiva=df_limpia.rename (columns= {'Q1':'Nivel Académico','Q2':'Especialidad','Q3':'Género','Q4':'Ha utilizado alguna vez Chat GPT','Q5.1':'Entiendo, Limitaciones de la IA','Q5.2':'Entiendo  que la IA, puede generar datos inexactos','Q5.3':'Entiendo que la IA, información fuera de contexto','Q5.4':'Entiendo que la IA, puede presentar Sesgos','Q5.5':'Entiendo que la IA, puede limitarse en ciertos contextos',
                                                       'Q5.6':'Entiendo que la IA,tienen inteligencia emocional limitada','Q6.1':'Imagino, Integrar la IA en practicas de Enseñanza','Q6.2':' Necesidad de ,Aprender a utilizar herramientas IA','Q6.3':'Las herramientas IA, pueden mejorar mi competencia digital','Q6.4':' las herramientas IA, pueden ayudarme a ahorrar tiempo','Q6.5':'Puede brindarme conocimiento único',
                                                       'Q6.6':'La IA, puede brindarme comentarios inmediatos','Q6.7':'Gran herramienta, por su disponibilidad 24/7','Q6.8':'Gran herramienta, apoyo en el anonimáto','Q7.1':'Creo que la IA, puede socavar el valor de la educación','Q7.2':'Creo que la IA, permite interactuar con otros','Q7.3':'Creo que la IA, puede obstaculizar mis habilitades genéricas','Q7.4':'Puedo volverme dependiente de la IA',
                                                       'Q8.1':'La IA, Apoyo personalizado e inmediato','Q8.2':'la IA, Apoyo lluvia de ideas','Q8.3':'La IA,Soporte de investigación y análisis','Q8.4':'la IA, soporte multimedia','Q8.5':'La IA, soporte administrativo','Q9.1':'La IA, precisión y transparencia','Q9.2':'La IA, privacidad y cuestiones éticas','Q9.3':'La IA, competencias Holísticas','Q9.4':'La IA, perspectivas profesionales',
                                                       'Q9.5':'La IA, Valores Humanos','Q10':'La IA, ventajas, desventajas, experiencias'}
                                                       
                                             )
     print(df_encuestadefinitiva)

     ver_DataFrame =st.toggle('Ver tabla de Datos')
     if  ver_DataFrame:
          st.dataframe(df_encuestadefinitiva, use_container_width=True)

     #KPIS

     
     numero_encuestados = df_encuestadefinitiva['Código Estudiante'].count()
     estudiantes_pregrado= (df_encuestadefinitiva['Nivel Académico']==1).sum()
     estudiantes_posgrado= (df_encuestadefinitiva['Nivel Académico']==2).sum()
     col1,col2,col3 = st.columns(3)
     st.markdown(
    f"""
    <style>
    .metrics-container {{
        display: flex;
        justify-content: space-around;  /* Espaciado entre elementos */
        font-size: 24px;
        color: #4CAF50;  /* Color del texto */
    }}
    .metric-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
    }}
    .metric-title {{
        font-size: 18px;
        margin-bottom: 5px;
    }}
    .metric-value {{
        font-size: 32px;
        font-weight: bold;
    }}
    </style>
    <div class="metrics-container">
        <div class="metric-container">
            <div class="metric-title">Número Estudiantes Encuestados</div>
            <div class="metric-value">{numero_encuestados}</div>
        </div>
        <div class="metric-container">
            <div class="metric-title">Estudiantes de Pregrado</div>
            <div class="metric-value">{estudiantes_pregrado}</div>
        </div>
        <div class="metric-container">
            <div class="metric-title">Estudiantes de Posgrado</div>
            <div class="metric-value">{estudiantes_posgrado}</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
     

    
     

with tab2:
#Especialidad
     
     tablarespuestas={
          'Número': ['1','2'],
          'Respuestas':['Pregrado ','Posgrado']          
          }

     
     df_tabla =pd.DataFrame(tablarespuestas)
     df_tabla.reset_index(drop=True, inplace=True)
     st.markdown(df_tabla.to_html(index=False), unsafe_allow_html=True)


     colorbarras= ['#FFD700','#F08080','#00FF00']

     
     especialidades = df_encuestadefinitiva['Especialidad'].unique()
     

     # Lista múltiple para seleccionar especialidades
     seleccionadas = st.multiselect(
     'Selecciona una o más especialidades:',
     options=especialidades,
     default=especialidades.tolist()  # Por defecto, muestra todas
     )

     # Filtra el DataFrame según la selección
     if seleccionadas:
          df_filtrado = df_encuestadefinitiva[df_encuestadefinitiva['Especialidad'].isin(seleccionadas)]
     else:
          df_filtrado = df_encuestadefinitiva

     # Crea el gráfico
     plt.figure(figsize=(7, 4))
     df_filtrado['Especialidad'].value_counts().plot(kind='barh', title='Especialidad o Carrera de los encuestados', width=0.3, color=colorbarras)
     plt.xlabel('Número de encuestados')  # Etiqueta del eje X
     plt.ylabel('Especialidad')  # Etiqueta del eje Y
     st.pyplot(plt)
     plt.close()

    


    
#Género
with tab3:

     
     colores = ['#F6CEF5', '#58ACFA',]
     counts = df_encuestadefinitiva['Género'].value_counts()
     plt.figure(figsize=(10, 6))
     plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=80, colors=colores)
     plt.axis('equal')
     st.markdown("<h4 style='color: #848484;'>Género de los encuestados donde 1 es Género Femenino y 2 es Género Masculino</h4>", unsafe_allow_html=True)
     st.pyplot(plt)

     


with tab4:
     #Uso de la Ia entre los participantes
 

     tablarespuestas={
          'Número': ['1','2','3','4','5'],
          'Respuestas':['NUNCA ','RARA VEZ','A VECES ','A MENUDO','MUY A MENUDO']          
          }


     df_tabla =pd.DataFrame(tablarespuestas)
     df_tabla.reset_index(drop=True, inplace=True)
     st.markdown(df_tabla.to_html(index=False), unsafe_allow_html=True)


     colores = ['#FF9933', '#990066','#99CCCC']
     df_UsodeIAgenerativa = df_encuestadefinitiva.groupby(['Ha utilizado alguna vez Chat GPT']).count()['Código Estudiante']
     plt.figure(figsize=(10, 5))
     colors = ['#99CCFF', '#00CC99','#9966FF','#669999','#66FF33']  
     plt.barh(df_UsodeIAgenerativa.index, df_UsodeIAgenerativa.values, color=colors)


     plt.xlabel('Número de Estudiantes')
     plt.title('Uso de Chat GPT')
     plt.grid(axis='x')


     st.pyplot(plt)
    



with tab5:

#Sesgos



#tabla de respuestas

     tablarespuestas={
          'Número': ['1','2','3','4','5'],
          'Respuestas':['NUNCA ','RARA VEZ','A VECES ','A MENUDO','MUY A MENUDO']          
          }


     df_tabla =pd.DataFrame(tablarespuestas)
     df_tabla.reset_index(drop=True, inplace=True)
     st.markdown(df_tabla.to_html(index=False), unsafe_allow_html=True)

     df_Sesgos= df_encuestadefinitiva.groupby(['Entiendo que la IA, puede presentar Sesgos']).count()['Código Estudiante']
     colores = ['#FF9933', '#990066','#99CCCC']
     plt.figure(figsize=(10, 5))
     colors = ['#990066', '#00CC99','#9966FF','#330033','#66FF33']  
     plt.barh(df_UsodeIAgenerativa.index, df_UsodeIAgenerativa.values, color=colors)


     plt.xlabel('Número de Estudiantes')
     plt.title('Entiendo que la IA, puede presentar Sesgos')
     plt.grid(axis='x')


     st.pyplot(plt)

with tab6:

     #Socavar la educación

 


     tablarespuestas={
          'Número': ['1','2','3','4','5'],
          'Respuestas':['NUNCA ','RARA VEZ','A VECES ','A MENUDO','MUY A MENUDO']          
          }

     colores = ['#FF9933', '#990066','#99CCCC']
     df_tabla =pd.DataFrame(tablarespuestas)
     df_tabla.reset_index(drop=True, inplace=True)
     st.markdown(df_tabla.to_html(index=False), unsafe_allow_html=True)

     fig, ax = plt.subplots()
     ax.hist(df_encuestadefinitiva['Creo que la IA, puede socavar el valor de la educación'])  

     with st.container(border=True):
          st.markdown( "<h4 style='color: #848484;'>Creo que la IA, puede socavar el valor de la educación</h4>", unsafe_allow_html=True)
          st.pyplot(fig)


with tab7:




     #Precisión y Transparencia & valores Humanos

     tablarespuestas={
          'Número': ['1','2','3','4','5'],
          'Respuestas':['NUNCA ','RARA VEZ','A VECES ','A MENUDO','MUY A MENUDO']          
          }
     

     df_tabla =pd.DataFrame(tablarespuestas)
     df_tabla.reset_index(drop=True, inplace=True)
     st.markdown(df_tabla.to_html(index=False), unsafe_allow_html=True)
     
          
     
     df_trasp_valores = pd.DataFrame(df_encuestadefinitiva, columns=['La IA, precisión y transparencia', 'La IA, Valores Humanos'])
     columns=['La IA, precisión y transparencia','La IA, Valores Humanos']
     st.line_chart(df_trasp_valores)

     categorias = ['La IA, precisión y transparencia', 'La IA, Valores Humanos']
     valores1 = [1, 5] 
     valores2 = [1, 5]
     x = np.arange(len(categorias))
     ancho = 0.3

     fig, ax = plt.subplots()
     barras1 = ax.bar(x - ancho/2, valores1, ancho, label='Precisión/Valores Humanos', color='#669999')
     barras2 = ax.bar(x + ancho/2, valores2, ancho, label='Transparencia', color='#99CCFF')

     ax.set_xlabel('Categorías')
     ax.set_ylabel('Respuestas(1-5)')
     ax.set_title('Conocimiento de precision y transparencia & Valores humanos en la IA')
     ax.set_xticks(x)
     ax.set_xticklabels(categorias)
     ax.legend()
     ax.set_ylim(0, 6) 
     st.pyplot(fig)

with tab8:
 
      #Privacidad y cuestiones éticas

     tablarespuestas={
          'Número': ['1','2','3','4','5'],
          'Respuestas':['NUNCA ','RARA VEZ','A VECES ','A MENUDO','MUY A MENUDO']          
          }


     df_tabla =pd.DataFrame(tablarespuestas)
     df_tabla.reset_index(drop=True, inplace=True)
     st.markdown(df_tabla.to_html(index=False), unsafe_allow_html=True)

     colores = ['#CCFFFF', '#FFCCFF','#FFCC66','#FF9999','#FFFF00']
     counts = df_encuestadefinitiva['La IA, privacidad y cuestiones éticas'].value_counts()
     plt.figure(figsize=(10, 6))
     plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=80, colors=colores)
     plt.axis('equal')
     st.markdown("<h4 style='color: #848484;'>Conozco el conepto: ' Privacidad y cuestiones éticas en la IA'</h4>", unsafe_allow_html=True)
     st.pyplot(plt)

with tab9:


     #Analisis de Correlación



     columnas_para_analisis=['Entiendo que la IA, puede presentar Sesgos','Creo que la IA, puede socavar el valor de la educación','La IA, precisión y transparencia','La IA, privacidad y cuestiones éticas','La IA, Valores Humanos']
     nuevodtframe = df_encuestadefinitiva[columnas_para_analisis]
     
     ver_DataFrame1 =st.toggle('Ver nuevo Dataframe')
     if  ver_DataFrame1:
          st.write(nuevodtframe)

     fig = sns.pairplot(nuevodtframe)


     st.pyplot(fig)

     data_points=np.random.normal(0,1,100) # Datos aleatorios para demostración
     corr = nuevodtframe.corr()

     plt.figure(figsize=(7, 7))
     sns.heatmap(corr, cmap="Greens", annot=True)


     st.pyplot(plt)

















    





