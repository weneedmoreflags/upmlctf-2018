# Ultimate Shortening - Web, 300 баллов
Заглядываем в исходный код страницы и видим вставку, необходимую для Яндекс.Метрики, в которой находим ID сайта:
```
(function (d, w, c) {
    (w[c] = w[c] || []).push(function() {
        try {
            w.yaCounter49779784 = new Ya.Metrika2({
                id:49779784,
                clickmap:true,
                trackLinks:true,
                accurateTrackBounce:true
            });
        } catch(e) { }
    });

    var n = d.getElementsByTagName("script")[0],
        s = d.createElement("script"),
        f = function () { n.parentNode.insertBefore(s, n); };
    s.type = "text/javascript";
    s.async = true;
    s.src = "https://mc.yandex.ru/metrika/tag.js";

    if (w.opera == "[object Opera]") {
        d.addEventListener("DOMContentLoaded", f, false);
    } else { f(); }
})(document, window, "yandex_metrika_callbacks2");
```
Идем по https://metrika.yandex.ru/dashboard?id=49779784, видим статистику сайта и сгенерированные страницы, среди которых находим и ссылку на флаг: https://ugra.ml/hHk2l. <br>
**Флаг:** `uctf_pl3as3_d0nt_f0110w_me`
