import streamlit as st
from views import View
import time

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        
        if st.button("Entrar"):
            # Tenta autenticar como cliente
            cliente = View.cliente_autenticar(email, senha)
            # Tenta autenticar como profissional
            profissional = View.profissional_autenticar(email, senha)
            
            if cliente is None and profissional is None:
                st.error("E-mail ou senha inválidos")
            else:
                if cliente:
                    st.session_state["id"] = cliente["id"]
                    st.session_state["nome"] = cliente["nome"]
                    st.session_state["tipo"] = "Cliente"
                elif profissional:
                    st.session_state["id"] = profissional["id"]
                    st.session_state["nome"] = profissional["nome"]
                    st.session_state["tipo"] = "Profissional"
                
                st.success(f"Bem-vindo, {st.session_state['nome']}!")
                time.sleep(2)
                st.rerun()
