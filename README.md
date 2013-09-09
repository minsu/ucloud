UCloud(CloudStack) Python Client
===

* Original Code from https://github.com/minsu/ucloud
* Forked and Revised by Jioh L. Jung (ziozzang@gmail.com)

The Python Commandline Tool & library for UCloud.

유클라우드 서버 API를 이용한 파이썬 클라이언트 라이브러리 및 Command Line 유틸리티 프로그램입니다.


### Installation Note

별도 설치없이 Git 클론한 후에 해당 폴더에서 명령을 실행하거나 해당 파이썬 모듈을 `import UClient` 한 후에 사용합니다. 명령어 실행은 다음의 Example과 같이 Command Line 환경에서 실행 합니다.

    python UClient.py server listVirtualMachines
    python UClient.py server deployVirtualMachine serviceofferingid=75 templateid=845 zoneid=2 diskofferingid=38 usageplantype=hourly
    ...
    python UClient.py server queryAsyncJobResult jobid=19993

    python UClient.py lb listLoadBalancers

    python UClient.py waf listWAFs
    

파이썬 라이브러리로 사용 하는 경우에는 ```pip install ucloud``` 로 설치 하면 됩니다.

### 환경 설정

* 파일에 직접 수정
 * Client.py 를 열어서 API_KEY 와 SECRET 을 수정 하거나, 환경 변수로 설정 할수 있다.

* 환경 변수로 설정
 * API/SECRET Key 설정: ```UCLOUD_API_KEY```, ```UCLOUD_SECRET``` 가 환경 변수로 설정 되어 있으면 해당 값을 읽어서 씁니다. (export 또는 윈도에서 set 으로 설정 하면 됩니다)
 * 출력 형식 지정: 기본은 JSON 출력이나, XML 출력을 하고 싶으면 환경변수에 ```UCLOUD_RESP_TYPE``` 를 xml 로 세팅 해주시면 됩니다.

* 코드로 실행 하는 경우, 파라미터로 넘겨 주는 방법
 * ``` client  = UClient.UClient(api_type="package", api_key=UCLOUD_API_KEY, secret=UCLOUD_SECRET) ``` 와 같이 파라미터로 넘겨줌



### 커맨드 라인으로 실행

```
./UClient.py [api_type] [command] [params1] [param2]...
```
기본 실행 형식입니다.

 

예를들어 zoneID 를 얻는 API는 다음과 같습니다.

관련 API 문서 http://developer.ucloudbiz.olleh.com/doc/cloudstack/etc/listZones/
```
./UClient.py server listZones
``` 

 

예를들어 WAF 생성 API 는 다음과 같습니다.

관련 API 문서 http://developer.ucloudbiz.olleh.com/doc/waf/WAF/createWAF-A/
```
./UClient.py waf name=wafname type=single spec=basic zoneid=9845bd17-d438-4bde-816d-1b12f37d5080 waf1consoleport=5950 waf1SSHport=5951 waf1DBport=5952
```

### 코드로 사용하기

파이썬 모듈로 사용할때에는 다음과 같이 사용하면 됩니다.

```
import json
from ucloud import UClient

client = UClient.UClient(api_type="server", api_key="API_KEY_HERE", secret="SECRET_KEY_HERE")
params = {
  "parameter1":"value1",
}
post_data = {
  "body1": "longbody1",
}
resp = client.run("Command", params, post=post_data) # POST 로 넘기는 경우
resp = client.run("Command", params) # POST를 쓰지 않는 경우
```


### API 타입 목록
중간에 들어가는 api_type 은 다음을 확인해주시면 됩니다.

