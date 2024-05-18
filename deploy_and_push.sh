# Сборка образов для Flask-приложения и скрипта
docker build -t sima/flask-app -f docker1 .
docker build -t sima/script -f docker2 .

# Пуш образов в Docker Hub
docker push sima/flask-app
docker push sima/script

# Применение манифестов конфигураций Kubernetes
kubectl apply -f /Users/Serafima/OneDrive/Desktop/flask_app_deployment.yaml
kubectl apply -f /Users/Serafima/OneDrive/Desktop/flask_app_service.yaml
kubectl apply -f /Users/Serafima/OneDrive/Desktop/script_deployment.yaml

