from Crypto.Util.number import *
from secret import flag

m1 = bytes_to_long(flag[:len(flag)//3])
m2 = bytes_to_long(flag[len(flag)//3:])

def gen():
    prime_list  = []
    for i in range(4):
        prime_list.append(getPrime(512))
    return sorted(prime_list)

prime_list = gen()
p,q,r,t = prime_list[0],prime_list[3],prime_list[1],prime_list[2]
e = 65537
n = p*q*r*t
phi = (p-1)*(q-1)*(r-1)*(t-1)
c1 = pow(m1,e,p*q)
p1 = getPrime(512)
q1 = getPrime(512)
N = p1*q1
c2 = pow(m2,p1,N)
c3 = pow(m2,q1,N)
print(f'n = {n}')
print(f'phi = {phi}')
print(f'c1 = {c1}')
print(f'N = {N}')
print(f'c2 = {c2}')
print(f'c3 = {c3}')

'''
n = 8836130216343708623415307573630337110573363595188748983290313549413242332143945452914800845282478216810685733227137911630239808895196748125078747600505626165666334675100147790578546682128517668100858766784733351894480181877144793496927464058323582165412552970999921215333509253052644024478417393146000490808639363681195799826541558906527985336104761974023394438549055804234997654701266967731137282297623426318212701157416397999108259257077847307874122736921265599854976855949680133804464839768470200425669609996841568545945133611190979810786943246285103031363790663362165522662820344917056587244701635831061853354597
phi = 8836130216343708623415307573630337110573363595188748983290313549413242332143945452914800845282478216810685733227137911630239808895196748125078747600505622503351461565956106005118029537938273153581675065762015952483687057805462728186901563990429998916382820576211887477098611684072561849314986341226981300596338314989867731725668312057134075244816223120038573374383949718714549930261073576391501671722900294331289082826058292599838631513746370889828026039555245672195833927609280773258978856664434349221972568651378808050580665443131001632395175205804045958846124475183825589672204752895252723130454951830966138888560
c1 = 78327207863361017953496121356221173288422862370301396867341957979087627011991738176024643637029313969241151622985226595093079857523487726626882109114134910056673489916408854152274726721451884257677533593174371742411008169082367666168983943358876017521749198218529804830864940274185360506199116451280975188409
N = 157202814866563156513184271957553223260772141845129283711146204376449001653397810781717934720804041916333174673656579086498762693983380365527400604554663873045166444369504886603233275868192688995284322277504050322927511160583280269073338415758019142878016084536129741435221345599028001581385308324407324725353
c2 = 63355788175487221030596314921407476078592001060627033831694843409637965350474955727383434406640075122932939559532216639739294413008164038257338675094324172634789610307227365830016457714456293397466445820352804725466971828172010276387616894829328491068298742711984800900411277550023220538443014162710037992032
c3 = 9266334096866207047544089419994475379619964393206968260875878305040712629590906330073542575719856965053269812924808810766674072615270535207284077081944428011398767330973702305174973148018082513467080087706443512285098600431136743009829009567065760786940706627087366702015319792328141978938111501345426931078
'''
