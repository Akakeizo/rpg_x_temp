#!/bin/bash

echo "🚀 Iniciando ambiente de monitoramento MESTRE..."
echo ""

# Verificar se Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker não está instalado. Por favor, instale o Docker primeiro."
    exit 1
fi

# Verificar se Docker Compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose não está instalado. Por favor, instale o Docker Compose primeiro."
    exit 1
fi

echo "📊 Iniciando serviços de monitoramento..."
docker-compose -f docker-compose.monitoring.yml up -d

echo ""
echo "✅ Serviços iniciados com sucesso!"
echo ""
echo "🌐 Acesse os serviços:"
echo "  • Dashboard MESTRE: http://localhost:8000/api/metrics/dashboard"
echo "  • Grafana: http://localhost:3000 (admin/admin)"
echo "  • Prometheus: http://localhost:9090"
echo "  • Jaeger: http://localhost:16686"
echo "  • Frontend: http://localhost:5173"
echo ""
echo "📡 WebSocket: ws://localhost:8000/ws/metrics"
echo ""
echo "🛑 Para parar os serviços, execute: docker-compose -f docker-compose.monitoring.yml down"
