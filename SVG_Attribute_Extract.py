from xml.dom import minidom # Importação da Biblioteca Imbutida(Padrão) que será usada no processo de extração dos atributos do arquivo SVG

filenames = ["file1.svg", "file2.svg", "file3.svg"] # Lista com o caminho de diretório dos arquivos SVG
# filename = ["unique_file.ext"] # No caso de um único arquivo SVG, usar uma lista com um único arquivo

# Função que irá extrair os atributos do arquivo SVG, passar os seguintes parâmetros
# "filename_list" é a lista que será inserida com o caminho dos arquivos. é recomendável que os arquivos estejam na mesma pasta do script, para que não haja erros.
# "tag_name" é o nome da Tag XML. Os atributos serão procurados somente dentro da Tag passada como parâmetro
# "attribute_selector" é o nome do Seletor XML de onde serão extraídos seus valores
def attribute_extract(filename_list, tag_name, attribute_selector):
    research_attributes_list = [] # Lista dos atributos pesquisados de todos os arquivos da lista passada como parâmetro

    for svg_file in filename_list: # Laço de Repetição para cada arquivo da lista
        document = minidom.parse(svg_file) # Abertura do arquivo para manipulação

        actual_attributes_list = [] # Alguns documentos podem ter várias tags, ocasinando assim, vários atributos, então é criado uma lista para armazená-los
        for document_tagname in document.getElementsByTagName(tag_name): # Iterando sobre cada tag do arquivo
            actual_attributes_list.append(document_tagname.getAttribute(attribute_selector)) # Adicionando o valor do seletor passado como parâmetro a lista "actual_attributes_list"
        research_attributes_list.append(actual_attributes_list) # Adição a lista principal, de todos os arquivos

        document.unlink() # Fechamento do arquivo para encerrar a operação

    return research_attributes_list # Retorno da pesquisa e extração

returned_values = attribute_extract(filenames, "svg", "id") # Exemplo de uso da função
print(returned_values) # Impressão dos valores retornados pela função