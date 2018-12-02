# Config file for db connectors etc


class Config(object):
    """
    Common configurations.
    """

    # TODO: Put all common config things here


class DevelopmentConfig(Config):
    """
    Config section for when working with dev env.
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Config section for when using in live env.
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
