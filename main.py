import pandas as pd
import streamlit as st


def init_state():
    if "step" not in st.session_state:
        st.session_state.step = 1

    if "form_data" not in st.session_state:
        st.session_state.form_data = {}


init_state()

st.title("Inspeção Diária ou Homologação - Qualidade Industrial")

st.progress(st.session_state.step / 6)

if st.session_state.step == 1:
    st.header("Etapa 1: Informações Gerais")

    with st.form("form_etapa_1", enter_to_submit=False):
        nome = st.text_input("Nome Operador")
        data = st.date_input("Data", format="DD/MM/YYYY")
        horario_inicio = st.time_input("Horario de Início", step=300)
        ordem_producao = st.text_input("Ordem de Produção")
        item = st.text_input("Item")
        pedido = st.text_input("Pedido")
        descricao = st.text_input("Descrição")
        cliente = st.text_input("Cliente")

        campos_obrigatorios = [
            nome,
            data,
            horario_inicio,
            ordem_producao,
            item,
            pedido,
            descricao,
            cliente,
        ]

        submitted = st.form_submit_button("Próximo")

        if submitted:
            if not all(campos_obrigatorios):
                st.error("Por favor, preencha todos os campos.")
            else:
                st.session_state.form_data["nome"] = nome
                st.session_state.form_data["data"] = data
                st.session_state.form_data["horario_inicio"] = horario_inicio
                st.session_state.form_data["ordem_producao"] = ordem_producao
                st.session_state.form_data["item"] = item
                st.session_state.form_data["pedido"] = pedido
                st.session_state.form_data["descricao"] = descricao
                st.session_state.form_data["cliente"] = cliente

                st.session_state.step = 2
                st.rerun()

elif st.session_state.step == 2:
    st.header("Etapa 2: Informações Tinta/Produção")

    with st.form("form_etapa_2", enter_to_submit=False):
        cor = st.text_input("Cor da Tinta")
        fornecedor = st.text_input("Fornecedor")
        lote = st.text_input("Lote")
        barra = st.text_input("Barra")

        col1, col2, col3 = st.columns([2, 10, 2])
        with col1:
            voltar = st.form_submit_button("Voltar")
        with col3:
            submitted = st.form_submit_button("Próximo")

        if voltar:
            st.session_state.step = 1
            st.rerun()

        campos_obrigatorios = [cor, fornecedor, lote, barra]

        if submitted:
            if not all(campos_obrigatorios):
                st.error("Por favor, preencha todos os campos.")
            else:
                st.session_state.form_data["cor"] = cor
                st.session_state.form_data["fornecedor"] = fornecedor
                st.session_state.form_data["lote"] = lote
                st.session_state.form_data["barra"] = barra

                st.session_state.step = 3
                st.rerun()

elif st.session_state.step == 3:
    st.header("Etapa 3: Informações Máquina")

    with st.form("form_etapa_3", enter_to_submit=False):
        ultima_troca_venturi = st.date_input(
            "Última Troca Venturi", value=None, format="DD/MM/YYYY"
        )

        col1, col2 = st.columns(2)

        velocidades_cabine_reciprocador = [0] * 2
        tensoes = [0] * 2

        with col1:
            velocidades_cabine_reciprocador[0] = st.number_input("Velocidade Cabine Reciprocador 1")
            tensoes[0] = st.number_input("Tensão 1")
            velocidade_cabine_painel_2_100 = st.number_input("Velocidade Cabine Painel 2 (%)", format="%0.1f", step=0.1)
            velocidade_estufa_rapida_100 = st.number_input("Velocidade Estufa (Rápida) (%)", format="%0.1f", step=0.1)
        with col2:
            velocidades_cabine_reciprocador[1] = st.number_input("Velocidade Cabine Reciprocador 2")
            tensoes[1] = st.number_input("Tensão 2")
            velocidade_cabine_painel_2 = st.number_input("Velocidade Cabine Painel 2")
            velocidade_estufa_rapida = st.number_input("Velocidade Estufa (Rápida)")

        col1, col2, col3 = st.columns([2, 10, 2])
        with col1:
            voltar = st.form_submit_button("Voltar")
        with col3:
            submitted = st.form_submit_button("Próximo")

        if voltar:
            st.session_state.step = 2
            st.rerun()

        campos_obrigatorios = []

        if submitted:
            if not all(campos_obrigatorios):
                st.error("Por favor, preencha todos os campos.")
            else:
                st.session_state.form_data["velocidades_cabine_reciprocador"] = velocidades_cabine_reciprocador
                st.session_state.form_data["tensoes"] = tensoes
                st.session_state.form_data["velocidade_cabine_painel_2_100"] = velocidade_cabine_painel_2_100
                st.session_state.form_data["velocidade_estufa_rapida_100"] = velocidade_estufa_rapida_100
                st.session_state.form_data["velocidade_cabine_painel_2"] = velocidade_cabine_painel_2
                st.session_state.form_data["velocidade_estufa_rapida"] = velocidade_estufa_rapida

                st.session_state.step = 4
                st.rerun()

