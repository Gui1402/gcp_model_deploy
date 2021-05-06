FROM tensorflow/serving

COPY ./models/* /models/

ENV MODEL_BASE_PATH=/models

WORKDIR models

# Expose ports
# #gRPC
# EXPOSE 8081

# REST
EXPOSE 8501

# Set where models should be stored in the container
ENV MODEL_BASE_PATH=/models

# The only required piece is the model name in order to differentiate endpoints
ENV MODEL_NAME=crack_detect

# Create a script that runs the model server so we can use environment variables
# while also passing in arguments from the docker command line
RUN echo '#!/bin/bash \n\n\
tensorflow_model_server \
--rest_api_port=8080 \
--model_name=${MODEL_NAME} \
--model_base_path=${MODEL_BASE_PATH} \
"$@"' > /usr/bin/tf_serving_entrypoint.sh \
&& chmod +x /usr/bin/tf_serving_entrypoint.sh

ENTRYPOINT ["/usr/bin/tf_serving_entrypoint.sh"]
