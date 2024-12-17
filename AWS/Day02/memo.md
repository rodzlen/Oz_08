IAM 권한이랑 접근 막는 곳 
route 에서 인터넷 외부망 연결은 0.0.0.0/0 - 모든 트래픽
ip 경로가 겹치는 경우 프리픽스이 큰 숫자를 따라간다.

중계기 - pri 와 pub 
Was NAT(중계기) 

firewall
기본적인 네트워크 차원 - security group, NAcl(network access control list), 
Stateful, Stateless  - 기존의 통신을 기억하고 있는지 유무

L4 방롸벽
- ip와 port번호로 구별

stateful - Egress, Eject(외향), ingress 허용
- Sercurity group

stateless - outbound, inbound 각자 허용 설정해줘야 통신 가능
- NACL


nat - 나가는 것만 가능

waf(web app firewall),anfw(amazon network firewall)


cbmod 400 "~~~"
change mod , no 

네트워크 상태 
1xx information
2xx Success
3xx redirect
4xx cl err
5xx server err
