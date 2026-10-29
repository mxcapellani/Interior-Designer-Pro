# Interior Designer Pro
Skill de análise arquitetônica, redesign de interiores e prompts fotorrealistas com prioridade absoluta à câmera da referência.

## Entrega e capacidades
Duas saídas: **prompt técnico completo em português** e **JSON estruturado em inglês**, com dez campos e restrições de arquitetura, perspectiva e câmera. JSON é organização de prompt destinada a fluxos como Nano Banana, não esquema oficial de API.
Análise de interiores e exteriores; móveis, decoração, estilos, materiais, revestimentos, iluminação, home staging, pessoas e pets apenas quando solicitados. Sem referência, não inventa câmera verificada. A preservação é instruída; o editor utilizado determina o resultado real.

## Instalação e uso
Copiar [.agents/skills/interior-designer-pro](.agents/skills/interior-designer-pro/SKILL.md) para a mesma estrutura do projeto alvo. O host precisa reconhecer Skills ou carregar explicitamente SKILL.md. Não instala automaticamente integrações.
Exemplo: “Nesta fotografia, aplique estilo Japandi e piso de madeira, mantendo arquitetura e câmera. Não adicione pessoas ou pets.” Outro: “Mantenha tudo e altere somente a luz para quente.” Ambas as saídas devem ser completas.
Modelo de linguagem é suficiente para prompts por descrição; visão é necessária para analisar imagem; editor externo é necessário para renderizar. Nenhum token obrigatório ou permissão de publicação/geração automática. Python é necessário apenas para validação opcional.

## Recursos novos e limites
Iteração contextual, distinção observado/proposto, tratamento de ausência de referência, flags de sujeitos existentes e comparação visual condicional. Máscaras são descrições até execução real; não há CAD, medição ou garantia de geometria. 4K+ é objetivo, não promessa. Não substitui projeto executivo.
[Auditoria](docs/AUDIT.md), [especificação original integral](docs/SOURCE_SPECIFICATION.md), [instalação e atualização](docs/INSTALLATION.md).

## Testes
```bash
python -m pip install -r tests/requirements.txt
python tests/validate_skill.py
python -m unittest discover -s tests -p 'test_*.py'
python .agents/skills/interior-designer-pro/scripts/validate_output.py examples/japandi-reference.json
```
[Testes de aceitação](tests/acceptance-tests.md) e [matriz](tests/comparison-matrix.md) não equivalem a testes executados. Veja [resultados](tests/RESULTS.md). GitHub Actions configurado para validação estrutural. O validador JSON não mede geometria nem verifica a língua dos textos.

MIT para o pacote original produzido; a especificação fornecida foi preservada para rastreabilidade, sem alegação de acesso a configurações privadas. Consultar [CHANGELOG](CHANGELOG.md).
