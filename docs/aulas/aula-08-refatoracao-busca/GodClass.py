class GodClass:
    """
    Exemplo de God Class com responsabilidades desconexas.
    
    Métodos de string, matemática, formatação e email convivem aqui, reduzindo a coesão.
    """
    def __init__(self, smtp_server: str = "smtp.example.com") -> None:
        self.cache = {}
        self.smtp_server = smtp_server
    
    # ---- Manipulação de Strings ----
    def str_title_case(self, s: str) -> str:
        return ' '.join([w.capitalize() for w in s.split()])
    
    def str_slugify(self, s: str) -> str:
        return s.lower().strip().replace(' ', '-').replace('_', '-')
    
    # ---- Cálculos Matemáticos ----
    def math_mean(self, xs: list[float]) -> float:
        if not xs:
            return 0.0
        return sum(xs) / len(xs)
    
    def math_std(self, xs: list[float]) -> float:
        if not xs:
            return 0.0
        m = self.math_mean(xs)
        return (sum((x - m) ** 2 for x in xs) / len(xs)) ** 0.5
    
    # ---- Formatação de Arquivo/CSV ----
    def file_render_csv(self, rows: list[list[str]]) -> str:
        return '\n'.join([','.join(map(str, r)) for r in rows])
    
    # ---- Email/IO ----
    def email_send_report(self, report: str, to: str) -> bool:
        if not to or '@' not in to:
            return False
        return True
    
    # ---- Lógica de Negócio Misturada ----
    def process(self, text: str, xs: list[float], rows: list[list[str]], to: str) -> dict[str, object]:
        title = self.str_title_case(text)
        slug = self.str_slugify(text)
        mean = self.math_mean(xs)
        std = self.math_std(xs)
        csv = self.file_render_csv(rows)
        sent = self.email_send_report(f"{title} / {mean:.2f}±{std:.2f}\n{csv}", to)
        return {"title": title, "slug": slug, "mean": mean, "std": std, "csv": csv, "sent": sent}