import json
from openpyxl import Workbook
from tkinter import Tk, filedialog, messagebox
import os

# ==============================
# CONFIGURAÇÃO (EDITÁVEL)
# ==============================
MAP = {
    "nome": "username",
    "usuario": "user",
    "admin": "admin",
    "tecnico": "technical"
}

# ==============================
# FUNÇÕES
# ==============================

def selecionar_arquivo():
    Tk().withdraw()
    arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo JSON",
        filetypes=[("Arquivos JSON", "*.json")]
    )
    return arquivo


def extrair_lista(data):
    if isinstance(data, list):
        return data
    elif isinstance(data, dict) and "content" in data:
        return data["content"]
    else:
        raise Exception("Formato de JSON não reconhecido")


def processar_json(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        data = json.load(f)
    return extrair_lista(data)


def gerar_excel(lista, caminho_saida):
    wb = Workbook()
    ws = wb.active
    ws.title = "Usuarios"

    # Cabeçalho
    ws.append(["Nome", "Usuario", "Tipo Acesso", "Admin", "Tecnico"])

    for user in lista:
        nome = user.get(MAP["nome"], "")
        usuario = "@" + str(user.get(MAP["usuario"], ""))

        admin_bool = user.get(MAP["admin"], False)
        tecnico_bool = user.get(MAP["tecnico"], False)

        admin = "Sim" if admin_bool else "Não"
        tecnico = "Sim" if tecnico_bool else "Não"

        if admin_bool and tecnico_bool:
            tipo = "Administrador / Técnico"
        elif admin_bool:
            tipo = "Administrador"
        elif tecnico_bool:
            tipo = "Técnico"
        else:
            tipo = ""

        ws.append([nome, usuario, tipo, admin, tecnico])

    wb.save(caminho_saida)


# ==============================
# EXECUÇÃO
# ==============================

def main():
    try:
        arquivo = selecionar_arquivo()

        if not arquivo:
            messagebox.showwarning("Aviso", "Nenhum arquivo selecionado.")
            return

        lista = processar_json(arquivo)

        pasta = os.path.dirname(arquivo)
        saida = os.path.join(pasta, "usuarios.xlsx")

        gerar_excel(lista, saida)

        messagebox.showinfo("Sucesso", f"Planilha gerada em:\n{saida}")

    except Exception as e:
        messagebox.showerror("Erro", str(e))


if __name__ == "__main__":
    main()