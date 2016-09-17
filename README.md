# Setup
You need to have:
1. Docker
2. Git

Please follow this instruction:
1. docker pull gdgsurabaya/demo-1
2. git clone http://github.com/gdg-surabaya/demo-1.git
3. docker run -d --name demo_1 -p 80:8000 -v $(pwd)/demo-1:/root/app gdgsurabaya/demo-1 bash kick_start.sh