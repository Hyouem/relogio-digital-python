"""Testes das funções de formatação do relógio."""

from datetime import datetime
import unittest

from main import (
    DIAS,
    MESES,
    formatar_data,
    formatar_hora,
)


class FormatacaoTestes(unittest.TestCase):

    def test_data_em_portugues(self):
        agora = datetime(2026, 11, 6, 11, 38, 9)

        self.assertEqual(
            formatar_data(agora),
            "sexta-feira, 6 de novembro de 2026",
        )

    def test_ano_bissexto(self):
        agora = datetime(2024, 2, 29)

        self.assertEqual(
            formatar_data(agora),
            "quinta-feira, 29 de fevereiro de 2024",
        )

    def test_hora_com_zero_a_esquerda(self):
        agora = datetime(2026, 11, 6, 7, 5, 3)

        self.assertEqual(
            formatar_hora(agora),
            "07:05:03",
        )

    def test_ultimo_segundo_do_dia(self):
        agora = datetime(2026, 11, 6, 23, 59, 59)

        self.assertEqual(
            formatar_hora(agora),
            "23:59:59",
        )

    def test_quantidade_de_dias_e_meses(self):
        self.assertEqual(len(DIAS), 7)
        self.assertEqual(len(MESES), 12)


if __name__ == "__main__":
    unittest.main()