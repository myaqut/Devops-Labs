# Docker Best Practises



#### 1- Identify Cacheable Units
Using more than one RUN command will affect the performance. use only one RUN command and add the dependencies to requirments.txt file.

#### 2- Reduce image size
You can reduce the image size by avoiding adding any unnecessary modules or dependencies. you can also avoid adding any debugging dependencies.

#### 3- Use Official Docker Images
Official docker image keeps you away from having extra size and not needed dependencies. Also, the official image is more secured and realiable. 

#### 4- Multi Stage Build
You can use use more than one stage in order to prevent usign the dependencies in the running container. you can check the example below.
    # Stage 0, "build-stage", based on Node.js, to build and compile the frontend
    FROM node:13.12.0 as build-stage
    WORKDIR /app
    COPY package*.json /app/
    RUN npm install
    COPY ./ /app/
    RUN npm run build
    # Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
    FROM nginx:1.15
    COPY --from=build-stage /app/build/ /usr/share/nginx/html

#### 5- Use Only Needed Privileges 
Don't give more than needed privileges to access other resources. Only give the privilege needed to access the required resources.


