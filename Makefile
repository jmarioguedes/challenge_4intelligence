.PHONY: install

install:
	# Instalando as diversas ferramenta de checagem e formatação
	@pip install isort blue prospector pip-audit --upgrade

	# Instalando a suíte de Testes Unitários
	@pip install pytest~=7.0 pytest-cov~=3.0 pytest-asyncio~=0.18 --upgrade

	# Instala as demais biblitecas necessárias para a execução dos testes unitários
	@pip install -r requirements.dev --upgrade

tests:
	@pytest --cov=./source --cov-report html -p no:warnings