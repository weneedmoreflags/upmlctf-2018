# Certificate Mess - Recon, 200 баллов
Автор таска: nsychev

Как вы могли заметить, [сайт нашего цтфа](https://ctf.upml.tech/) открывается по безопасному протоколу HTTPS.

Недавно оказалось, что один из наших серверов взломали. Злые хакеры украли самое важное сокровище — **сертификат безопасности**! Я думал, что всё покончено — теперь один из них обязательно сделает MitM-атаку и украдет все флаги, начал переезжать на другой домен, и вообще планировал отменить цтф.

Однако, я выяснил, что сертификат можно **отозвать**! Но, к сожалению, сертификат с сервера удалили, и я не могу узнать его номер :(

Единственное, что у нас осталось — заметка одного из сисадминов, содержащая какой-то хеш. Вот он: `E15CE349A0343793770C95630B273BC51196B64FD7A2E4C7637C043B24CA82B4`.

Найдете для меня номер сертификата? Сдайте его в формате `ab:cd:ef:...:90`

**Важно: флаг в данном таске не начинается с uctf**
