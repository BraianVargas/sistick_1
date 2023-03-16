from producto import productoBP

@productoBP.route('/')
def index():
    return "Product Index"