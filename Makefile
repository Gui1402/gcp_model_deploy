serving-local:
	export MODEL_NAME=cats & export MODEL_PATH="$(pwd)/models/${MODEL_NAME}"
	systemctl start docker &
	sudo docker run -p 8500:8500 -p 8501:8501 -v "${MODEL_PATH}:/models/${MODEL_NAME}" -e MODEL_NAME="${MODEL_NAME}" -t tensorflow/serving:latest


serving-gcp:
	export MODEL_NAME=cats & export PROJECT_NAME=ml-practice-307417
	gcloud auth configure-docker
	sudo docker build -t "gcr.io/${PROJECT_NAME}/${MODEL_NAME}" .
	sudo docker push "gcr.io/${PROJECT_NAME}/${MODEL_NAME}"
	gcloud run deploy --image "gcr.io/${PROJECT_NAME}/${MODEL_NAME}" --platform managed --region us-east1 --allow-unauthenticated --project ${PROJECT_NAME}

