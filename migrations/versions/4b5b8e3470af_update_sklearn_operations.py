# -*- coding: utf-8 -*-

"""Adding distinct sklearn operations

Revision ID: 4b5b8e3470af
Revises: 49be2ac6780f
Create Date: 2018-08-26 10:42:09.555626

"""
from alembic import context
from alembic import op
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import table, column,text


# revision identifiers, used by Alembic.
revision = '4b5b8e3470af'
down_revision = '49be2ac6780f'
branch_labels = None
depends_on = None


def _insert_operation():
    tb = table('operation',
                            column("id", Integer),
                            column("slug", String),
                            column('enabled', Integer),
                            column('type', String),
                            column('icon', String),
                            )
    columns = ['id', 'slug', 'enabled', 'type', 'icon']
    data = [
        (4006, 'gbt-regressor',	1, 'TRANSFORMATION','fa-id-card'),
        (4007, 'linear-regression',	1, 'TRANSFORMATION','fa-chart-line'),
        (4008, 'random-forest-regressor', 1, 'TRANSFORMATION','fa-laptop'),
        (4009, 'sgd-regressor',	1, 'TRANSFORMATION','fa-id-card'),
        (4010, 'huber-regressor', 1, 'TRANSFORMATION','fa-laptop'),
        (4011, 'svm-classification', 1, 'TRANSFORMATION', 'fa-tag'),
        (4012, 'naive-bayes-classifier', 1, 'TRANSFORMATION', 'fa-tag'),

    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_new_operation_platform():
    tb = table(
        'operation_platform',
        column('operation_id', Integer),
        column('platform_id', Integer))

    columns = ('operation_id', 'platform_id')
    data = [
        (4006, 4),
        (4007, 4),
        (4008, 4),
        (4009, 4),
        (4010, 4),
        (4011, 4),
        (4012, 4),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)

def _insert_operation_category_operation():
    tb = table(
        'operation_category_operation',
        column('operation_id', Integer),
        column('operation_category_id', Integer))

    columns = ('operation_id', 'operation_category_id')
    data = [
        (4006, 8),
        (4006, 21),
        (4006, 4001),

        (4007, 8),
        (4007, 21),
        (4007, 4001),

        (4008, 8),
        (4008, 21),
        (4008, 4001),

        (4009, 8),
        (4009, 21),
        (4009, 4001),

        (4010, 8),
        (4010, 21),
        (4010, 4001),

        (4011, 8),
        (4011, 18),
        (4011, 4001),

        (4012, 8),
        (4012, 18),
        (4012, 4001),

    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_form():
    operation_form_table = table(
        'operation_form',
        column('id', Integer),
        column('enabled', Integer),
        column('order', Integer),
        column('category', String), )

    columns = ('id', 'enabled', 'order', 'category')
    data = [
        (4006, 1, 1, 'execution'),
        (4007, 1, 1, 'execution'),
        (4008, 1, 1, 'execution'),
        (4009, 1, 1, 'execution'),
        (4010, 1, 1, 'execution'),
        (4011, 1, 1, 'execution'),
        (4012, 1, 1, 'execution'),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(operation_form_table, rows)

def _insert_operation_form_translation():
    tb = table(
        'operation_form_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String))

    columns = ('id', 'locale', 'name')
    data = [
        (4006, 'en', 'Execution'),
        (4006, 'pt', 'Execução'),
        (4007, 'en', 'Execution'),
        (4007, 'pt', 'Execução'),
        (4008, 'en', 'Execution'),
        (4008, 'pt', 'Execução'),
        (4009, 'en', 'Execution'),
        (4009, 'pt', 'Execução'),
        (4010, 'en', 'Execution'),
        (4010, 'pt', 'Execução'),
        (4011, 'en', 'Execution'),
        (4011, 'pt', 'Execução'),
        (4012, 'en', 'Execution'),
        (4012, 'pt', 'Execução'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_operation_form():
    tb = table(
        'operation_operation_form',
        column('operation_id', Integer),
        column('operation_form_id', Integer))

    columns = ('operation_id', 'operation_form_id')
    data = [
        (4006, 41),  # appearance
        (4006, 4006), # own execution form

        (4007, 41),
        (4007, 4007),

        (4008, 41),
        (4008, 4008),

        (4009, 41),
        (4009, 4009),

        (4010, 41),
        (4010, 4010),

        (4011, 41),
        (4011, 4011),

        (4012, 41),
        (4012, 4012),

    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_translation():
    tb = table(
        'operation_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = ('id', 'locale', 'name', 'description')
    data = [

        (4006, 'en', 'Gradient Boosting Regressor', 'Gradient Boosting for regression'),
        (4007, 'en', 'Linear Regression', 'Linear regression with combined L1 and L2 priors as regularizer (ElasticNet).'),
        (4008, 'en', 'Random Forest Regressor', 'A random forest regressor.'),
        (4009, 'en', 'SGD Regressor', 'Linear model fitted by minimizing a regularized empirical loss with Stochastic Gradient Descent.'),
        (4010, 'en', 'Huber Regressor',  'Linear regression model that is robust to outliers.'),
        (4011, 'en', 'SVM Classification',  'Uses a SVM Classifier.'),
        (4012, 'en', 'Naive-Bayes Classifier',  'Uses a Naive-Bayes Classifier.'),

        (4006, 'pt', 'Regressor Gradient Boosting',	'Regressão por Gradient Boosting'),
        (4007, 'pt', 'Regressão Linear', 'Regressão linear com combinações de regularizadores L1 e L2 (ElasticNet).'),
        (4008, 'pt', 'Regressão por Random Forest', 'Um regressor por random forest.'),
        (4009, 'pt', 'Regressor SGD', 'Modelo linear ajustado por minimização com o gradiente descendente estocástico.'),
        (4010, 'pt', 'Regressor Hube ',  'Modelo de regressão linear que é robusto para outliers.'),
        (4011, 'pt', 'Classificador SVM',  'Usa um classificador SVM.'),
        (4012, 'pt', 'Classificador Naive-Bayes',  'Usa um classificador Naive-Bayes.'),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port():
    tb = table(
        'operation_port',
        column('id', Integer),
        column('type', String),
        column('tags', String),
        column('operation_id', Integer),
        column('order', Integer),
        column('multiplicity', String),
        column('slug', String), )

    columns = [c.name for c in tb.columns]
    data = [

    	(4006, 'OUTPUT', None, 4006, 1, 'MANY', 'algorithm'),
        (4007, 'OUTPUT', None, 4007, 1, 'MANY', 'algorithm'),
        (4008, 'OUTPUT', None, 4008, 1, 'MANY', 'algorithm'),
        (4009, 'OUTPUT', None, 4009, 1, 'MANY', 'algorithm'),
        (4010, 'OUTPUT', None, 4010, 1, 'MANY', 'algorithm'),
        (4011, 'OUTPUT', None, 4011, 1, 'MANY', 'algorithm'),
        (4012, 'OUTPUT', None, 4012, 1, 'MANY', 'algorithm'),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_translation():
    tb = table(
        'operation_port_translation',
        column('id', Integer),
        column('locale', String),
        column('name', String),
        column('description', String), )

    columns = ('id', 'locale', 'name', 'description')
    data = [
        (4006, 'en', 'algorithm', 'Untrained regressor model'),
        (4006, 'pt', 'algoritmo', 'Modelo de regressão não treinado'),
        (4007, 'en', 'algorithm', 'Untrained regressor model'),
        (4007, 'pt', 'algoritmo', 'Modelo de regressão não treinado'),
        (4008, 'en', 'algorithm', 'Untrained regressor model'),
        (4008, 'pt', 'algoritmo', 'Modelo de regressão não treinado'),
        (4009, 'en', 'algorithm', 'Untrained regressor model'),
        (4009, 'pt', 'algoritmo', 'Modelo de regressão não treinado'),
        (4010, 'en', 'algorithm', 'Untrained regressor model'),
        (4010, 'pt', 'algoritmo', 'Modelo de regressão não treinado'),
        (4011, 'en', 'algorithm', 'Untrained classification model'),
        (4011, 'pt', 'algoritmo', 'Modelo de classificação não treinado'),
        (4012, 'en', 'algorithm', 'Untrained classification model'),
        (4012, 'pt', 'algoritmo', 'Modelo de classificação não treinado'),
    ]

    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)


def _insert_operation_port_interface_operation_port():
    tb = table(
        'operation_port_interface_operation_port',
        column('operation_port_id', Integer),
        column('operation_port_interface_id', Integer), )

    columns = ('operation_port_id', 'operation_port_interface_id')
    data = [
        (4006, 17),  #IRegressionAlgorithm
        (4007, 17),
        (4008, 17),
        (4009, 17),
        (4010, 17),
        (4011, 5),  #ClassificationAlgorithm
        (4012, 5),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)



def _insert_operation_form_field():
    tb = table(
        'operation_form_field',
        column('id', Integer),
        column('name', String),
        column('type', String),
        column('required', Integer),
        column('order', Integer),
        column('default', Text),
        column('suggested_widget', String),
        column('values_url', String),
        column('values', String),
        column('scope', String),
        column('form_id', Integer), )

    columns = ('id', 'name', 'type', 'required', 'order', 'default',
               'suggested_widget', 'values_url', 'values', 'scope', 'form_id')
    data = [
        # 'gbt-regressor'
        (4027, 'learning_rate', 'FLOAT', 0, 1, 0.1, 'decimal', None, None, 'EXECUTION', 4006),
        (4028, 'n_estimators', 'INTEGER', 0, 2, 100, 'integer', None, None, 'EXECUTION', 4006),
        (4029, 'max_depth', 'INTEGER', 0, 3, 3, 'integer', None, None, 'EXECUTION', 4006),
        (4030, 'min_samples_split', 'INTEGER', 0, 4, 2, 'integer', None, None, 'EXECUTION', 4006),
        (4031, 'min_samples_leaf', 'INTEGER', 0, 5, 1, 'integer', None, None, 'EXECUTION', 4006),
        (4032, 'seed', 'INTEGER', 0, 6, None, 'integer', None, None, 'EXECUTION', 4006),

        # linear-regression
        (4033, 'alpha', 'FLOAT', 	0, 1, 1.0, 'decimal', None, None, 'EXECUTION', 4007),
        (4034, 'l1_ratio', 'FLOAT', 	0, 2, 0.5, 'decimal', None, None, 'EXECUTION', 4007),
        (4035, 'normalize', 'INTEGER', 0, 3,  1, 'checkbox', None, None,'EXECUTION', 4007),
        (4036, 'max_iter', 'INTEGER', 0, 4, 1000, 'integer', None, None, 'EXECUTION', 4007),
        (4037, 'tol', 'FLOAT', 	0, 5, 0.0001, 'decimal', None, None, 'EXECUTION', 4007),
        (4038, 'seed', 'INTEGER', 0, 6, None, 'integer', None, None, 'EXECUTION', 4007),

        # random-forest-regressor
        (4039, 'n_estimators', 'INTEGER', 0, 1, 10, 'integer', None, None, 'EXECUTION', 4008),
        (4040, 'max_features', 'TEXT', 0, 2, 'auto - max=n_features', 'dropdown', None,
		'[{"key": \"auto - max=n_features\", \"value\": \"auto\"}, '
		'{\"key\": \"sqrt - max=sqrt(n_features)\", \"value\": \"sqrt\"}, '
        '{\"key\": \"log2 - max=log2(n_features)\", \"value\": \"log2\"}]', 'EXECUTION', 4008),
        (4041, 'max_depth', 'INTEGER', 0, 3, 3, 'integer', None, None, 'EXECUTION', 4008),
        (4042, 'min_samples_split', 'INTEGER', 0, 4, 2, 'integer', None, None, 'EXECUTION', 4008),
        (4043, 'min_samples_leaf', 'INTEGER', 0, 5, 1, 'integer', None, None, 'EXECUTION', 4008),
        (4044, 'seed', 'INTEGER', 0, 6, None, 'integer', None, None, 'EXECUTION', 4008),

        # sgd-regressor
        (4045, 'alpha', 'FLOAT', 	0, 1, 0.0001, 'decimal', None, None, 'EXECUTION', 4009),
        (4046, 'l1_ratio', 'FLOAT', 	0, 2, 0.15, 'decimal', None, None, 'EXECUTION', 4009),
        (4047, 'max_iter', 'INTEGER', 0, 3, 1000, 'integer', None, None, 'EXECUTION', 4009),
        (4048, 'tol', 'FLOAT', 	0, 4, 0.001, 'decimal', None, None, 'EXECUTION', 4009),
        (4049, 'seed', 'INTEGER', 0, 5, None, 'integer', None, None, 'EXECUTION', 4009),

        # huber-regressor
        (4050, 'epsilon', 'FLOAT', 	0, 1, 1.35, 'decimal', None, None, 'EXECUTION', 4010),
        (4051, 'max_iter', 'INTEGER', 0, 2, 100, 'integer', None, None, 'EXECUTION', 4010),
        (4052, 'alpha', 'FLOAT', 	0, 3, 0.0001, 'decimal', None, None, 'EXECUTION', 4010),
        (4053, 'tol', 'FLOAT', 	0, 4, 0.00001, 'decimal', None, None, 'EXECUTION', 4010),

        #geo-within
        (3113, 'attributes', 'TEXT',   0, 4, None, 'attribute-selector', None, None, 'EXECUTION', 3031),

        #svm-classification
        (4054, 'c', 'FLOAT', 	0, 1, 1.0, 'decimal', None, None, 'EXECUTION', 4011),
        (4055, 'kernel', 'TEXT', 0, 2, 'rbf', 'dropdown', None,
		'[{"key": \"rbf\", \"value\": \"rbf\"}, '
		'{\"key\": \"linear\", \"value\": \"linear\"}, '
        '{\"key\": \"poly\", \"value\": \"poly\"}, '
        '{\"key\": \"sigmoid\", \"value\": \"sigmoid\"}]', 'EXECUTION', 4011),
        (4056, 'degree', 'INTEGER', 0, 3, 3, 'integer', None, None, 'EXECUTION', 4011),
        (4057, 'tol', 'FLOAT', 	0, 4, 0.001, 'decimal', None, None, 'EXECUTION', 4011),
        (4058, 'max_iter', 'INTEGER', 0, 5, 1000, 'integer', None, None, 'EXECUTION', 4011),
        (4059, 'seed', 'INTEGER', 0, 6, None, 'integer', None, None, 'EXECUTION', 4011),

        #naive-Bayes
        (4060, 'type', 'TEXT', 0, 1, 'Multinomial', 'dropdown', None,
		'[{"key": \"Bernoulli\", \"value\": \"Bernoulli\"}, '
		'{\"key\": \"Multinomial\", \"value\": \"Multinomial\"}, '
        '{\"key\": \"Gaussian\", \"value\": \"Gaussian\"}]', 'EXECUTION', 4012),
        (4061, 'alpha', 'FLOAT', 	0, 2, 1.0, 'decimal', None, None, 'EXECUTION', 4012),
        (4062, 'class_prior', 'TEXT',   0, 3, None, 'attribute-selector', None, None, 'EXECUTION', 4012),

        (4063, 'seed', 'INTEGER', 0, 6, None, 'integer', None, None, 'EXECUTION', 4003),
    ]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)



def _insert_operation_form_field_translation():
    tb = table(
        'operation_form_field_translation',
        column('id', Integer),
        column('locale', String),
        column('label', String),
        column('help', String), )

    columns = ('id', 'locale', 'label', 'help')
    data = [
        # gbt-regressor'
        (4027, 'en', 'Learning rate', 'Learning rate shrinks the contribution of each tree by learning_rate. There is a trade-off between learning rate and number of estimators.'),
        (4028, 'en', 'Number of estimators', 'The number of boosting stages to perform. Gradient boosting is fairly robust to over-fitting so a large number usually results in better performance.'),
        (4029, 'en', 'Maximum depth', 'Maximum depth of the individual regression estimators. The maximum depth limits the number of nodes in the tree. Tune this parameter for best performance; the best value depends on the interaction of the input variables.'),
        (4030, 'en', 'Minimun samples split', 'The minimum number of samples required to split an internal node.'),
        (4031, 'en', 'Minimum samples leaf', 'The minimum number of samples required to be at a leaf node.'),
        (4032, 'en', 'Seed', 'The seed of the pseudo random number generator to use when shuffling the data.'),
        (4027, 'pt', 'Taxa de aprendizado', 'A taxa de aprendizado reduz a contribuição de cada árvore. Existe um trade-off entre taxa de aprendizado e número de árvores.'),
        (4028, 'pt', 'Número de árvores','Número de árvores na floresta.'),
        (4029, 'pt', 'Profundidade máxima','Profundidade máxima na árvore.'),
        (4030, 'pt', 'Nó interno mínimo', 'Porcentagem do número mínimo de amostras necessárias para dividir um nó interno.'),
        (4031, 'pt', 'Nó de folha mínima', 'Porcentagem do número mínimo de amostras necessárias para estar em um nó folha.'),
        (4032, 'pt', 'Semente', 'A semente do gerador de números pseudo-aleatórios a ser usada ao embaralhar os dados.'),

        # linear-regression
        (4033, 'en', 'Alpha', 'Constant that multiplies the penalty terms.'),
        (4034, 'en', 'L1 ratio', 'The ElasticNet mixing parameter, with 0 <= l1_ratio <= 1. For l1_ratio = 0 the penalty is an L2 penalty. For l1_ratio = 1 it is an L1 penalty. For 0 < l1_ratio < 1, the penalty is a combination of L1 and L2.'),
        (4035, 'en', 'Normalize', 'If True, the regressors will be normalized before regression.'),
        (4036, 'en', 'Maximum number of iterations', 'The maximum number of iterations.'),
        (4037, 'en', 'Tolerance', 'The tolerance for the optimization: if the updates are smaller than tol, the optimization code checks the dual gap for optimality and continues until it is smaller than tol.'),
        (4038, 'en', 'Seed', 'The seed of the pseudo random number generator to use when shuffling the data.'),
        (4033, 'pt', 'Alpha', 'Constante que multiplica o termo de regularização.'),
        (4034, 'pt', 'L1 ratio', 'O parâmetro de mistura Elastic Net, com 0<=l1_ratio<=1. l1_ratio=0 corresponde a penalidade L2, l1_ratio=1 a L1.'),
        (4035, 'pt', 'Normalizar', 'Se os regressores serão normalizados antes da regressão.'),
        (4036, 'pt', 'Número máximo de iterações', 'Número máximo de iterações.'),
        (4037, 'pt', 'Tolerancia','Tolerância para critérios de parada.'),
        (4038, 'pt', 'Semente', 'A semente do gerador de números pseudo-aleatórios a ser usada ao embaralhar os dados.'),

        # random-forest-regressor
        (4039, 'en', 'Number of estimators', 'The number of trees in the forest.'),
        (4040, 'en', 'Maximum number of features', 'The number of features to consider when looking for the best split.'),
        (4041, 'en', 'Maximum depth', 'Maximum depth of the individual regression estimators. The maximum depth limits the number of nodes in the tree. Tune this parameter for best performance; the best value depends on the interaction of the input variables.'),
        (4042, 'en', 'Minimun samples split', 'The minimum number of samples required to split an internal node.'),
        (4043, 'en', 'Minimum samples leaf', 'The minimum number of samples required to be at a leaf node.'),
        (4044, 'en', 'Seed', 'The seed of the pseudo random number generator to use when shuffling the data.'),
        (4039, 'pt', 'Número de árvores','Número de árvores na floresta.'),
        (4040, 'pt', 'Número máximo de atributos','Número de atributos a serem considerados ao procurar a melhor divisão.'),
        (4041, 'pt', 'Profundidade máxima','Profundidade máxima na árvore.'),
        (4042, 'pt', 'Nó interno mínimo', 'Porcentagem do número mínimo de amostras necessárias para dividir um nó interno.'),
        (4043, 'pt', 'Nó de folha mínima', 'Porcentagem do número mínimo de amostras necessárias para estar em um nó folha.'),
        (4044, 'pt', 'Semente', 'A semente do gerador de números pseudo-aleatórios a ser usada ao embaralhar os dados.'),

        # sgd-regressor
        (4045, 'en', 'Alpha', 'Constant that multiplies the regularization term.'),
        (4046, 'en', 'L1 ratio', 'The Elastic Net mixing parameter, with 0 <= l1_ratio <= 1. l1_ratio=0 corresponds to L2 penalty, l1_ratio=1 to L1.'),
        (4047, 'en', 'Maximum number of iterations', 'Maximum number of iterations.'),
        (4048, 'en', 'Tolerance', 'Tolerance for stopping criteria.'),
        (4049, 'en', 'Seed', 'The seed of the pseudo random number generator to use when shuffling the data.'),
        (4045, 'pt', 'Alpha', 'Constante que multiplica o termo de regularização.'),
        (4046, 'pt', 'Taxa L1', 'O parâmetro de mistura Elastic Net, com 0<=l1_ratio<=1. l1_ratio=0 corresponde a penalidade L2, l1_ratio=1 a L1.'),
        (4047, 'pt', 'Número máximo de iterações', 'Número máximo de iterações.'),
        (4048, 'pt', 'Tolerancia','Tolerância para critérios de parada.'),
        (4049, 'pt', 'Semente', 'A semente do gerador de números pseudo-aleatórios a ser usada ao embaralhar os dados.'),

        # huber-regressor
        (4050, 'en', 'Epsilon', 'The parameter epsilon controls the number of samples that should be classified as outliers. The smaller the epsilon, the more robust it is to outliers.'),
        (4051, 'en', 'Maximum number of iterations', 'Maximum number of iterations.'),
        (4052, 'en', 'Alpha', 'Regularization parameter.'),
        (4053, 'en', 'Tolerance', 'Tolerance for stopping criteria.'),
        (4050, 'pt', 'Epsilon', 'O parâmetro epsilon controla o número de amostras que devem ser classificadas como outliers. Quanto menor o epsilon, mais robusto é para outliers.'),
        (4051, 'pt', 'Número máximo de iterações', 'Número máximo de iterações.'),
        (4052, 'pt', 'Alpha', 'Parâmetro de Regularização.'),
        (4053, 'pt', 'Tolerancia','Tolerância para critérios de parada.'),

        #geo-within
        (3113, 'en', 'Attributes', 'List of selected shapefile attributes (without polygon field).'),
		(3113, 'pt', 'Atributos', 'Lista dos atributos para selecionar do shapefile.'),

        #svm-classification
        (4054, 'en', 'C', 'Penalty parameter C of the error term.'),
        (4055, 'en', 'Kernel', 'Specifies the kernel type to be used in the algorithm.'),
        (4056, 'en', 'Degree', 'Degree of the polynomial kernel function. Ignored by all other kernels.'),
        (4057, 'en', 'Tolerance', 'Tolerance for stopping criterion.'),
        (4058, 'en', 'Maximum number of iterations', 'Maximum number of iterations.'),
        (4059, 'en', 'Seed', 'The seed of the pseudo random number generator to use when shuffling the data.'),
        (4054, 'pt', 'C', 'Parâmetro de penalidade C do termo de erro.'),
        (4055, 'pt', 'Kernel', 'Especifica o tipo de kernel a ser usado no algoritmo.'),
        (4056, 'pt', 'Grau do Polinômio', 'Grau da função do kernel polinomial. Ignorado por todos os outros kernels.'),
        (4057, 'pt', 'Tolerancia', 'Tolerância para critérios de parada.'),
        (4058, 'pt', 'Número máximo de iterações', 'Número máximo de iterações.'),
        (4059, 'pt', 'Semente', 'A semente do gerador de números pseudo-aleatórios a ser usada ao embaralhar os dados.'),

        #naive-Bayes
        (4060, 'en', 'Model type', 'The Gaussian assumes that the likelihood of the features is Gaussian; '
            'The multinomial is suitable for discrete features; Bernoulli is designed for binary/boolean features (non binary features will be converted).'),
        (4061, 'en', 'Smoothing', 'Additive (Laplace/Lidstone) smoothing parameter (0 for no smoothing). Only for Multinomial and Bernoulli types.'),
        (4062, 'en', 'Classes probabilities', 'Prior probabilities of the classes. If specified the priors are not adjusted according to the data.'),
        (4060, 'pt', 'Tipo de modelo', 'O Gaussiano assume que a probabilidade das características é Gaussiana; '
            'O multinomial é adequado para características discretas; Bernoulli é projetado para campos binários/booleanos (campos não binários serão convertidos).'),
        (4061, 'pt', 'Suavização', 'Parâmetro de suavização Aditivo (Laplace / Lidstone) (0 para não suavização). Apenas para os tipos Multinomial e Bernoulli.'),
        (4062, 'pt', 'Peso das classes', 'Peso probabilistico das classes. Se especificado, os pesos não são ajustados de acordo com os dados.'),

	]
    rows = [dict(zip(columns, row)) for row in data]
    op.bulk_insert(tb, rows)



all_commands = [

	(_insert_operation, 'DELETE FROM operation WHERE id >= 4006'),
	(_insert_new_operation_platform, 'DELETE FROM operation_platform WHERE operation_id >= 4006' ),
	(_insert_operation_category_operation, 'DELETE FROM operation_category_operation WHERE operation_id >= 4006'),
	(_insert_operation_form, 'DELETE FROM operation_form WHERE id >= 4006'),
	(_insert_operation_form_translation, 'DELETE FROM operation_form_translation WHERE id >= 4006'),
	(_insert_operation_operation_form, 'DELETE FROM operation_operation_form WHERE operation_id >= 4006'),
	(_insert_operation_translation, 'DELETE FROM operation_translation WHERE id >= 4006'),
	(_insert_operation_port, 'DELETE FROM operation_port WHERE id >= 4006' ),
	(_insert_operation_port_translation, 'DELETE FROM operation_port_translation WHERE id >= 4006' ),
	(_insert_operation_port_interface_operation_port, 'DELETE FROM operation_port_interface_operation_port WHERE operation_port_id >= 4006'),
	(_insert_operation_form_field,
     'DELETE FROM operation_form_field WHERE id >= 4027;'
     'DELETE FROM operation_form_field WHERE id = 3113'),
	(_insert_operation_form_field_translation,
    'DELETE FROM operation_form_field_translation WHERE id >= 4027;'
    'DELETE FROM operation_form_field_translation WHERE id = 3113' ),
    ("""
    UPDATE operation_platform SET operation_id=3030 WHERE operation_id=16 AND platform_id=4;
    """,
    """
    UPDATE operation_platform SET operation_id=16 WHERE operation_id=3030 AND platform_id=4;
    """),
    ("""
    DELETE FROM operation_platform WHERE platform_id=4 AND operation_id=78;
    DELETE FROM operation_platform WHERE platform_id=4 AND operation_id=8;
    DELETE FROM operation_platform WHERE platform_id=4 AND operation_id=9;
    DELETE FROM operation_platform WHERE platform_id=4 AND operation_id=4;
    DELETE FROM operation_platform WHERE platform_id=4 AND operation_id=3008;
    """,
    """
    INSERT INTO operation_platform (operation_id, platform_id) VALUES (78, 4), (8, 4), (9, 4), (4, 4);
    """),
    ("""
        UPDATE operation_form_field
        SET type='INTEGER', suggested_widget='integer'
        WHERE id=4008 or id=4009 or id=4014 or id=4015 or id=4017 or id=4018;
    ""","""
        UPDATE operation_form_field
        SET type='FLOAT', suggested_widget='decimal'
        WHERE id=4008 or id=4009 or id=4014 or id=4015 or id=4017 or id=4018;
    """),
    ("""
        UPDATE operation_form_field
        SET `default`=2
        WHERE id=4008 or id=4014 or id=4017;
        UPDATE operation_form_field
        SET `default`=1
        WHERE id=4009 or id=4015 or id=4018;
    ""","""
        UPDATE operation_form_field
        SET `default`=NULL
        WHERE id=4008 or id=4014 or id=4017;
        UPDATE operation_form_field
        SET `default`=NULL
        WHERE id=4009 or id=4015 or id=4018;
    """),
    ("""
        UPDATE operation_form_field_translation
        SET label='C', help='Inverse of regularization strength. Like in support vector machines, smaller values specify stronger regularization.'
        WHERE id=4002 AND locale='en';
        UPDATE operation_form_field_translation
        SET label='C', help='Força de regularização inversa. Como no SVM, valores menores especificam uma regularização mais forte.'
        WHERE id=4002 AND locale='pt';
    """,
    """
        UPDATE operation_form_field_translation
        SET label='Inverse of regularization strength', help='Like in support vector machines, smaller values specify stronger regularization.'
        WHERE id=4002 AND locale='en';
        UPDATE operation_form_field_translation
        SET label='força de regularização inversa', help='Como nas máquinas de vetores de suporte, valores menores especificam uma regularização mais forte.'
        WHERE id=4002 AND locale='pt';
    """),
    ("""
        UPDATE operation_form_field_translation SET help='The Laplace smoothing parameter (0 for no smoothing).' WHERE id=136 AND locale='en';
        UPDATE operation_form_field_translation SET help='Parâmetro de suavização Laplace (0 para não suavização).' WHERE id=136 AND locale='pt';
        UPDATE operation_form_field_translation SET help='Thresholds in multi-class classification to adjust the probability of predicting each class. Array must have length equal to the number of classes.' WHERE id=377 AND locale='en';
        UPDATE operation_form_field_translation SET help='Limiar na classificação de várias classes para ajustar a probabilidade de prever cada classe. A lista deve ter comprimento igual ao número de classes.' WHERE id=377 AND locale='pt';
    """,
    """
        UPDATE operation_form_field_translation SET help='Smoothing.' WHERE id=136 AND locale='en';
        UPDATE operation_form_field_translation SET help='Smoothing.' WHERE id=136 AND locale='pt';
        UPDATE operation_form_field_translation SET help='Thresholds' WHERE id=377 AND locale='en';
        UPDATE operation_form_field_translation SET help='Thresholds' WHERE id=377 AND locale='pt';
    """)



	]

def upgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in all_commands:
            if isinstance(cmd[0], (unicode, str)):
                connection.execute(cmd[0])
            elif isinstance(cmd[0], list):
                for row in cmd[0]:
                    connection.execute(row)
            else:
                cmd[0]()
    except:
        session.rollback()
        raise
    session.commit()



def downgrade():
    ctx = context.get_context()
    session = sessionmaker(bind=ctx.bind)()
    connection = session.connection()

    try:
        for cmd in reversed(all_commands):
            if isinstance(cmd[1], (unicode, str)):
                connection.execute(cmd[1])
            elif isinstance(cmd[1], list):
                for row in cmd[1]:
                    connection.execute(row)
            else:
                cmd[1]()
    except:
        session.rollback()
        raise
    session.commit()
