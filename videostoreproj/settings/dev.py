from .base import *

DEBUG = True

MEDIA_ROOT = '/demo/media'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'xyz_console': {
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'land': {
            'handlers': ['xyz_console'],
            'level': 'DEBUG'
        }
    }
}

STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')
STRIPE_PLAN_MONTHLY_ID = os.environ.get('STRIPE_PLAN_MONTHLY_ID')
STRIPE_PLAN_ANNUAL_ID = os.environ.get('STRIPE_PLAN_ANNUAL_ID')
STRIPE_WEBHOOK_SIGNING_KEY = os.environ.get('STRIPE_WEBHOOK_SIGNING_KEY')


PAYPAL_WEBHOOK_ID = os.environ.get('PAYPAL_WEBHOOK_ID')
PAYPAL_CLIENT_ID = 'AdEp2G56jT8NzXFZaB28YHIuzzhpu-PwM-DscZptqPWHsXGWiuKYmsmoDhfxfIy7dVFz_ANte09MCnGP'
PAYPAL_CLIENT_SECRET = 'ECuj1x7aEJldYi6Xy7fKm5JeSFFsi9cyg47K1m4s49VRoaOogubwACqNYtqILx-T8gto_Rh7lvtQn1-t'
PAYPAL_PLAN_MONTHLY_ID = 'P-4UC9584338506991TMCQY3OQ'
PAYPAL_MODE = 'sandbox'
