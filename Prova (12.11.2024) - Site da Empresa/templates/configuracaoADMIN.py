import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime
class ConfiguracaoADMIN:
    def main():
        st.header("Horários Disponíveis")
        ConfiguracaoADMIN.atualizar()
    def atualizar():
        cliente_id = st.session_state.get("cliente_id")
        if cliente_id is None:
            st.error("Nenhum cliente logado.")
            return

        cliente = next((c for c in View.cliente_listar() if c.id == cliente_id), None)

        if cliente:
            nome = cliente.nome
            email = cliente.email
            fone = cliente.fone
            senha = st.text_input("Informe a nova senha", cliente.senha, type="password")

            if st.button("Atualizar"):
                View.cliente_atualizar(cliente_id, nome, email, fone, senha)
                st.success("Dados atualizados com sucesso!")
                time.sleep(2)
                st.rerun()
        else:
            st.error("Cliente não encontrado.")