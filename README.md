UCloud(CloudStack) Python Client
===

유클라우드 서버 API를 이용한 파이썬 클라이언트 라이브러리 및 Command Line 유틸리티 프로그램입니다.

### Installation Note

별도 설치없이 Git 클론한 후에 해당 폴더에서 명령을 실행하거나 해당 파이썬 모듈을 `import UClient` 한 후에 사용합니다. 명령어 실행은 다음의 Example과 같이 Command Line 환경에서 실행 합니다.

    python UClient.py listVirtualMachines
    python UClient.py deployVirtualMachine serviceofferingid=75 templateid=845 zoneid=2 diskofferingid=38 usageplantype=hourly
    ...
    python UClient.py queryAsyncJobResult jobid=19993

### 주의사항

프로그램 사용상 주의할 점들입니다.

- 실행하기 전에 Client.py 파일을 열어 API 키 값과 Secret Key 값을 지정해 주어야 명령들이 동작합니다.
- 일부 명령어의 경우 Command Line 실행시 보기 편한 형태로 출력되지만, 필요한 필드가 빠져있을 수 있습니다. 또한 대부분의 명령은 서버가 회신한 JSON 데이터를 출력합니다.
- 모듈로 사용할 경우 모든 데이터는 JSON 데이터로 처리되어야 합니다.
- 잘못된 명령에 대한 서버의 반응은 별도의 에러메시지 보다는 `500 Server Error`만 나오기 때문에 디버깅 시에는 명령어 파라미터 등에 대한 오탈자를 잘 살펴보아야 합니다.
- `destroyVirtualMachine`과 같은 명령은 `stopVirtualMachine`이 이루어 진 다음에 실행되어야 정상 동작합니다.

### 지원하는 명령들

유클라우드 서버 API 전체가 사용가능합니다, 테스트 해 본 것은 VM 관련한 명령과 Port Forwarding 관련 명령 뿐입니다.

### 기본값 지정을 통한 편리한 사용

`commands.py` 에 명시되어 있는 각 명령에는 `default` 라는 Dictionary 데이터가 있습니다. 기본 값으로 지정할 경우 명령창에서 별도로 지정하지 않는 한 해당 `default` 값이 사용됩니다. 현재 `deployVirtualMachine` 명령의 기본값은 `Ubuntu 11.04, 1GB, 100GB` 시간제 요금이 들어가 있습니다.

### 사용자 포럼

유클라우드 서버 API 사용자 채널이 [아이언백](http://www.ironbag.net)에 개설되어 있으며 모든 문의는 해당 채널을 통해 받습니다. 또한 관련한 팁이나 사용담 등을 서로 공유하였으면 하는 바램입니다.

### 버전

0.1A : 2012. 03.19 Release

[채널바로가기]( http://www.ironbag.net/channel/00287799451678010)
===
