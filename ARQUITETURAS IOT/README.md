# 🌐 Curso: Arquitetura de Redes para IoT
**Foco:** Arduino, C++, Python e Integração de Sistemas

---

## 📑 Módulo 1: Fundamentos e Arquitetura de Redes IoT
*   **A Pilha de Protocolos IoT:** Diferenças entre o modelo OSI tradicional e a pilha IoT.
*   **Arquitetura de 3 Camadas:** 
    1.  **Percepção (Hardware):** Sensores e Atuadores.
    2.  **Rede (Conectividade):** Protocolos de transporte (Wi-Fi, Bluetooth, LoRa, Zigbee).
    3.  **Aplicação:** Dashboards, Nuvem e Processamento de Dados.
*   **Edge Computing vs. Cloud Computing:** Onde processar os dados?

---

## 🤖 Módulo 2: O "Core" da Percepção - Arduino e C++
*   **Programação em C++ para Microcontroladores:**
    *   Estrutura `setup()` e `loop()`.
    *   Gestão de memória e tipos de dados otimizados (int, float, char).
    *   Manipulação de GPIOs (Entradas/Saídas Digitais e Analógicas).
*   **Comunicação Serial:**
    *   Protocolo UART para troca de mensagens com o computador.
*   **Projeto Prático 1:** Leitura de sensor de temperatura/umidade e envio via Serial.

---

## 🐍 Módulo 3: O Elo de Ligação - Python no IoT
*   **Por que Python no IoT?** Automação, análise de dados e facilidade de integração.
*   **Bibliotecas Essenciais:** 
    *   `pyserial`: Para ler dados do Arduino via USB.
    *   `paho-mqtt`: Para comunicação com brokers na nuvem.
    *   `requests`: Para integração com APIs REST.
*   **Projeto Prático 2:** Script Python para ler a porta serial e salvar os dados do Arduino em um arquivo `.csv` ou Banco de Dados SQL.

---

## 🛰️ Módulo 4: Protocolos de Comunicação de Dados
*   **MQTT (Message Queuing Telemetry Transport):**
    *   O padrão ouro da IoT.
    *   Conceitos de *Publish/Subscribe*, *Broker* e *Topics*.
*   **HTTP/REST:** Quando usar métodos GET/POST em dispositivos IoT.
*   **JSON:** O formato universal de troca de mensagens.

---

## 🛠️ Projeto Integrador Final: Sistema de Monitoramento Remoto
1.  **Arduino (C++):** Coleta dados e envia para o gateway.
2.  **Gateway (Python):** Recebe os dados, processa e envia para um Broker MQTT ou Dashboard.
3.  **Visualização:** Criação de um alerta visual ou log de eventos.

---

## 📚 Referências e Links Úteis
*   [Documentação Arduino](https://arduino.cc)
*   [Python Serial Port Extension](https://readthedocs.io)
*   [MQTT Essentials - HiveMQ](https://hivemq.com)