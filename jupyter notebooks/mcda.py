"""Pesos e métodos de agregação do estudo, com os parâmetros do docs/log_decisoes.md.

Todas as funções recebem a matriz de decisão X (municípios nas linhas, os cinco
critérios nas colunas, na ordem de CRITERIOS, notas brutas de 0 a 100).
"""
import numpy as np
import pandas as pd

CRITERIOS = ["IAG0001", "IES0001", "IES2003", "IRS0001", "IRS3002"]
NOMES = ["Água", "Esgoto", "Tratamento", "Coleta", "Destinação"]
ESQUEMAS = ["Pesos iguais", "CRITIC", "AHP Gaussiano", "AHP clássico"]
METODOS = ["Soma ponderada", "TOPSIS", "VIKOR", "PROMETHEE II"]  # ordem de compensação: total, total, parcial, limitada

# Matriz de Saaty preenchida pelo autor (log_decisoes.md, seção 6.3)
SAATY = np.array([
    [1,   3,   4,   2,   5],
    [1/3, 1,   2,   1/2, 3],
    [1/4, 1/2, 1,   1/3, 2],
    [1/2, 2,   3,   1,   4],
    [1/5, 1/3, 1/2, 1/4, 1],
])
IR = {3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32}

# Limiares do PROMETHEE II (log_decisoes.md, seção 4); Destinação usa a função em U
Q = np.array([8.94, 11.06, 7.24, 6.40, 5.0])
P = np.array([32.90, 41.65, 50.10, 31.39, 5.0])
FUNCAO = ["linear", "linear", "linear", "linear", "U"]
V_VIKOR = 0.5


def minmax(X):
    return (X - X.min(0)) / (X.max(0) - X.min(0))


def pesos_saaty(A=SAATY):
    """Pesos pela média geométrica das linhas e razão de consistência."""
    n = len(A)
    gm = np.prod(A, axis=1) ** (1 / n)
    w = gm / gm.sum()
    lam = ((A @ w) / w).mean()
    rc = ((lam - n) / (n - 1)) / IR[n]
    return w, rc


def pesos_gaussianos(X):
    N = X / X.sum(0)
    f = N.std(0) / N.mean(0)  # desvio-padrão populacional
    return f / f.sum()


def pesos_critic(X):
    M = minmax(X)
    c = M.std(0) * (1 - np.corrcoef(M.T)).sum(0)  # Pearson entre os valores min-max
    return c / c.sum()


def pesos(X, A=SAATY):
    return {
        "Pesos iguais": np.full(X.shape[1], 1 / X.shape[1]),
        "CRITIC": pesos_critic(X),
        "AHP Gaussiano": pesos_gaussianos(X),
        "AHP clássico": pesos_saaty(A)[0],
    }


def soma_ponderada(X, w, esquema):
    """Notas brutas com pesos iguais (é o ABES), min-max com CRITIC, pela soma nos dois AHP."""
    if esquema == "Pesos iguais":
        return X.sum(1)
    if esquema == "CRITIC":
        return minmax(X) @ w
    return (X / X.sum(0)) @ w


def topsis(X, w, normalizacao="vetorial"):
    R = X / np.sqrt((X ** 2).sum(0)) if normalizacao == "vetorial" else minmax(X)
    V = R * w
    d_mais = np.sqrt(((V - V.max(0)) ** 2).sum(1))
    d_menos = np.sqrt(((V - V.min(0)) ** 2).sum(1))
    return d_menos / (d_mais + d_menos)


def vikor_q(X, w, v=V_VIKOR):
    """Índice Q (menor é melhor)."""
    d = (X.max(0) - X) / (X.max(0) - X.min(0))
    S = (w * d).sum(1)
    R = (w * d).max(1)
    return v * (S - S.min()) / (S.max() - S.min()) + (1 - v) * (R - R.min()) / (R.max() - R.min())


def fluxos_por_criterio(X, q=Q, p=P, funcao=FUNCAO):
    """Fluxo líquido unicritério φⱼ de cada município."""
    n = len(X)
    F = np.zeros_like(X, dtype=float)
    for j in range(X.shape[1]):
        D = X[:, j][:, None] - X[:, j][None, :]
        if funcao[j] == "U" or q[j] == p[j]:
            Pj = (D > q[j]).astype(float)
        else:
            Pj = np.clip((D - q[j]) / (p[j] - q[j]), 0, 1)
        F[:, j] = (Pj.sum(1) - Pj.sum(0)) / (n - 1)
    return F


def rankings(X, A=SAATY, v=V_VIKOR, normalizacao_topsis="vetorial", F=None):
    """Pontuação dos 16 rankings, todas no sentido 'maior é melhor' (o Q do VIKOR entra com sinal trocado)."""
    W = pesos(X, A)
    F = fluxos_por_criterio(X) if F is None else F
    out = {}
    for m in METODOS:
        for e in ESQUEMAS:
            w = W[e]
            if m == "Soma ponderada":
                s = soma_ponderada(X, w, e)
            elif m == "TOPSIS":
                s = topsis(X, w, normalizacao_topsis)
            elif m == "VIKOR":
                s = -vikor_q(X, w, v)
            else:
                s = F @ w
            out[f"{m} | {e}"] = s
    return pd.DataFrame(out)


def posicoes(pontuacao):
    """Posição 1 = melhor; empates recebem a mesma posição (a menor)."""
    return pontuacao.rank(ascending=False, method="min").astype(int)
