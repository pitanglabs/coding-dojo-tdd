# Coding Dojo de TDD 
O coding dojo é um evento onde os participantes têm a oportunidade de praticar e aperfeiçoar suas habilidades de programação em um ambiente colaborativo e descontraído. Durante o coding dojo, os participantes trabalham em projetos de código juntos, trocando ideias e aprendendo uns com os outros.

Test-Driven Development (TDD) é uma técnica de desenvolvimento de software que envolve escrever testes antes de escrever o código que será testado. O objetivo do TDD é garantir que o código esteja correto e funcione como o esperado antes de ser implementado.

# Livraria Floreios e Borrões
localizada no Beco Diagonal desde 1454, desenvolveu um serviço que permite aos compradores adquirir livros através da entrega de corujas. Para oferecer aos seus clientes uma experiência de compra ainda mais prática, a Floreios e Borrões precisa criar um carrinho de compras. Esta classe permitirá aos usuários **adicionar** livros no carrinho, **remover** livros indesejados, **limpar** o carrinho, adicionar **cupons de desconto** e **calcular o valor total** da compra.

## Livros Disponiveis
| Nome | Preço |
| :----- | :----: |
| Livro Invisível da Invisibilidade | 10 Galleon |
| O Livro Monstruoso dos Monstros | 3 Galleon |
| A Vida e as Mentiras de Alvo Dumbledore | 4.5 Galleon | 
| Viagens com Trasgos | 2 Galleon |
| Hogwarts: Uma História | 2 Galleon |
| Segredos das Artes das Trevas | 5 Galleon |
| Trouxas Sensitivos | 1 Galleon |
| Quadribol Através dos Séculos | 1.5 Galleon |

## Cupons de Desconto
| Código | Desconto (%) |
| :----- | :----: |
| BloodyBaron | 10% |
| MimsyPorpington | 15% |
| FatFriar | 5% |
| HelenaRavenclaw | 20% |

# Testing

```shell
$ python3 -m unittest -v test
```
