# Connection à un Raspberry branché sur le port ethernet en SSH

* Configurer une connexion ethernet avec `Link-Local Only` dans `IPv4 Settings` (Varie selon le network manager, parfois non nécessaire)
* Allumer le raspberry, le brancher en ethernet
* `ssh pi@raspberry-name-here.local`
* Enjoy

Note: sur Arch cela ne fonctionne pas par défaut, il faut activer le mdns: https://wiki.archlinux.fr/Avahi
J'ai dû également dans mon network manager sous l'onglet "ethernet" choisir le device qui a un nom (et pas uniquement une adresse mac).
