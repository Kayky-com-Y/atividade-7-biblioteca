Nós escolhemos o on_delete.SET_NULL porque partiimos do pressuposto de que um livro pode ter mais de um autor, então se o autor x for excluído o y deveria permanecer. 

Forms sem o csrf token: sem o csrf o forms proibe o envio e a criação do arquivo por causa da falta de segurança que o csrf gera (o que é obrigatorio para evitar o envio de arquivos forjados para o banco)

1:

a - O LivroModelForm mudou? Por que as regras do Model funcionam nele e no Admin sem nenhuma alteração?

Não. O livroModelForm não precisa ser alterado porque usamos o Model para as validações automaticamente pelo ModelForm.

b - Qual é a diferença entre um validator e o método clean_<campo>()? Dê um exemplo de regra que só pode ser feita com clean_<campo>().

Um validator recebe um valor e o valida, normalmente lançando ValidationError se ele for inválido. É adequado para regras reutilizáveis de um único campo, como limitar páginas a 5000.

clean_<campo>() é um método do formulário para tratar um campo específico. Além de validar, pode transformar o valor e devolvê-lo. Por exemplo, normalizar o título com strip(); um validator valida, mas não deve alterar o dado.

c - Para cada regra, diga qual estratégia usar: argumento do campo, validators=[...], clean_<campo>() ou clean(). Justifique.

Título diferente do nome do autor: clean(), porque compara dois campos — título e autor.
Título sem espaços no início e no fim: clean_titulo(), retornando o título com strip(). No formulário atual, forms.CharField já usa strip=True por padrão.
Máximo de 5000 páginas: validators=[MaxValueValidator(5000)] no campo do model. É uma regra de um único campo que deve valer também no Admin.
Livro indisponível precisa ter ISBN: clean(), pois depende dos valores de disponibilidade e ISBN. A validação deve gerar um erro se estiver indisponível e o ISBN estiver vazio.

2:
