# Бэкдор: Write-up

В таске нам говорят, что за Петром пытаются следить. Что ж, поищем, как. Данный этап был немного 
угадайкой, однако, существовало несколько способов найти способ слежки:

1. Заметить, что при входе за Петра через некоторое время выводится сообщение с ошибкой про упавший
   сервис, и понять, что это за приложение, по логам.
2. Обнаружить `~/.xprofile`, в котором запускается бэкдор.
3. Сравнить образ с чистой Lubuntu и увидеть странный jar-файл.

Файл называется `button.jar`. При запуске из консоли он показывает логи движения мыши и нажатых 
клавиш, значит, скорее всего, это то, что нам нужно. Забираем себе на компьютер и смотрим.

На самом деле, jar-файлы — это почти как zip-архивы, поэтому мы можем их банально распаковать.
Внутри обнаруживаем пакеты `org.jnativehook` и `leet`. Первый полностью совпадает с 
[оригинальным репозиторием](https://github.com/kwhat/jnativehook), а второй уже поинтереснее.

Декомпилируем `leet/FileSystem.class` (в манифесте именно он указан как главный класс), и смотрим:

```java
    public FileSystem() {
        if ("42".equals(System.getenv("X_SHOW_FLAG"))) {
            final String not_a_flag = "illwpxzy_zezq_cfmro_zitf";
            try (
                    FileWriter fileWriter = new FileWriter("/tmp/flag4.txt");
                    BufferedWriter bufferedWriter = new BufferedWriter(fileWriter)
            ) {
                bufferedWriter.write("flag 4: ");
                for (int i = not_a_flag.length() - 1; i >= 0; i--) {
                    bufferedWriter.write(inverse(not_a_flag.charAt(i)));
                }
                bufferedWriter.write('\n');
            } catch (Exception e) {
                // ...
            }
        }
    }
```

Хм. Тут вряд ли есть что-то похожее на флаг. Но на всякий случай попробуем запустить программу
с переменной окружения:

    X_SHOW_FLAG=42 java -jar button.jar

О, в `/tmp/flag4.txt` флаг. Как неожиданно.

Флаг: **ugra_linux_java_backdoor**
