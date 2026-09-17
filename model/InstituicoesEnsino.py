
class InstituicoesEnsino():

    def __init__(self, id, no_entidade, co_entidade, no_uf, sg_uf, co_uf, no_municipio, co_municipio, no_mesorregiao, co_mesorregiao, no_microrregiao, co_microrregiao, nu_ano_censo, no_regiao, co_regiao, qt_mat_bas, qt_mat_inf, qt_mat_fund, qt_mat_med, qt_mat_prof, qt_mat_eja, qt_mat_esp):
        self.id = id
        self.no_entidade = no_entidade
        self.co_entidade = co_entidade
        self.no_uf = no_uf
        self.sg_uf = sg_uf
        self.co_uf = co_uf
        self.no_municipio = no_municipio
        self.co_municipio = co_municipio
        self.no_mesorregiao = no_mesorregiao
        self.co_mesorregiao = co_mesorregiao
        self.no_microrregiao = no_microrregiao
        self.co_microrregiao = co_microrregiao
        self.nu_ano_censo = nu_ano_censo
        self.no_regiao = no_regiao
        self.co_regiao = co_regiao
        self.qt_mat_bas = qt_mat_bas
        self.qt_mat_inf = qt_mat_inf
        self.qt_mat_fund = qt_mat_fund
        self.qt_mat_med = qt_mat_med
        self.qt_mat_prof = qt_mat_prof
        self.qt_mat_eja = qt_mat_eja
        self.qt_mat_esp = qt_mat_esp


    def __str__(self):

        return (
            f"ID: {self.id}\n"
            f"Instituição: {self.no_entidade}\n"
            f"Código: {self.co_entidade}\n"
            f"Município: {self.no_municipio} - {self.sg_uf}\n"
            f"Região: {self.no_regiao}\n"
            f"Ano do Censo: {self.nu_ano_censo}\n"
            f"Matriculados: {self.qt_mat_bas}\n"
            f"  - Educação Infantil: {self.qt_mat_inf}\n"
            f"  - Ensino Fundamental: {self.qt_mat_fund}\n"
            f"  - Ensino Médio: {self.qt_mat_med}\n"
            f"  - Ensino Profissional: {self.qt_mat_prof}\n"
            f"  - EJA: {self.qt_mat_eja}\n"
            f"  - Educação Especial: {self.qt_mat_esp}"
        )


    def to_dict(self):
        return {
            "id": self.id,
            "no_entidade": self.no_entidade,
            "co_entidade": self.co_entidade,
            "no_uf": self.no_uf,
            "sg_uf": self.sg_uf,
            "co_uf": self.co_uf,
            "no_municipio": self.no_municipio,
            "co_municipio": self.co_municipio,
            "no_mesorregiao": self.no_mesorregiao,
            "co_mesorregiao": self.co_mesorregiao,
            "no_microrregiao": self.no_microrregiao,
            "co_microrregiao": self.co_microrregiao,
            "nu_ano_censo": self.nu_ano_censo,
            "no_regiao": self.no_regiao,
            "co_regiao": self.co_regiao,
            "qt_mat_bas": self.qt_mat_bas,
            "qt_mat_inf": self.qt_mat_inf,
            "qt_mat_fund": self.qt_mat_fund,
            "qt_mat_med": self.qt_mat_med,
            "qt_mat_prof": self.qt_mat_prof,
            "qt_mat_eja": self.qt_mat_eja,
            "qt_mat_esp": self.qt_mat_esp
        }
