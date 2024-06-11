# base image
FROM node:20.11-alpine3.19 AS dev

WORKDIR /app/web

# 复制 package.json 和 package-lock.json (如果有) 到工作目录
COPY package*.json ./

# 安装项目依赖
RUN npm install

# 复制项目文件到工作目录
COPY . .

# 构建应用
RUN npm run build

# 指定运行时的端口
EXPOSE 3000

# 运行 Next.js 应用
CMD ["npm", "start"]