종류 | API 타입 | 매뉴얼/가이드 | API 주소
--- | --- | --- | ---
AutoScaling	| as | http://developer.ucloudbiz.olleh.com/doc/autoscaling/ | https://api.ucloudbiz.olleh.com/autoscaling/v1/client/api
CDN | cdn | http://developer.ucloudbiz.olleh.com/doc/CDN/ | https://api.ucloudbiz.olleh.com/cdn/v1/client/api
Loadbalancer | lb | http://developer.ucloudbiz.olleh.com/doc/loadbalancer/ | https://api.ucloudbiz.olleh.com/loadbalancer/v1/client/api
Messaging | msg | http://developer.ucloudbiz.olleh.com/doc/messaging/ | https://api.ucloudbiz.olleh.com/messaging/v1/client/api
NAS Service | nas | http://developer.ucloudbiz.olleh.com/doc/nas/ | https://api.ucloudbiz.olleh.com/nas/v1/client/api
Packaging | package | http://developer.ucloudbiz.olleh.com/doc/packaging/ | https://api.ucloudbiz.olleh.com/packaging/v1/client/api
Server/CloudStack | server | http://developer.ucloudbiz.olleh.com/doc/cloudstack/ | https://api.ucloudbiz.olleh.com/server/v1/client/api
uCloud DB/RDBAAS | db | http://developer.ucloudbiz.olleh.com/doc/DB/ | https://api.ucloudbiz.olleh.com/db/v1/client/api
Watch | watch | http://developer.ucloudbiz.olleh.com/doc/watch/ | https://api.ucloudbiz.olleh.com/watch/v1/client/api
Web Application Firewall | waf | http://developer.ucloudbiz.olleh.com/doc/waf/ | https://api.ucloudbiz.olleh.com/waf/v1/client/api


### 디버깅 방법
현재 디버깅은 코드로 작성 하는 경우에만 지원 합니다. 파라미터를 넣어 실행할때에 debug=True 로 실행 해주면 됩니다.

```
client.run(.... , debug=True)
```

### 주의사항

프로그램 사용상 주의할 점들입니다.

- 실행하기 전에 API 키 값과 Secret Key 값을 설정 해 주어야 명령들이 동작합니다.
- 일부 명령어의 경우 Command Line 실행시 보기 편한 형태로 출력되지만, 필요한 필드가 빠져있을 수 있습니다. 또한 대부분의 명령은 서버가 회신한 JSON/XML 데이터를 출력합니다.
- 모듈로 사용할 경우 모든 데이터는 JSON 데이터로 처리되어야 합니다.
- 커맨드 라인으로 명령어를 호출할 경우 오직 GET 방식으로 요청 됩니다.
- 잘못된 명령에 대한 서버의 반응은 별도의 에러메시지도 출력되지만 XML포맷으로된 에러 메시지가 출력 됩니다.
- `destroyVirtualMachine`과 같은 명령은 `stopVirtualMachine`이 이루어 진 다음에 실행되어야 정상 동작합니다.

### 지원하는 명령들

유클라우드 서버 API 전체가 사용가능합니다, 테스트 해 본 것은 VM 관련한 명령과 Port Forwarding 관련 명령 뿐입니다.

유클라우드 로드밸런서 API 지원이 추가되었습니다. (2012. 11. 13)

유클라우드 웹 방화벽 API 지원이 추가되었습니다. (2013. 02. 20)

유클라우드 Package API 지원이 추가 되었습니다. (2013. 08. 19)

유클라우드 전체 API 지원이 추가 되었습니다. (2013. 08. 23)

PIP/PyPI 에서 설치가 가능합니다. (2013. 09. 09)

### 기본값 지정을 통한 편리한 사용

`commands.py` 에 명시되어 있는 각 명령에는 `default` 라는 Dictionary 데이터가 있습니다. 기본 값으로 지정할 경우 명령창에서 별도로 지정하지 않는 한 해당 `default` 값이 사용됩니다. 현재 `deployVirtualMachine` 명령의 기본값은 kr-1b 존에 `Ubuntu 11.04 32bit, 1vCore, 1GB RAM, 100GB Disk` 시간제 요금이 들어가 있습니다.

`commands.py` 에 명시 되어 있지 않은 명령어도 실행에는 문제가 없으며 API 문서를 보고 적절한 파라미터를 명시하면 명령어를 사용할수 있습니다.


### 버전

0.1A : 2012. 03. 19 Release

0.2A : 2012. 11. 13

0.3A : 2013. 02. 20

0.3A-Forked-ziozzang-v1 : 2013. 08. 19

0.3A-Forked-ziozzang-v3 : 2013. 08. 23

1.0 : 2013. 09. 09
