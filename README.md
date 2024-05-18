# task 2

## Интеграция приложения с Istio

### Шаг 1: Установка и настройка Istio

1. Запустить кластер Minikube:
   ```bash
   minikube start
   ```

2. Установить Istio:
   ```bash
   curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.22.0 TARGET_ARCH=x86_64 sh -
   cd istio-1.21.0
   export PATH=$PWD/bin:$PATH
   istioctl install --set profile=demo -y --set meshConfig.outboundTrafficPolicy.mode=REGISTRY_ONLY
   ```

3. Добавить метку пространства имен для автоматического внедрения Envoy sidecar:
   ```bash
   kubectl label namespace default istio-injection=enabled
   ```

### Шаг 2: Настройка входящего трафика через Ingress Gateway

1. Создать все необходимые манифесты для направления входящего трафика через Ingress Gateway.

### Шаг 3: Обновление эндпоинта /time

1. Изменить логику эндпоинта `/time` вашего приложения для выполнения запроса на `http://worldtimeapi.org/api/timezone/Europe/Moscow` и возврата значения поля `datetime` пользователю.

### Шаг 4: Разрешение внешнего трафика на worldtimeapi.org

1. Создать манифесты для разрешения внешнего трафика на `worldtimeapi.org`.

### Шаг 5: Обновление README

1. Обновить README вашего проекта, описав, куда нужно делать запрос, чтобы получить результат (оставить с предыдущего задания, если ничего не поменялось).

### Дополнительные шаги

1. Создать docker-образы и применить манифесты приложения, скрипта и сервиса.
   ```bash
   sh dpl.sh
   ```

2. Установить соединение с вашим LoadBalancer сервисом:
   ```bash
   minikube tunnel
   ```

3. Получить URL-адрес для подключения к вашему сервису и добавьте `/time` или `/statistics` для доступа к текущему времени и статистике заходов на сайт.

4. Для чтения файла `statistics.txt`, выполнить следующие шаги:
   ```bash
   kubectl get pods
   kubectl exec -it <pod_with_script_name> -- /bin/bash
   cat statistics.txt
   ```

Эти шаги интеграции нашего приложения с Istio помогут обеспечить эффективное управление трафиком и безопасностью в кластере Kubernetes.
