from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from fastemplate.exceptions import FastemplateBaseException
from fastemplate.exceptions.user import InvalidUsernameOrPassword, NiceTryMeowNowGoBack, InvalidAuthCredentials
from fastemplate.exceptions.cart import CartIdAlreadyExistsException, MismatchedLenghtException, \
    CartIdNotFoundException, ItemAlreadyAddedException, ItemNotFoundException, UnsupportedFileExtensionException, \
    InvalidTokenException


def exceptions_handler(app: FastAPI):
    """
    API exceptions handler.
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

    @app.exception_handler(CartIdAlreadyExistsException)
    async def cart_id_in_use_exception_handler(request: Request, exception: CartIdAlreadyExistsException):
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

    @app.exception_handler(ItemAlreadyAddedException)
    async def item_already_added_exception_handler(request: Request, exception: ItemAlreadyAddedException):
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

    @app.exception_handler(CartIdNotFoundException)
    async def cart_id_not_found_exception_handler(request: Request, exception: CartIdNotFoundException):
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

    @app.exception_handler(MismatchedLenghtException)
    async def mismatched_lenght_exception_handler(request: Request, exception: MismatchedLenghtException):
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

    @app.exception_handler(ItemNotFoundException)
    async def item_not_found_exception_handler(request: Request, exception: ItemNotFoundException):
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

    @app.exception_handler(UnsupportedFileExtensionException)
    async def unsupported_file_extension_exception_handler(request: Request, exception: ItemNotFoundException):
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

    @app.exception_handler(InvalidTokenException)
    async def invalid_token_exception_handler(request: Request, exception: InvalidTokenException):
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

    @app.exception_handler(InvalidUsernameOrPassword)
    async def invalide_username_or_password_exception_handler(request: Request, exception: InvalidUsernameOrPassword):
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

    @app.exception_handler(NiceTryMeowNowGoBack)
    async def nice_try_meow_exception_handler(request: Request, exception: NiceTryMeowNowGoBack):
        """
        Handler for NiceTryMeowNowGoBack.
        """
        return JSONResponse(
            status_code=exception.status_code,
            content={
                'status': exception.status_code,
                'message': exception.message,
                'exception': exception.name
            }
        )

    @app.exception_handler(InvalidAuthCredentials)
    async def nice_try_meow_exception_handler(request: Request, exception: InvalidAuthCredentials):
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
