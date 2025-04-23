import platform

def versao():
    sistema = platform.system()
    versao = platform.version()
    print(f"O seu sistema é o {sistema} e a versão dele é a {versao}")
versao()