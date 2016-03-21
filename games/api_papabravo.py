# -*- coding: utf-8 -*-
from nGle_util import nGle_util

class papabravo():

	def __init__(self):
		self.beta_server = "http://54.169.105.64:8083"

		self.device_id = uuid.uuid4()
        self.sns_id = 800000000000000000000 + self.curNumber
        self.zinny_id = str(self.sns_id) + ".google.1"
        self.version = "CF922C78-6778-4ED4-86FB-17871233FFB7"
        self.request_friend_id = ''
        self.requestMissionInfo = ''
        self.enterStage_Idx = ''
        self.stage_list = list()


	# 최초접속 session_id와 server 정보 확인
    def login_LoginToLoginServer(self):
        strUrl = ('/Login/LoginToLoginServer')

        strBody=[NVPair('msg','{"device":"%s","phoneos":"2", "phonenumber":"010-000-0000"}' % self.device_id)]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "login_LoginToLoginServer", None, sleeptime)
        loginServer = self.trim_result(result.getText().encode('utf-8'),'Data')
        self.session_id = loginServer['session_id']
    
    # Nzine 처음 접속 프로토콜 기존유저인지 유무를 알려줌
    def login_NZIN_LoginToLoginServer(self, sleeptime):
        strUrl = ('/Login/NZIN_LoginToLoginServer')
        strBody = [NVPair('msg','{"zinnyuid":"%s","version":"%s"}' % (self.zinny_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "login_NZIN_LoginToLoginServer", None, sleeptime)
        
    # Nzine 처음 접속 프로토콜 기존유저인지 유무를 알려줌
    def login_NZIN_Neobazar_SelectSNS(self, sleeptime):
        strUrl = ('/Login/NZIN_Neobazar_SelectSNS')
        strBody=[NVPair('msg','{"device":"%s","phoneos":"2","phonenumber":"0","version":"%s","zinnyuid":"%s","snsid":"%s","snstype":"2","snsprofile":""}' % (self.device_id, self.version, self.zinny_id, self.sns_id))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "login_LoginToLoginServer", self.zinny_id, sleeptime)
        loginServer = self.trim_result(result.getText().encode('utf-8'),'Data')
        self.session_id = loginServer['session_id']
        
    # 게임 프로토콜 버전 체크
    def login_Version(self, sleeptime):
        strUrl = ('/Login/Version')
        strBody=[NVPair('msg','{"version":"%s"}' % self.version)]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "login_Version", None, sleeptime)

    # 유저 정보 요청
    def lobby_RequestUser(self, sleeptime):
        strUrl = ('/Lobby/RequestUser')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "lobby_RequestUser", None, sleeptime)
        
        user_Info = self.trim_result(result.getText().encode('utf-8'),'Data')
        self.user_NickName = user_Info['NickName']
        self.user_Tutorial = user_Info['TutorialProgress']
        
        #for obj in user_Info:
        #   print "user_Info[%s] : %s" % (obj, user_Info[obj])
        
    # 닉네임 생성
    def login_CreateNickName(self, sleeptime):
        if self.user_NickName in ("", "noname"):
            strUrl = ('/Login/CreateNickName')
            strBody=[NVPair('msg','{"session_id":"%s","version":"%s","nickname":"T-%s","national":"1"}' % (self.session_id, self.version, str(self.device_id)[0:8]))]
            result = request1.POST(strUrl, strBody, strHeader)
            self.checkResponse(result, 200, "login_CreateNickName", None, sleeptime)
        
    # 캐릭터 인벤토리 요청
    def lobby_RequestCharacterInventory(self, sleeptime):
        strUrl = ('/Lobby/RequestCharacterInventory')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "lobby_RequestCharacterInventory", None, sleeptime)

    # 무기 인벤토리 요청
    def lobby_RequestWeaponInventory(self, sleeptime):
        strUrl = ('/Lobby/RequestWeaponInventory')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "lobby_RequestWeaponInventory", None, sleeptime)

    # 일반 아이템 인벤토리 요청
    def lobby_RequestSubItemInventory(self, sleeptime):
        strUrl = ('/Lobby/RequestSubItemInventory')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "lobby_RequestSubItemInventory", None, sleeptime)
        
    # 튜토리얼 완료 (step은 1이상 14 미만)
    def tutorial_RequestUpdateTutorial(self, sleeptime):
        if self.user_Tutorial < 14:
            strUrl = ('/Tutorial/RequestUpdateTutorial')
            strBody=[NVPair('msg','{"session_id":"%s","version":"%s", "step":"%s"}' % (self.session_id, self.version, self.user_Tutorial))]
            result = request1.POST(strUrl, strBody, strHeader)
            self.checkResponse(result, 200, "tutorial_RequestUpdateTutorial", None, sleeptime)

    # 친구 리스트 요청
    def friend_RequestFriendList(self, sleeptime):
        strUrl = ('/Friend/RequestFriendList')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "friend_RequestFriendList", None, sleeptime)
        
    # 친구 추천 (랜덤 10명)
    def friend_Recommend(self, sleeptime):
        strUrl = ('/Friend/Recommend')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "friend_Recommend", None, sleeptime)
        friend_Recommend_list = self.trim_result(result.getText().encode('utf-8'),'Data')
        r_counter = 0
        for obj in friend_Recommend_list:
            if r_counter == 0:
                self.request_friend_id = obj['UserUID']
            else:
                break

    # 친구 요청 (랜덤 1명 요청)
    def friend_RequestFriend(self, sleeptime):
        if self.request_friend_id != '':
            strUrl = ('/Friend/RequestFriend')
            strBody=[NVPair('msg','{"session_id":"%s","version":"%s","frienduid":"%s"}' % (self.session_id, self.version, self.request_friend_id))]
            result = request1.POST(strUrl, strBody, strHeader)
            self.checkResponse(result, 200, "friend_RequestFriend", None, sleeptime)
        
    # 로비 정보 요청
    def lobby_RequestLobby(self, sleeptime):
        strUrl = ('/Lobby/RequestLobby')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "lobby_RequestLobby", None, sleeptime)
    
    # 출석보상 리스트 요청
    def attendanceReward_RequestAttendanceRewardList(self, sleeptime):
        strUrl = ('/AttendanceReward/RequestAttendanceRewardList')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "attendanceReward_RequestAttendanceRewardList", None, sleeptime)
    
    # 출석보상 받는지 여부 체크
    def attendanceReward_RequestAttendance(self, sleeptime):
        strUrl = ('/AttendanceReward/RequestAttendanceRewardList')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "attendanceReward_RequestAttendance", None, sleeptime)
    
    # 사용자 상점 리스트 호출 (category : 1(일반상점), 2(PvP상점), 3(도전모드상점), 4(클랜상점))
    def lobby_RequestUserShopList(self, sleeptime, shop_category):
        strUrl = ('/Lobby/RequestUserShopList')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s","category":"%s"}' % (self.session_id, self.version, shop_category))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "lobby_RequestUserShopList", None, sleeptime)
        
    # 유저의 미션 리스트 진행상황 조회
    def mission_RequestMissionList(self, sleeptime):
        strUrl = ('/Mission/RequestMissionList')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "mission_RequestMissionList", None, sleeptime)
        RequestMission_List = self.trim_result(result.getText().encode('utf-8'),'Data')
        r_counter = 0
        for obj in RequestMission_List:
            if r_counter == 0:
                if obj['State'] == 2:
                    self.reward_mission = obj['Idx']
            else:
                break
                
    # 미션 보상 받기
    def mission_GetReward(self, sleeptime):
        if self.reward_mission:
            strUrl = ('/Mission/GetReward')
            strBody=[NVPair('msg','{"session_id":"%s","version":"%s","missionidx":"%s"}' % (self.session_id, self.version, self.reward_mission))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "mission_GetReward", self.reward_mission, sleeptime)
    
    # 미션 진행상황 조회
    def mission_RequestMissionInfo(self, sleeptime):
        if self.requestMissionInfo != '':
            strUrl = ('/Mission/RequestMissionInfo')
            strBody=[NVPair('msg','{"session_id":"%s","version":"%s","missionidx":"%s"}' % (self.session_id, self.version, self.requestMissionInfo))]
            result = request1.POST(strUrl, strBody, strHeader)
            self.checkResponse(result, 200, "mission_RequestMissionInfo", None, sleeptime)
    
    # 전체 스테이지 정보 요청
    def stage_RequestStageInfo(self, sleeptime):
        strUrl = ('/Stage/RequestStageInfo')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "stage_RequestStageInfo", None, sleeptime)
        Stage_Info = self.trim_result(result.getText().encode('utf-8'),'Data')
        # Make Stage List
        if len(self.stage_list) == 0:
            for obj in Stage_Info:
                self.stage_list.append(obj['StageIdx'])

    # 인게임 들어가기 전에 들어갈 수 있는지 체크하는 프로토콜
    def stage_RequestEnterStage(self, sleeptime):
        self.stage_RequestStageInfo(100)
        self.enterStage_Idx = max(self.stage_list)

        if self.enterStage_Idx != "":
            strUrl = ('/Stage/RequestEnterStage')
            strBody=[NVPair('msg','{"session_id":"%s","version":"%s","idx":"%s","frienduid":""}' % (self.session_id, self.version, self.enterStage_Idx))]
            result = request1.POST(strUrl, strBody, strHeader)
            self.checkResponse(result, 200, "stage_RequestEnterStage", self.enterStage_Idx, sleeptime)
            enterStage_Info = self.trim_result(result.getText().encode('utf-8'), 'Data')
    
    # 스테이지 클리어
    def stage_ClearStage(self, sleeptime):
        strUrl = ('/Stage/ClearStage')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s","stageidx":"%s","mission1clear":"1","mission2clear":"1","mission3clear":"1","usedslot1":"0","usedslot2":"0","usedslot3":"0","iswin":"1"}' % (self.session_id, self.version, self.enterStage_Idx))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "stage_ClearStage", self.enterStage_Idx, sleeptime)
    
    
    # 메일 리스트 요청
    def mail_RequestMailList(self, sleeptime):
        strUrl = ('/Mail/RequestMailList')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "mail_RequestMailList", None, sleeptime)
    
    # 나의 랭킹정보, 나의 전시즌 랭킹정보, 전체 (1~ 30위) 랭킹 정보
    def rank_TotalRanking(self, sleeptime):
        strUrl = ('/Rank/TotalRanking')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "rank_TotalRanking", None, sleeptime)
    
    # shop_FreeLotteryCheck
    def shop_FreeLotteryCheck(self, sleeptime):
        strUrl = ('/Shop/FreeLotteryCheck')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "shop_FreeLotteryCheck", None, sleeptime)
    
    # 인게임 상점 요청
    def lobby_RequestInGameShop(self, sleeptime):
        strUrl = ('/Lobby/RequestInGameShop')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "lobby_RequestInGameShop", None, sleeptime)
        
    # 도전모드에서 필요한 정보를 요청
    def lobby_RequestChallenge(self, sleeptime):
        strUrl = ('/Lobby/RequestChallenge')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s"}' % (self.session_id, self.version))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "lobby_RequestChallenge", None, sleeptime)
    
    # 도전모드 들어가기 전에 들어갈수 있는지 체크하는 프로토콜
    def stage_RequestEnterChallenge(self, sleeptime, stageidx):
        strUrl = ('/Stage/RequestEnterChallenge')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s","stageidx":"%s"}' % (self.session_id, self.version, stageidx))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "stage_RequestEnterChallenge", None, sleeptime)
    
    # 도전모드 보상처리
    def stage_ClearChallenge(self, sleeptime, stageidx, iswin, cleartime):
        strUrl = ('/Stage/ClearChallenge')
        strBody=[NVPair('msg','{"session_id":"%s","version":"%s","stageidx":"%s","usedslot1":"0","usedslot2":"0","usedslot3":"0","iswin":"%s","cleartime":"%s"}' % (self.session_id, self.version, stageidx, iswin, cleartime))]
        result = request1.POST(strUrl, strBody, strHeader)
        self.checkResponse(result, 200, "stage_ClearChallenge", None, sleeptime)