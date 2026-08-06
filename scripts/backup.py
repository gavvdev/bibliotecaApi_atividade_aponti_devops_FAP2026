import shutil
from datetime import datetime

origem="data/livros.json"

destino=f"backups/backup-{datetime.now().strftime('%Y-%m-%d')}.json"

shutil.copy(origem,destino)

print("Backup realizado.")