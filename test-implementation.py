#!/usr/bin/env python3
"""
Script de teste para verificar a implementação das fases 3, 4 e 5
"""

import requests
import json
import time

def test_dashboard():
    """Testa o dashboard de métricas"""
    print("🧪 Testando Dashboard de Métricas...")
    
    try:
        response = requests.get("http://localhost:8000/api/metrics/dashboard")
        if response.status_code == 200:
            data = response.json()
            print("✅ Dashboard API - OK")
            print(f"   Sessões ativas: {data.get('sessions', {}).get('active', 0)}")
            print(f"   Participantes: {data.get('sessions', {}).get('total_participants', 0)}")
        else:
            print(f"❌ Dashboard API - Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro ao testar dashboard: {e}")

def test_prometheus():
    """Testa as métricas do Prometheus"""
    print("\n🧪 Testando Métricas Prometheus...")
    
    try:
        response = requests.get("http://localhost:8000/api/metrics/prometheus")
        if response.status_code == 200:
            content = response.text
            if "mestre_sessoes_ativas" in content:
                print("✅ Métricas MESTRE encontradas")
            else:
                print("⚠️  Métricas MESTRE não encontradas")
        else:
            print(f"❌ Prometheus metrics - Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro ao testar Prometheus: {e}")

def test_alerts():
    """Testa o sistema de alertas"""
    print("\n🧪 Testando Sistema de Alertas...")
    
    try:
        response = requests.get("http://localhost:8000/api/alerts")
        if response.status_code == 200:
            alerts = response.json()
            print(f"✅ Sistema de alertas - OK ({len(alerts)} alertas)")
            for alert in alerts:
                print(f"   ⚠️  {alert['type']}: {alert['message']}")
        else:
            print(f"❌ Alertas - Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro ao testar alertas: {e}")

def test_services():
    """Testa se os serviços estão rodando"""
    print("\n🧪 Verificando serviços...")
    
    services = [
        ("http://localhost:8000/api/metrics/dashboard", "Dashboard API"),
        ("http://localhost:9090", "Prometheus"),
        ("http://localhost:3000", "Grafana"),
        ("http://localhost:16686", "Jaeger"),
    ]
    
    for url, name in services:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code in [200, 302]:
                print(f"✅ {name} - OK")
            else:
                print(f"⚠️  {name} - Status: {response.status_code}")
        except:
            print(f"❌ {name} - Não acessível")

def main():
    """Função principal de teste"""
    print("🚀 Iniciando testes de implementação MESTRE")
    print("=" * 50)
    
    test_dashboard()
    test_prometheus()
    test_alerts()
    test_services()
    
    print("\n" + "=" * 50)
    print("✅ Testes concluídos!")
    print("\n📋 Próximos passos:")
    print("   1. Execute start-monitoring.bat (Windows) ou start-monitoring.sh (Linux/Mac)")
    print("   2. Acesse http://localhost:8000/api/metrics/dashboard")
    print("   3. Configure alertas no Grafana")
    print("   4. Teste o WebSocket com o frontend")

if __name__ == "__main__":
    main()
