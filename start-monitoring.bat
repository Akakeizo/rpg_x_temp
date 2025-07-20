@echo off
echo 🚀 Iniciando ambiente de monitoramento MESTRE...
echo.

REM Verificar se Docker está instalado
docker --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker não está instalado. Por favor, instale o Docker primeiro.
    pause
    exit /b 1
)

REM Verificar se Docker Compose está instalado
docker-compose --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker Compose não está instalado. Por favor, instale o Docker Compose primeiro.
    pause
    exit /b 1
)

echo 📊 Iniciando serviços de monitoramento...
docker-compose -f docker-compose.monitoring.yml up -d

echo.
echo ✅ Serviços iniciados com sucesso!
echo.
echo 🌐 Acesse os serviços:
echo   • Dashboard MESTRE: http://localhost:8000/api/metrics/dashboard
echo   • Grafana: http://localhost:3000 (admin/admin)
echo   • Prometheus: http://localhost:9090
echo   • Jaeger: http://localhost:16686
echo   • Frontend: http://localhost:5173
echo.
echo 📡 WebSocket: ws://localhost:8000/ws/metrics
echo.
echo 🛑 Para parar os serviços, execute: docker-compose -f docker-compose.monitoring.yml down
pause
