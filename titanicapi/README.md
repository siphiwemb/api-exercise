
## Useful information:


# Tools and tech stack
This is the list of technologies and tools that I used of for this excercise:
* `SQLite`: To import DB Data from the csv provided into a small, fast, self-contained, high-reliability, full-featured, SQL database engine. 
* `Django`: For the RESTful API - a high-level Python web framework that encourages rapid development and clean, pragmatic design.
* `Minikube`: To serve as a local Kubernetes infrastructure.
* `Docker/Docker-compose`: Used to accelerate the api build. (would have been nice to explore https://kompose.io/)
* `AWS ECR`: I used a fully managed Docker container registry that makes it easy to store, share, and deploy container images.
* `Github`: Hosted code in Github and imported to GitLab when I realised i need to share the project with a GitLab user.
* `Git Actions`: To automate all the workflows,CI/CD. Build, tag, scan, push and deploy to minikube
* `Secrets`: Used github to store secrets.
* `Trivy`: To Scan docker images for critical vulrenabilities.
* `Postman`: To test the API

# Project structure
This is the Project struture and folder definitions of the Solution presented in this repo:
* `.github` - Contains a git action workflow folder that has a main.yml file that defines CI/CD configuration.
* `titanicapi` - Main Project Folder, where the Dockerfile, manage.py, titanic.sqlite3 files reside.
    * `Manifests` - Contains all the kubernetes yaml files to configure k8s resources.
    * `titanicapi` - Settings.py & Urls.py resides in here - this is where I configure Django app settings, routes including DB connections.
    * `webapp` - Api implementations live in here - models, views and the serializer.


# Notes
* To run this locally, in the titanic project directory, run `docker-compose up`, this will create the API, connect to SQLite DB and Start the development server on http://0.0.0.0:8080/ 
* To Get a list of all people http://0.0.0.0:8080/api/people will return the desired results.
* To Get person by id http://0.0.0.0:8080/api/people?id=887 i.e. this will return Mr. Prtrick Dooley.
* To Update person by id http://0.0.0.0:8080/api/people?id=887 i.e. this Update entry with id 887 given the correct Json Body.
* To Delete person by id http://0.0.0.0:8080/api/people?id=887 i.e. will delete entry with id 887 accodingly.

#Automation Notes
* On push, using ubuntu as a runner agent the pipeline will checkout the main branch, pull AWS crendentials from github Secrets and Login to ECR, build and tag the image using the dockerFile in the checked out repo. Scan the image for vulrenabilities before it pushes the to ECR.
* Once the image is pushed to ECR minikube is deployed with an argument that passed which sets a deployment.yml to use the latest build image tag.
* A deploy to minikube is then applied where kubernetes resources are now created.
* Minikube service list is then displayed showing api service before the runner dies.

This was to display a one push automation that does an end-to-end build and deploy to kubernetes. Whoever given and existing cluster this was going to be archived with the following steps in my git actions:

```    # Deploy to EKS cluster
    - name: Deploy to cluster
      uses: kodermax/kubectl-aws-eks@master
      env:
        KUBE_CONFIG_DATA: ${{ secrets.KUBE_CONFIG_DATA }}
        ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
        ECR_REPOSITORY: titanicapi
        IMAGE_TAG: ${{ github.sha }}
      with:
        args: set image -n titanicapi-ns deployment/titanicapi-api titanicapi-api=$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
    # Verify deployment
    - name: Verify deployment
      uses: kodermax/kubectl-aws-eks@master
      env:
        KUBE_CONFIG_DATA: ${{ secrets.KUBE_CONFIG_DATA }}
      with:
        args: rollout status -n titanicapi-ns deployment/titanicapi-api```
