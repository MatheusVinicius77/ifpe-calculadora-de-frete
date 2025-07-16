#!/bin/bash

# Ativar ambiente uv (ajuste o comando se seu ambiente for diferente)
if command -v uv &> /dev/null; then
  echo "Ativando ambiente uv..."
  uv activate
else
  echo "Comando 'uv' não encontrado, certifique-se de ativar seu ambiente virtual manualmente."
fi

# Ajustar PYTHONPATH para src
export PYTHONPATH=src

# Rodar testes com cobertura
pytest --cov=src/calculadora_frete 