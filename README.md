# 세린이 키우기

## 개요
"세린이 키우기"는 Pygame을 사용하여 개발된 게임입니다. 이 게임에서 플레이어는 세린이라는 캐릭터를 조작하여 다양한 몬스터와 싸우고 아이템을 수집합니다. 게임은 여러 종류의 몬스터, 경험치, 아이템(무기, 스탯) 등을 특징으로 합니다.


![Example Image](https://github.com/yujin-zero/Project-Serin/blob/main/image/game.png)


## 게임 설명
이 게임은 세린이라는 캐릭터가 몬스터와 싸우며 얻은 경험치로 레벨업을 하면서 레벨업 시 아이템을 골라 세린이를 더 강하게 만들고, 강해진 세린이를 오랫동안 버텨서 최고점수를 갱신하며 즐길 수 있는 게임입니다.
## 요구 사항
- Python 3.10.13
- Pygame 라이브러리
- 코드에 명시된 기타 종속성

## 설치

### Windows
1. Python이 설치되어 있는지 확인합니다. [python.org](https://www.python.org/downloads/)에서 다운로드할 수 있습니다.
2. 명령 프롬프트를 열고 다음 명령어를 입력하여 Pygame을 설치합니다:
    ```bash
    pip install pygame
    ```
3. 게임 파일을 다운로드하고 `main.py`가 있는 디렉토리로 이동합니다.

### macOS
1. Python이 설치되어 있는지 확인합니다. [python.org](https://www.python.org/downloads/)에서 다운로드할 수 있습니다.
2. 터미널을 열고 다음 명령어를 입력하여 Pygame을 설치합니다:
    ```bash
    pip install pygame
    ```
3. 게임 파일을 다운로드하고 `main.py`가 있는 디렉토리로 이동합니다.

### Linux
1. Python이 설치되어 있는지 확인합니다. 배포판의 패키지 관리자를 사용하여 Python을 설치할 수 있습니다. 예를 들어:
    ```bash
    sudo apt-get install python3
    ```
2. 터미널을 열고 다음 명령어를 입력하여 Pygame을 설치합니다:
    ```bash
    pip install pygame
    ```
3. 게임 파일을 다운로드하고 `main.py`가 있는 디렉토리로 이동합니다.

## 게임 실행
종속성을 모두 설치한 후, `main.py`가 있는 디렉토리로 이동하여 다음 명령어로 게임을 실행합니다:

```bash
python main.py
```


## 게임 조작법
- 화살표 키를 사용하여 세린을 이동합니다.
- 아이템을 수집하고 몬스터를 처치하여 경험치를 획득합니다.

## 특징
- **몬스터**: 다람쥐, 대나무 몬스터, 영혼 몬스터 등 다양한 종류의 몬스터가 등장합니다.
- **아이템**: AppleWeapon과 CarrotWeapon 등의 아이템을 수집하여 능력을 향상시킬 수 있습니다.
- **경험치 바**: 진행 상황을 추적하고 레벨을 올릴 수 있습니다.
- **UI 요소**: 화면에 처치한 몬스터 수와 코인 수가 표시됩니다.

## 코드 구조
- **main.py**: 게임을 초기화하고 실행하는 메인 파일.
- **Background.py**: 배경 이미지 로딩 및 스크롤링을 처리합니다.
- **Camera.py**: 카메라가 플레이어 캐릭터를 따라가도록 관리합니다.
- **Serin.py**: 세린 캐릭터 클래스를 포함합니다.
- **spawn.py**: 몬스터 스폰을 관리합니다.
- **monster_squirrel.py, monster_BamBoo.py, monster_Spirit.py**: 다양한 몬스터 클래스.
- **ui.py**: 사용자 인터페이스 요소를 관리합니다.
- **Inventory.py**: 인벤토리 시스템을 관리합니다.
- **AppleWeapon.py**: 사과가 돌며 몹을 공격하는 무기.
- **CarrotWeapon.py**: 당근이 총처럼 쏴지며 공격하는 무기.
- **WhipWeapon.py**: 채찍이 앞에 있는 몹을 공격하는 무기.
- **LeafWeapon.py**: 나뭇잎이 사방으로 발사되며 공격하는 무기.
- **WingBoots.py**: 이동속도를 증가시키는 아이템.
- **Heart.py**: 피회복 아이템
- **HealthBoostItem.py**: 최대 체력을 증가시키는 아이템.
- **DamageReductionItem.py**: 받는 피해를 줄이는 아이템.
- **DamageText.py**: 데미지 텍스트를 표시합니다.
- **Gem.py**: 경험치 젬을 처리합니다.
- **LevelUpUI.py**: 레벨업 UI 요소를 관리합니다.
- **Button.py** : 레벨업 UI안에 버튼을 관리합니다.



## 참고 사항
- 모든 이미지 및 사운드 파일이 코드에서 참조하는 디렉토리에 있는지 확인하세요.
- 문제나 버그가 발생하면 코드 주석을 참고하거나 개발자에게 문의하세요.

## 저자
- **개발자**: [소유진], [하윤철], [김시원], [윤의종]
- **이메일**: [https://github.com/yujin-zero] , [https://github.com/Yooncheol1], [https://github.com/huro0906],[https://github.com/Dochanii]

게임을 즐기세요!
