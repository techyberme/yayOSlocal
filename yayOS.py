import streamlit as st
import pandas as pd
import plotly.express as px
import hmac
import csv
import time
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the passward is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Contraseña incorrecta, si no recuerda su contraseña contacte con su proveedor")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.

precios=[]
horas=[]
maximo=0.0
with open('data.csv', mode ='r')as file:
# reading the CSV file
    csvFile = csv.reader(file)
     # Skip the header row
    next(csvFile, None)
    
    for lines in csvFile:
        precios.append(float(lines[1]))
        horas.append(lines[0])
maximo=max(precios)
avg=round(sum(precios)/len(precios),2)
posmax=precios.index(maximo) #gets the position of the maximum value
horamax= horas[posmax]

st.write("""
# Hola Yay@

""")
 
with st.sidebar:
     st.title('Tu Lavavajillas')
     st.info('Qué toca hoy')
     choice = st.radio('Menú', ['Precios', 'Aparatos', 'Programas', 'Datos del lavavajillas'])
if choice == 'Precios':
     st.write("Estos son los precios")
     st.title('Gráfica de precios')
     st.write("La media de hoy es", avg, "€/MWh")
     st.write('El precio máximo hoy es:', maximo, '€/MWh a las',horamax,'horas' )
     df=pd.read_csv('data.csv')
     fig = px.line(df, x="hora", y="precio [€/MWh]", title='Precios de hoy')  #I have used plotly.express so I can see the price by passing the cursor over the graphs
     st.plotly_chart(fig)
     
if choice == 'Aparatos':
     col1, col2, col3 = st.columns([2,3,1])
     boton='lavavajillas'
     on = col1.toggle(boton)
     if on:
          
          col2.write(":white_check_mark:")
     else: 
           
          col2.write(":x:")
     st.write('Secadora')
     container_2 = st.empty()
     button_A = container_2.button('Encender')
     if button_A:
          container_2.empty()
          button_B = container_2.button('Apagar')
if choice== "Programas":
        st.subheader('Escoge el programa')
        col1, col2, col3 = st.columns([3,3,3])
        on=col1.toggle("económico")
        if on:
          with st.empty():
               for secs in range(1200,0,-1):
                    mm, ss = secs//60, secs%60
                    st.metric("⏳ Quedan: ", f"{mm:02d}:{ss:02d}")
                    time.sleep(1)
                    st.write("✔️ ¡terminado!")
        on1= col2.toggle("a fondo")
        if on1:
              with col2.empty():
               for secs in range(1800,0,-1):
                    mm, ss = secs//60, secs%60
                    st.metric("⏳ Quedan: ", f"{mm:02d}:{ss:02d}")
                    time.sleep(1)
                    st.write("✔️ ¡Terminado!")
        on2= col3.toggle("rápido")
        if on2:
              with col3.empty():
               for secs in range(600,0,-1):
                    mm, ss = secs//60, secs%60
                    st.metric("⏳ Quedan: ", f"{mm:02d}:{ss:02d}")
                    time.sleep(1)
                    st.write("✔️ ¡Terminado!")

if choice== "Datos del lavavajillas":
    col1, col2, col3 = st.columns([2,3,1])
    col1.write("¿Puerta abierta?")
    on = col2.toggle("")
    col1.write('Programas realizados hoy:')

    

          


          
 
      
