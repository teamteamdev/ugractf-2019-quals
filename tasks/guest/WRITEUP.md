# Гостевой режим: Write-up

1. Запускаем загрузку торрента.
2. Ужасаемся его размеру.
3. Пишем в чате, что таск не очень.
4. Загружаем архив до конца.
5. Не выключаем раздачу.

После этого, распаковав, обнаруживаем странные файлы. Погуглив непонятные руны вида `vmdk`, `vbox`, понимаем (или просто догадываемся), что перед нами образ виртуальной машины VirtualBox.

Импортируем, запускаем. С вероятностью 60% у нас даже всё получается (если не повезет, придется сбросить снапшот). В любом случае, получаем экран входа. 

На экране входа есть пользователь Guest без пароля. Неожиданно для себя обнаруживаем, что таск именно на это и намекает. Входим, видим в домашней директории файл. Методом просмотра расширения понимаем, что файл `flag.7z` скорее всего является файлом, лежащим в 7-Zip архиве.

Однако, на виртуалке нет 7-Zip, поэтому для решения таска можно использовать два способа:

1. Настроить интернет в виртуалке, скачать 7-Zip (`apt install p7zip-full`), распаковать.
2. Настроить VMWare Tools и перетащить файл на хост-машину.

Распаковываем архив, и внутри оказывается флаг.

Флаг: **ugra_b055box_ready**
