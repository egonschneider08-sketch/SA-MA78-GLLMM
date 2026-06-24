-- Active: 1782324666582@@mysql-luxevoyage-projetoluxevoyage.a.aivencloud.com@18410@LuxeVoyage
-- 7. Avaliacoes_Parceiros (10 registros)
INSERT INTO Avaliacoes_Parceiros (id_parceiro, id_usuario_interno, nota, comentarios) VALUES
(1, 3, 4, 'Hotel muito bom, mas atrasou o check-in.'),
(2, 1, 5, 'Pousada fantástica, clientes sempre elogiam.'),
(3, 3, 3, 'Muitos cancelamentos de voos recentes.'),
(4, 4, 5, 'Motorista pontual e cordial.'),
(5, 1, 4, 'Guia conhece muito a região.'),
(6, 1, 5, 'Passeio de buggy incrível!'),
(8, 2, 5, 'Resort padrão internacional.'),
(9, 3, 4, 'Carros novos, mas fila no balcão.'),
(10, 4, 5, 'Acionamento do seguro foi rápido e eficiente.'),
(1, 2, 4, 'Bom custo-benefício na baixa temporada.');


-- 8. Destaques_Sazonais (5 registros)
INSERT INTO Destaques_Sazonais (id_municipio, data_inicio, data_fim, classificacao) VALUES
(8, '2026-02-10', '2026-02-20', 'Carnaval'),
(4, '2026-12-26', '2026-12-31', 'Réveillon'),
(6, '2026-12-15', '2027-02-28', 'Verão Alta Temporada'),
(2, '2026-06-01', '2026-07-31', 'Festival de Inverno'),
(10, '2026-07-01', '2026-08-31', 'Temporada de Ventos (Kitesurf)');


-- 9. Pacote (5 registros)
INSERT INTO Pacote (nome_pacote, id_municipio_destino, status) VALUES
('Escapada Romântica Búzios', 4, 'Ativo'),
('Férias em Família no Nordeste', 8, 'Ativo'),
('Aventura Jeri', 10, 'Ativo'),
('Executivo SP Rápido', 1, 'Ativo'),
('Belezas do Sul - Floripa e Balneário', 5, 'Rascunho');


-- 10. Temporada (4 registros)
INSERT INTO Temporada (nome, data_inicio, data_fim) VALUES
('Baixa Temporada 2026', '2026-03-01', '2026-06-30'),
('Alta Temporada Férias', '2026-07-01', '2026-07-31'),
('Primavera 2026', '2026-08-01', '2026-11-30'),
('Verão 2026/2027', '2026-12-01', '2027-02-28');


-- 11. Modulos_Pacote (15 registros)
INSERT INTO Modulos_Pacote (id_pacote, id_servico_parceiro, obrigatorio) VALUES
(1, 3, TRUE), (1, 6, TRUE), (1, 2, TRUE), (1, 14, FALSE),
(2, 3, TRUE), (2, 6, TRUE), (2, 11, TRUE), (2, 12, FALSE),
(3, 4, TRUE), (3, 3, TRUE), (3, 8, TRUE), (3, 9, FALSE),
(4, 5, TRUE), (4, 1, TRUE),
(5, 13, TRUE);
