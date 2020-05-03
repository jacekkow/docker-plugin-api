import functools

import flask
from werkzeug.local import LocalProxy


class InputValidationException(Exception):
    pass


class Blueprint(flask.Blueprint):
    logger = LocalProxy(lambda: flask.current_app.logger)

    def route(self, route, **options):
        parent_function_wrapper = super().route(route, **options)

        def newFunctionWrapper(func):
            @functools.wraps(func)
            def newFunction():
                try:
                    result = func()
                except InputValidationException as e:
                    self.logger.error(e)
                    return {
                        'Err': e.args[0],
                    }
                return result

            return parent_function_wrapper(newFunction)

        return newFunctionWrapper


app = Blueprint('Plugin', __name__)

functions = []


@app.route('/Plugin.Activate', methods=['POST'])
def Activate():
    return {
        'Implements': functions,
    }


__all__ = ['InputValidationException', 'Blueprint', 'app', 'functions']
