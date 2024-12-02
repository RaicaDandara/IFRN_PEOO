import streamlit as st
import pandas as pd
from views import View
import time

class AbrirContaUI:
    def main():
        st.header("Abrir Conta no Sistema")
        AbrirContaUI.inserir()

    def inserir():
        st.subheader("Escolha o tipo de conta")
        tipo_conta = st.radio("Tipo de conta", ["Cliente", "Profissional"])

        if tipo_conta == "Cliente":
            nome = st.text_input("Informe o nome")
            email = st.text_input("Informe o e-mail")
            fone = st.text_input("Informe o telefone")
            senha = st.text_input("Informe a senha", type="password")

            if st.button("Inserir"):
                if not nome or not email or not fone or not senha:
                    st.error("Todos os campos são obrigatórios para criar uma conta de cliente.")
                else:
                    View.cliente_inserir(nome, email, fone, senha)
                    st.success("Conta de cliente criada com sucesso!")
                    time.sleep(2)
                    st.experimental_rerun()

        elif tipo_conta == "Profissional":
            nome = st.text_input("Informe o nome")
            email = st.text_input("Informe o e-mail")
            espec = st.text_input("Informe a especialidade")
            cons = st.text_input("Informe o conselho")
            senha = st.text_input("Informe a senha", type="password")

            if st.button("Inserir"):
                if not nome or not email or not espec or not cons or not senha:
                    st.error("Todos os campos são obrigatórios para criar uma conta de profissional.")
                else:
                    View.profissional_inserir(nome, email, espec, cons, senha)
                    st.success("Conta de profissional criada com sucesso!")
                    time.sleep(2)
                    st.rerun()
