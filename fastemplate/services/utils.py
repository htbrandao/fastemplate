from starlette.middleware.cors import CORSMiddleware


def allow_cors(app):
    """
    Enable CORS in app

    :param FastAPI app: the main app
    :return: app with CORS enabled
    :rtype: FastAPI
    """
    return app.add_middleware(CORSMiddleware,
                              allow_origins=["*"],
                              allow_methods=["*"],
                              allow_headers=["*"],
                              allow_credentials=True
                              )
