import streamlit as st
import time
from views import View

class Configuracao:
    @staticmethod
    def main():
        st.header("Configurações de Conta")
        Configuracao.atualizar()

    @staticmethod
    def atualizar():
        tipo = st.session_state.get("tipo")
        if tipo == "Cliente":
            cliente_id = st.session_state.get("id")  # Alterado para usar a chave consistente
            cliente = next((c for c in View.cliente_listar() if c.id == cliente_id), None)
            
            if cliente is None:
                st.error("Cliente não encontrado.")
                return
            nome = st.text_input("Informe o novo nome", cliente.nome)
            email = st.text_input("Informe o novo e-mail", cliente.email)
            fone = st.text_input("Informe o novo telefone", cliente.fone)
            senha = st.text_input("Informe a nova senha", cliente.senha, type="password")

            if st.button("Atualizar"):
                View.cliente_atualizar(cliente_id, nome, email, fone, senha, cliente.id_perfil)
                st.success("Dados atualizados com sucesso!")
                time.sleep(2)
                st.rerun()

        elif tipo == "Profissional":
            profissional_id = st.session_state.get("id")  # Alterado para usar a chave consistente
            profissional = next((p for p in View.profissional_listar() if p.id == profissional_id), None)
            
            if profissional is None:
                st.error("Profissional não encontrado.")
                return
            nome = st.text_input("Informe o novo nome", profissional.nome)
            email = st.text_input("Informe o novo e-mail", profissional.email)
            especialidade = st.text_input("Informe a nova especialidade", profissional.especialidade)
            conselho = st.text_input("Informe o novo conselho", profissional.conselho)  # Corrigido de 'concelho' para 'conselho'
            senha = st.text_input("Informe a nova senha", profissional.senha, type="password")

            if st.button("Atualizar"):
                View.profissional_atualizar(profissional_id, nome, email, especialidade, conselho, senha)
                st.success("Dados atualizados com sucesso!")
                time.sleep(2)
                st.rerun()

        else:
            st.error("Tipo de usuário não identificado.")
