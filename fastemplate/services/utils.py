from starlette.middleware.cors import CORSMiddleware


def allow_cors(app):
    """
    # TODO: docstring
    """
    return app.add_middleware(CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True
    )
