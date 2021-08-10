from fastapi import Request
from starlette.responses import JSONResponse

from fastemplate.exceptions import FastemplateBaseException
from fastemplate.exceptions import user
from fastemplate.exceptions import cart


def exceptions_handler(app):
    """
    API exceptions handler.

    :param FastAPI app: the main app
    """

    @app.exception_handler(FastemplateBaseException)
    async def base_exception_handler(request: Request, exception: FastemplateBaseException):
        """
        Handler for base exception.
        """
        return JSONResponse(
            status_code=exception.status_code,
            content={
                'status': exception.status_code,
                'message': exception.message,
                'exception': exception.name
            }
        )

    @app.exception_handler(cart.CartIdAlreadyExistsException)
    async def cart_id_in_use_exception_handler(request: Request, exception: cart.CartIdAlreadyExistsException):
        """
        Handler for CartIdAlreadyExistsException.
        """
        return JSONResponse(
            status_code=exception.status_code,
            content={
                'status': exception.status_code,
                'message': exception.message,
                'exception': exception.name
            }
        )

    @app.exception_handler(cart.ItemAlreadyAddedException)
    async def item_already_added_exception_handler(request: Request, exception: cart.ItemAlreadyAddedException):
        """
        Handler for CartIdNotFoundException.
        """
        return JSONResponse(
            status_code=exception.status_code,
            content={
                'status': exception.status_code,
                'message': exception.message,
                'exception': exception.name
            }
        )

    @app.exception_handler(cart.CartIdNotFoundException)
    async def cart_id_not_found_exception_handler(request: Request, exception: cart.CartIdNotFoundException):
        """
        Handler for CartIdNotFoundException.
        """
        return JSONResponse(
            status_code=exception.status_code,
            content={
                'status': exception.status_code,
                'message': exception.message,
                'exception': exception.name
            }

        )

    @app.exception_handler(cart.MismatchedLenghtException)
    async def mismatched_lenght_exception_handler(request: Request, exception: cart.MismatchedLenghtException):
        """
        Handler for MismatchedLenghtException.
        """
        return JSONResponse(
            status_code=exception.status_code,
            content={
                'status': exception.status_code,
                'message': exception.message,
                'exception': exception.name
            }
        )

    @app.exception_handler(cart.ItemNotFoundException)
    async def item_not_found_exception_handler(request: Request, exception: cart.ItemNotFoundException):
        """
        Handler for ItemNotFoundException.
        """
        return JSONResponse(
            status_code=exception.status_code,
            content={
                'status': exception.status_code,
                'message': exception.message,
                'exception': exception.name
            }
        )

    @app.exception_handler(cart.UnsupportedFileExtensionException)
    async def unsupported_file_extension_exception_handler(request: Request, exception: cart.ItemNotFoundException):
        """
        Handler for UnsupportedFileExtensionException.
        """
        return JSONResponse(
            status_code=exception.status_code,
            content={
                'status': exception.status_code,
                'message': exception.message,
                'exception': exception.name
            }
        )

    @app.exception_handler(cart.InvalidTokenException)
    async def invalid_token_exception_handler(request: Request, exception: cart.InvalidTokenException):
        """
        Handler for InvalidTokenException.
        """
        return JSONResponse(
            status_code=exception.status_code,
            content={
                'status': exception.status_code,
                'message': exception.message,
                'exception': exception.name
            }
        )

    @app.exception_handler(user.InvalidUsernameOrPassword)
    async def invalide_username_or_password_exception_handler(request: Request, exception: user.InvalidUsernameOrPassword):
        """
        Handler for InvalidUsernameOrPassword.
        """
        return JSONResponse(
            status_code=exception.status_code,
            content={
                'status': exception.status_code,
                'message': exception.message,
                'exception': exception.name
            }
        )

    @app.exception_handler(user.NiceTryMeowNowGoBack)
    async def nice_try_meow_exception_handler(request: Request, exception: user.NiceTryMeowNowGoBack):
        """
        Handler for NiceTryMeowNowGoBack.
        """
        return JSONResponse(
            headers={'WWW-Authenticate': 'Bearer'},
            status_code=exception.status_code,
            content={
                'status': exception.status_code,
                'message': exception.message,
                'exception': exception.name
            }
        )

    @app.exception_handler(user.InvalidAuthCredentials)
    async def invalid_auth_credentials_exception_handler(request: Request, exception: user.InvalidAuthCredentials):
        """
        Handler for InvalidAuthCredentials.
        """
        return JSONResponse(
            status_code=exception.status_code,
            content={
                'status': exception.status_code,
                'message': exception.message,
                'exception': exception.name
            }
        )
