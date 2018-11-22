import jwt


def encode_jwt(paylow, settings):
    encoded = jwt.encode(paylow, settings['SECRET_KEY'], algorithm='HS256')
    return encoded


def decode_jwt(access_token, settings):
    return jwt.decode(access_token, settings['SECRET_KEY'], leeway=settings["SECRET_EXPRIE"],
                      options={"verify_exp": True})
