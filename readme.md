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
a - O que acontece se esquecermos request.FILES na view? E se esquecermos o enctype no template? Reproduza os dois erros e descreva o que viram (o formulário dá algum aviso?).

Nos dois casos, a view não recebe a imagem. A capa é opcional, então o formulario não avisa

b -  Qual é a diferença entre STATICFILES_DIRS / {% static %} e MEDIA_ROOT / .url? Quando usar cada um na Mini biblioteca?

STATICFILES_DIRS e {% static %} são utilizados para arquivos estáticos do projeto, como CSS, JavaScript e imagens fixas. Já MEDIA_ROOT e .url são utilizados para arquivos enviados pelos usuários, como as capas dos livros. Na Mini biblioteca, estilos e ícones fixos pertencem a static; as capas enviadas pelos usuários pertencem a media.

c -  Ao excluir um livro (ou trocar a capa), o arquivo antigo continua em media/capas/. Por que isso acontece e que problema pode causar a longo prazo?

O banco guarda o caminho da imagem, não o arquivo. Excluir o livro apaga o registro, mas o arquivo continua armazenado. Ao substituir a capa, o campo passa a apontar para o novo arquivo, mas o antigo ainda permanece guardado.

Com o tempo, isso acumula arquivos inutilizados que consomem espaço, alem disso se os arquivos contiverem dados pessoais, pode haver um problema de que o usuario ou dono dos arquivos querem a exclusão irreparavel dos arquivos, mas não conseguirem.

d - Por que a extensão do arquivo não basta como proteção? Que outros cuidados o servidor deve ter com uploads?

Um arquivo que não é imagem pode ser renomeado para .png assim passando por sima da proteção de extensão. Verificação e limite de tamanho alem da verificação do conteúdo real.

3: 
a - Na CreateView, quem faz o if request.method == "POST" que escrevíamos à mão? O que acontece quando o formulário é inválido?

 View.dispatch() encaminha a requisição para get() ou post(). Na CreateView, o ProcessFormView.post() obtém o formulário, verifica is_valid() e chama form_valid() ou form_invalid(). Se for inválido, o formulário é exibido novamente com os erros e não é salvo.

 b - Por que o upload da capa continuou funcionando na CreateView sem passarmos request.FILESmanualmente?

 O FormMixin.get_form_kwargs() inclui automaticamente request.POST e request.FILES ao criar o formulário. Por isso, não é preciso passar request.FILES manualmente como na view de função.

 c - Por que o DeleteView mostra uma página de confirmação e só exclui no POST? Que problema aconteceria se a exclusão ocorresse em um GET?

 O GET apenas mostra a página de confirmação, a exclusão acontece no POST. Se o GET excluísse, então um link ou um robô poderia apagar dados sem uma confirmação explícita.

 d -  Cite uma vantagem e uma desvantagem das CBVs em relação às FBVs. Em que situação você ainda escolheria uma função?

 Uma vantagem das CBVs é reduzir código repetitivo e facilitar a reutilização do comportamento genérico. Uma desvantagem é que o fluxo pode ficar menos explícito, especialmente com muitas heranças ou personalizações. Eu escolheria uma FBV para uma operação pequena ou muito específica, quando a sequência de ações fica mais clara escrita diretamente.