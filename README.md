# Одноранговый мессенджер на PyQt

## Задание:
Требуется создать одноранговый мессенджер, реализующий следующий функционал:

- Поддержка подключения к удалённому клиенту по IP адресу.
- Шифрование с открытым ключом.
- Передача текстовых сообщений.
- Передача изображений в тексте с их показом.
- Передача прочих файлов.

## Запуск

```shell script
pyuic5 resources/messenger.ui -o resources/messenger.py 

python main.py 9002
```
## Скриншоты

![Сообщения в чате](https://github.com/elizarpif/p2p/blob/develop/screenshots/6.png)


![Изображение в чате](https://github.com/elizarpif/p2p/blob/develop/screenshots/7.png)

![Два клиента](https://github.com/elizarpif/p2p/blob/develop/screenshots/p2p.png)