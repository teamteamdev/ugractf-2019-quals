# Ученый: Write-up

Нам дан PDF-файл с каким-то, по всей видимости шаблонным, PDF-файлом.

Исследовав данный файл, можно заметить, что PDF-файл содержит вложенный 
файл.

Понять этот факт намного проще, найдя оригинал в Интернете — этот
файл был шаблоном с Overleaf. Сравня PDFку с оригиналом и поняв, за что отвечают 
различающиеся блоки, можно также обнаружить вложение.

Открыть же искомый файл очень просто — любой десктопный PDF-ридер (например, 
стандартный Adobe Reader) показывает такие файлы на вкладке «Вложения». Там 
будет картинка, в которой и написан флаг.

Флаг: **ugra_its_not_an_embedded_file**
