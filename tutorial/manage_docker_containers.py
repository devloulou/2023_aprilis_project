"""
Hogyan manageled a Docker containereket?

Nem szeretnénk egyesével managelni összetartozó containereket

A containereke managelését orchestration-nek nevezzük,
és a dockerhez a legismertebb orchestration megoldások a következők:

1. Kubernetes - Google fejlesztése, container orchestration tool
2. docker-swarn - ha több clusteres - cluster: több gép van összekövetve, ezek között eloszlik a 
feldolgozások erőforrásai, és a clusteren 1 gépet node-nak nevezzük
3. docker-compose - több container egyidejű indulása, leállítás, módosítása

"""