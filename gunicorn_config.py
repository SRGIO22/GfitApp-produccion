import os

def on_starting(server):
    # Forzar a que se ejecute tu script de base de datos antes de arrancar la web en internet
    if os.path.exists('scripts/populate_db.py'):
        print("Configurando base de datos de producción GfitApp...")
        os.system('python scripts/populate_db.py')