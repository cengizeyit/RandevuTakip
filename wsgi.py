# uygulamaları getir
from controller.auth import bp_auth
from controller.dashboard import bp_dashboard
from app import *

app.register_blueprint(bp_auth)
app.register_blueprint(bp_dashboard)

# uygulamaları kaydet
if __name__=='main':
    app.run()