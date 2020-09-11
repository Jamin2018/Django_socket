from django.utils.deprecation import MiddlewareMixin


class SoloveCrossDomainMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        """
        处理跨域的中间件，将所有的响应都能实现跨域
        """
        response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Allow-Headers'] = "Content-Type"
        return response