import streamlit as st
import pandas as pd
from views import View

class ListarHorarioUI:
    @staticmethod
    def main():
        st.header("Horários Disponíveis")
        ListarHorarioUI.listar()

    @staticmethod
    def listar():
        tipo_usuario = st.session_state.get("tipo")  # Tipo de usuário: 'cliente' ou 'profissional'
        horarios = View.horario_listar_disponiveis()  # Supondo que retorna todos os horários disponíveis
        if len(horarios) == 0:
            st.write("Nenhum horário disponível")
        else:
            dic = []
            for obj in horarios:
                dic.append(obj.to_json())
            df = pd.DataFrame(dic)

            # Filtragem baseada no tipo de usuário
            if tipo_usuario == 'cliente':
                # Cliente visualiza todos os horários, ou apenas os não reservados
                st.dataframe(df)
            elif tipo_usuario == 'profissional':
                # Profissional visualiza apenas os seus horários
                id_profissional = st.session_state.get("id_profissional")  # ID do profissional, armazenada na sessão
# se não funcionar tente: id_profissional = st.session_state.get("id")
                # Filtra os horários pelo ID do profissional
                df_profissional = df[df['id_profissional'] == id_profissional]  # Filtra a tabela com base no ID
                if df_profissional.empty:
                    st.write(f"Nenhum horário agendado para o profissional {id_profissional}")
                else:
                    st.dataframe(df_profissional)
