-- Active: 1782324623621@@mysql-luxevoyage-projetoluxevoyage.a.aivencloud.com@18410@LuxeVoyage
INSERT INTO Estado (sigla, nome, regiao_nome, timezone) VALUES
('SP', 'São Paulo', 'Sudeste', 'America/Sao_Paulo'),
('RJ', 'Rio de Janeiro', 'Sudeste', 'America/Sao_Paulo'),
('SC', 'Santa Catarina', 'Sul', 'America/Sao_Paulo'),
('BA', 'Bahia', 'Nordeste', 'America/Bahia'),
('CE', 'Ceará', 'Nordeste', 'America/Fortaleza');

INSERT INTO Municipio (id_estado, nome, categoria) VALUES
(1, 'São Paulo', 'Capital'),
(1, 'Campinas', 'Interior'),
(2, 'Rio de Janeiro', 'Capital'),
(2, 'Búzios', 'Litoral'),
(3, 'Florianópolis', 'Capital'),
(3, 'Balneário Camboriú', 'Litoral'),
(4, 'Salvador', 'Capital'),
(4, 'Porto Seguro', 'Litoral'),
(5, 'Fortaleza', 'Capital'),
(5, 'Jericoacoara', 'Litoral');

INSERT INTO Parceiros (razao_social, tipo_parceiro, status) VALUES
('Hotelaria Brasil SA', 'Hotel', 'Ativo'),
('Pousada do Sol Nascente LTDA', 'Pousada', 'Ativo'),
('Voe Bem Linhas Aéreas', 'Companhia Aérea', 'Ativo'),
('Transportadora Caminhos', 'Transfer', 'Ativo'),
('Guia Turístico Regional SC', 'Guia', 'Ativo'),
('Aventuras Radicais Nordeste', 'Passeios', 'Ativo'),
('Restaurante Sabor do Mar', 'Alimentação', 'Inativo'),
('Resort de Luxo SP', 'Resort', 'Ativo'),
('Aluguel de Carros Express', 'Locadora', 'Ativo'),
('Seguros Viagem Protegida', 'Seguradora', 'Ativo');

INSERT INTO Cobertura_Parceiros (id_parceiro, id_municipio, status) VALUES
(1, 1, 'Ativo'), (1, 3, 'Ativo'), (2, 4, 'Ativo'), (2, 6, 'Ativo'),
(3, 1, 'Ativo'), (3, 3, 'Ativo'), (3, 5, 'Ativo'), (3, 7, 'Ativo'),
(4, 5, 'Ativo'), (5, 6, 'Ativo'), (6, 8, 'Ativo'), (6, 10, 'Ativo'),
(8, 2, 'Ativo'), (9, 1, 'Ativo'), (10, 1, 'Ativo');

INSERT INTO Servicos_Parceiros (id_parceiro, categoria_servico, nome_servico) VALUES
(1, 'Hospedagem', 'Quarto Standard - Casal'),
(1, 'Hospedagem', 'Quarto Luxo - Frente Mar'),
(2, 'Hospedagem', 'Chalé com Café da Manhã'),
(3, 'Transporte', 'Voo Econômico Ida e Volta'),
(3, 'Transporte', 'Voo Executivo'),
(4, 'Transporte', 'Transfer Aeroporto - Hotel'),
(5, 'Guia', 'City Tour Histórico'),
(6, 'Passeio', 'Mergulho com Cilindro'),
(6, 'Passeio', 'Passeio de Buggy'),
(7, 'Alimentação', 'Jantar Completo 3 Pratos'),
(8, 'Hospedagem', 'Suíte Presidencial All Inclusive'),
(9, 'Locação', 'Aluguel de SUV 7 Diárias'),
(9, 'Locação', 'Aluguel Carro Compacto 3 Diárias'),
(10, 'Seguro', 'Seguro Viagem Nacional Básico'),
(10, 'Seguro', 'Seguro Viagem Premium');

INSERT INTO Usuario_Interno (nome, cargo, email_corporativo, nivel_acesso) VALUES
('Ana Silva', 'Vendedora', 'ana.silva@agencia.com', 'Vendedor'),
('Carlos Moura', 'Gerente Comercial', 'carlos.moura@agencia.com', 'Gerente'),
('Beatriz Souza', 'Analista de Operações', 'beatriz.souza@agencia.com', 'Operacoes'),
('Diego Alves', 'Atendimento', 'diego.alves@agencia.com', 'Suporte'),
('Fernanda Costa', 'Administrador', 'fernanda.costa@agencia.com', 'Admin');