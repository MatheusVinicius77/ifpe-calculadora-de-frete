@echo off

REM Verifica se o comando 'uv' está disponível
where uv >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Ativando ambiente uv...
    uv activate
) else (
    echo Comando 'uv' nao encontrado, certifique-se de ativar seu ambiente virtual manualmente.
)

REM Ajustar PYTHONPATH para src
set PYTHONPATH=src

REM Rodar testes com cobertura
pytest --cov=src/calculadora_frete
