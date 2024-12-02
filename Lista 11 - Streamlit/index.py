from templates.manterclienteUI import ManterClienteUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterservicoUI import ManterServicoUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.abrircontaUI import AbrirContaUI
from templates.listarhorarioUI import ListarHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.manterperfilUI import ManterPerfilUI 
from templates.loginUI import LoginUI
from views import View

import streamlit as st

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": 
            LoginUI.main()
        if op == "Abrir Conta": 
            AbrirContaUI.main()
               
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Perfis", "Cadastro de Profissionais", "Cadastro de Serviços", "Abrir Agenda do Dia", "Configurações"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Perfis": ManterPerfilUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Horários Disponíveis", "Configurações"])
        if op == "Horários Disponíveis": ListarHorarioUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Gerenciar Horários", "Configurações"])
        if op == "Gerenciar Horários": ManterHorarioUI.main()
        if op == "Configurações": ManterPerfilUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["id"]
            del st.session_state["nome"]
            del st.session_state["tipo"]
            st.experimental_rerun()
    
    def sidebar():
        if "id" not in st.session_state:
            # Usuário não está logado
            IndexUI.menu_visitante()   
        else:
            # Usuário está logado, mostra o menu correspondente
            tipo = st.session_state.get("tipo", "")
            st.sidebar.write("Bem-vindo(a), " + st.session_state["nome"])
            
            if tipo == "Admin": 
                IndexUI.menu_admin()
            elif tipo == "Cliente": 
                IndexUI.menu_cliente()
            elif tipo == "Profissional": 
                IndexUI.menu_profissional()
            
            IndexUI.sair_do_sistema()
    
    def main():
        # Verifica se o usuário admin existe
        View.cliente_admin()
        # Monta o sidebar
        IndexUI.sidebar()
       
IndexUI.main()