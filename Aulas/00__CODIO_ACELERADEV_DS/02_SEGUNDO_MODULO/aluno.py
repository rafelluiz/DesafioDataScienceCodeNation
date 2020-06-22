import streamlit as st

def main():
  st.title('Aula Streamlit')
  st.markdown('# Botão')
  botao = st.button('Botao')

  if botao:
    st.markdown('**Botão Clicado**')

  st.markdown('Checkbox')

  check = st.checkbox('CheckBox')
  if check:
    st.markdown('__Clicado__')

  st.markdown('Radio:')
  radio = st.radio('Escolha as opçoes',['Opt 1','Opt 2'])
  if radio == 'Opt 1':
    st.markdown('Opt 1')
  else:
    st.markdown('Opt 2')

  st.markdown('Selectbox')
  select = st.selectbox('Choose opt',['Opt 1','Opt 2'])
  if select == 'Opt 1':
    st.markdown('Opt 1')
  else:
    st.markdown('Opt 2')

  st.markdown('MultSelect')
  multi_select = st.multiselect('Chose: ',['Opt 1','Opt 2','Opt 3','Opt 4','Opt 5'])
  if multi_select:
    imprimir_multiselect = ''
    for i in multi_select:
      imprimir_multiselect += f' {i}'
    st.markdown(imprimir_multiselect)


if __name__ == '__main__':
  main()