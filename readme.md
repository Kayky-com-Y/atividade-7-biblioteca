Nós escolhemos o on_delete.SET_NULL porque partiimos do pressuposto de que um livro pode ter mais de um autor, então se o autor x for excluído o y deveria permanecer. 

Forms sem o csrf token: sem o csrf o forms proibe o envio e a criação do arquivo por causa da falta de segurança que o csrf gera (o que é obrigatorio para evitar o envio de arquivos forjados para o banco)