from sources.application import create_application
from sources.setting import setting

import uvicorn

application = create_application()

if __name__ == "__main__":
    uvicorn.run(app="sources.main:application", host=setting)
