
    CREATE TABLE IF NOT EXISTS tb_instituicao_ensino (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        no_entidade TEXT NOT NULL,
        co_entidade INTEGER NOT NULL UNIQUE,

        no_uf TEXT NOT NULL,
        sg_uf TEXT NOT NULL,
        co_uf INTEGER NOT NULL,

        no_municipio TEXT NOT NULL,
        co_municipio INTEGER NOT NULL,

        no_mesorregiao TEXT,
        co_mesorregiao INTEGER,

        no_microrregiao TEXT,
        co_microrregiao INTEGER,

        nu_ano_censo INTEGER NOT NULL,

        no_regiao TEXT,
        co_regiao INTEGER,

        qt_mat_bas INTEGER DEFAULT 0,
        qt_mat_inf INTEGER DEFAULT 0,
        qt_mat_fund INTEGER DEFAULT 0,
        qt_mat_med INTEGER DEFAULT 0,
        qt_mat_prof INTEGER DEFAULT 0,
        qt_mat_eja INTEGER DEFAULT 0,
        qt_mat_esp INTEGER DEFAULT 0
    );

    CREATE TABLE IF NOT EXISTS tb_usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(150) NOT NULL,
        email VARCHAR(150) NOT NULL UNIQUE,
        cpf VARCHAR(11) NOT NULL UNIQUE,
        nascimento DATE NOT NULL
    );