elif st.session_state.step == 4:
    st.header("Etapa 4: Informações Máquina (Temperaturas)")

    with st.form("form_etapa_4", enter_to_submit=False):

        col1, col2 = st.columns(2)

        velocidades_cabine_reciprocador = [0] * 2
        tensoes = [0] * 2

        with col1:
            st.text("Program.")

            entrada_estufa_program = st.number_input("Entrada Estufa")
            saida_estufa_program = st.number_input("Saída Estufa")
            pressao_bicos_deseng_fosf_program = st.number_input("Pressão Bicos Deseng/Fosf")

        with col2:
            st.text("Real")

            entrada_estufa_real = st.number_input("Entrada Estufa", key="entrada_estufa_real")
            saida_estufa_real = st.number_input("Saída Estufa", key="saida_estufa_real")
            pressao_bicos_deseng_fosf_real = st.number_input("Pressão Bicos Deseng/Fosf", key="pressao_bicos_deseng_fosf_real")
        
        limpeza_umidade_pos_secagem = st.selectbox("Limpeza e Umidade Pós Secagem", ("OK", "ÁGUA", "GRAXA", "ÓLEO", "OUTROS"))

        col1, col2, col3 = st.columns([2, 10, 2])
        with col1:
            voltar = st.form_submit_button("Voltar")
        with col3:
            submitted = st.form_submit_button("Próximo")

        if voltar:
            st.session_state.step = 3
            st.rerun()

        campos_obrigatorios = []

        if submitted:
            if not all(campos_obrigatorios):
                st.error("Por favor, preencha todos os campos.")
            else:
                st.session_state.form_data["entrada_estufa_program"] = entrada_estufa_program
                st.session_state.form_data["saida_estufa_program"] = saida_estufa_program
                st.session_state.form_data["pressao_bicos_deseng_fosf_program"] = pressao_bicos_deseng_fosf_program
                st.session_state.form_data["entrada_estufa_real"] = entrada_estufa_real
                st.session_state.form_data["saida_estufa_real"] = saida_estufa_real
                st.session_state.form_data["pressao_bicos_deseng_fosf_real"] = pressao_bicos_deseng_fosf_real
                st.session_state.form_data["limpeza_umidade_pos_secagem"] = limpeza_umidade_pos_secagem

                st.session_state.step = 5
                st.rerun()

elif st.session_state.step == 5:
    st.header("Etapa 5: Informações Máquina (Pistolas)")

    with st.form("form_etapa_5", enter_to_submit=False):
        vazoes_pistolas = [0] * 24

        pist_col1, pist_col2 = st.columns(2)

        with pist_col1:
            st.text("Espelho")
            vazoes_pistolas[0] = st.number_input("1")
            vazoes_pistolas[1] = st.number_input("2")
            vazoes_pistolas[2] = st.number_input("3")
            vazoes_pistolas[3] = st.number_input("4")
            vazoes_pistolas[4] = st.number_input("5")
            vazoes_pistolas[5] = st.number_input("6")
            vazoes_pistolas[6] = st.number_input("7")
            vazoes_pistolas[7] = st.number_input("8")
            vazoes_pistolas[8] = st.number_input("9")
            vazoes_pistolas[9] = st.number_input("10")
            vazoes_pistolas[20] = st.number_input("21")
            vazoes_pistolas[21] = st.number_input("22")

        with pist_col2:
            st.text("Dobra")
            vazoes_pistolas[10] = st.number_input("11")
            vazoes_pistolas[11] = st.number_input("12")
            vazoes_pistolas[12] = st.number_input("13")
            vazoes_pistolas[13] = st.number_input("14")
            vazoes_pistolas[14] = st.number_input("15")
            vazoes_pistolas[15] = st.number_input("16")
            vazoes_pistolas[16] = st.number_input("17")
            vazoes_pistolas[17] = st.number_input("18")
            vazoes_pistolas[18] = st.number_input("19")
            vazoes_pistolas[19] = st.number_input("20")
            vazoes_pistolas[22] = st.number_input("23")
            vazoes_pistolas[23] = st.number_input("24")

        col1, col2, col3 = st.columns([2, 10, 2])
        with col1:
            voltar = st.form_submit_button("Voltar")
        with col3:
            submitted = st.form_submit_button("Próximo")

        if voltar:
            st.session_state.step = 4
            st.rerun()

        campos_obrigatorios = []

        if submitted:
            if not all(campos_obrigatorios):
                st.error("Por favor, preencha todos os campos.")
            else:
                st.session_state.form_data["vazoes_pistolas"] = vazoes_pistolas

                st.session_state.step = 6
                st.rerun()

elif st.session_state.step == 6:
    st.header("Etapa 5: Informações Máquina (Pistolas)")

    with st.form("form_etapa_5", enter_to_submit=False):
        testes = [[0, 0, 0]] * 3

        st.text("Camadas")

        df = pd.DataFrame(columns=["Esquerda", "Centro", "Direita"], index=["Topo", "Meio", "Baixo"])

        camadas = st.data_editor(df)

        st.text("Barra")
        barra_retoque = st.toggle("Retoque Líquido")
        barra_mistura = st.toggle("Mistura de Itens")
        barra_retrabalho = st.toggle("Retrabalho")

        st.text("Avaliação Inspetor")

        teste_cura = st.toggle("Teste de Cura (MEK)")
        teste_aderencia = st.toggle("Teste de Aderência (grade)")
        teste_visual = st.toggle("Teste Visual da Barra")

        col1, col2, col3 = st.columns([2, 10, 2])
        with col1:
            voltar = st.form_submit_button("Voltar")
        with col3:
            submitted = st.form_submit_button("Próximo")

        if voltar:
            st.session_state.step = 5
            st.rerun()

        campos_obrigatorios = []

        if submitted:
            if not all(campos_obrigatorios):
                st.error("Por favor, preencha todos os campos.")
            else:
                st.session_state.form_data["camadas"] = camadas
                st.session_state.form_data["barra_retoque"] = barra_retoque
                st.session_state.form_data["barra_mistura"] = barra_mistura
                st.session_state.form_data["barra_retrabalho"] = barra_retrabalho
                st.session_state.form_data["teste_cura"] = teste_cura
                st.session_state.form_data["teste_aderencia"] = teste_aderencia
                st.session_state.form_data["teste_visual"] = teste_visual

                st.session_state.step = 7
                st.rerun()