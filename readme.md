# Цель

Создайте индикатор, показывающий, что пришло время уйти с рынка криптовалют (бычий рынок окончен).

Индикатор составной:
- прирост просмотров каналов в YT по криптотематике
- прирост подписок на каналы в YT по криптотематике
- недельный RSI
- недельный MA
- Инекс страха и жадности (непрерывной жадности в днях)
- прирост скачиваний приложений криптобирж, криптокошельков


Ресурсы:
- https://developers.appbrain.com/info/help/api/specification.html Google Play app information
- https://fastapi-utils.davidmontague.xyz/user-guide/repeated-tasks/ Fastapi Repeated Tasks
- https://fastapi.tiangolo.com/tutorial/background-tasks/ - Fastapi Background Tasks
- https://console.cloud.google.com/apis/library/youtube.googleapis.com?project=yt-crypto-analytics - YouTube Data API v3
- https://socialblade.com/youtube/channel/UCLnMsLbiJxgNjfX-AW9uHWw/monthly - socialblade, YT historical statistic 