from rest_framework.pagination import PageNumberPagination

class SmallPagination(PageNumberPagination):
    #Define el parametro de request para la paginacion 
    page_query_param = 'p'
    #define el tamaño de pagina
    page_size = 6
    #define en la url la cantidad de paginas que se va a mostrar
    page_size_query_param = "page_size"
    #Define el parametro maximo de paginas que se muestra
    max_page_size = 6


class MediumPagination(PageNumberPagination):
    #Define el parametro de request para la paginacion 
    page_query_param = 'p'
    #define el tamaño de pagina
    page_size = 10
    #define en la url la cantidad de paginas que se va a mostrar
    page_size_query_param = "page_size"
    #Define el parametro maximo de paginas que se muestra
    max_page_size = 10



class LargeePagination(PageNumberPagination):
    #Define el parametro de request para la paginacion 
    page_query_param = 'p'
    #define el tamaño de pagina
    page_size = 18
    #define en la url la cantidad de paginas que se va a mostrar
    page_size_query_param = "page_size"
    #Define el parametro maximo de paginas que se muestra
    max_page_size = 18