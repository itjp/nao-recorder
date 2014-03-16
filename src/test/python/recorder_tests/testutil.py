'''
Created on 8 Jul 2013

@author: davesnowdon
'''

import random

from recorder.core import JOINT_NAMES

# arms
POSITION_ZERO = [ -0.004643917083740234, 0.35584592819213867, 0.10120201110839844, 0.009161949157714844, -0.21326804161071777, -0.03984212875366211, -0.009245872497558594, 0.974399983882904, -0.516916036605835, 0.27922987937927246, -1.5876480340957642, 1.236362099647522, 0.9225810170173645, 4.1961669921875e-05, -0.516916036605835, -0.31136012077331543, -1.5923337936401367, 1.2502517700195312, 0.9235100746154785, 4.1961669921875e-05, 0.07213997840881348, -0.013848066329956055, 0.45555615425109863, 0.04912996292114258, 0.22545599937438965, 0.9771999716758728]
POSITION_ARMS_UP = [0.11040592193603516, 0.3481760025024414, -1.5954017639160156, 0.029103994369506836, -0.598301887512207, -0.04597806930541992, 0.047512054443359375, 0.3004000186920166, -0.3251659870147705, 0.2654240131378174, -1.575376033782959, 1.3759560585021973, 0.8743381500244141, -0.033705949783325195, -0.3251659870147705, -0.2607381343841553, -1.5509161949157715, 1.3821759223937988, 0.8575479984283447, 0.04606199264526367, -1.595318078994751, 0.0060939788818359375, 0.5215179920196533, 0.0583338737487793, 0.8129780292510986, 0.9739999771118164]
POSITION_ARMS_OUT = [-0.018450021743774414, -0.009245872497558594, 0.05824995040893555, 1.2532360553741455, -0.42649388313293457, -1.1888080835342407, 0.047512054443359375, 0.30479997396469116, -0.6089560985565186, 0.27309393882751465, -1.579978108406067, 1.3820921182632446, 0.8651340007781982, -0.015298128128051758, -0.6089560985565186, -0.26534008979797363, -1.5877318382263184, 1.3990497589111328, 0.8560140132904053, 0.01691603660583496, 0.05526590347290039, -1.245649814605713, 0.47856616973876953, 1.2303099632263184, -0.0031099319458007812, 0.30720001459121704]
POSITION_ARMS_DOWN = [0.0060939788818359375, 0.1288139820098877, 1.592250108718872, 0.12114405632019043, -1.3775739669799805, -0.038308143615722656, 0.15335798263549805, 0.9395999908447266, -0.23466014862060547, -0.052114009857177734, -0.7148020267486572, 2.112546443939209, -1.1894419193267822, 0.07980990409851074, -0.23466014862060547, 0.07213997840881348, -0.6611959934234619, 2.112546443939209, -1.186300277709961, -0.10426998138427734, 1.5954017639160156, -0.12122797966003418, 1.4649280309677124, 0.05526590347290039, -0.1795198917388916, 0.09599995613098145]
POSITION_ARMS_BACK = [0.0060939788818359375, 0.12727999687194824, 2.035576105117798, -0.004643917083740234, -1.3775739669799805, -0.06131792068481445, 0.15335798263549805, 0.9395999908447266, -0.23619413375854492, -0.052114009857177734, -0.7132680416107178, 2.112546443939209, -1.1894419193267822, 0.07520794868469238, -0.23619413375854492, 0.07213997840881348, -0.6596620082855225, 2.112546443939209, -1.1857401132583618, -0.07512402534484863, 2.040262222290039, -0.010779857635498047, 1.4664621353149414, 0.0813438892364502, -0.1795198917388916, 0.09599995613098145]
POSITION_ARMS_LEFT_UP_RIGHT_OUT = [-0.1043538972735405, 0.21625208854675293, -1.5969362258911133, 0.1748340129852295, -0.11816000938415527, -1.084496021270752, -1.4082541465759277, 0.9711999893188477, -0.5000419616699219, 0.29610395431518555, -1.5907161235809326, 1.4035680294036865, 0.8589980602264404, -0.04444408416748047, -0.5000419616699219, -0.3941960334777832, -1.6000041961669922, 1.4512062072753906, 0.8314700126647949, 0.06293606758117676, 0.05373191833496094, -1.2471837997436523, 0.19170808792114258, 1.1934938430786133, 0.5123140811920166, 0.9735999703407288]
POSITION_ARMS_RIGHT_UP_LEFT_OUT = [-0.009245872497558594, 0.14415407180786133, 0.05518198013305664, 1.2501680850982666, -0.7639739513397217, -1.0783600807189941, 0.1349501609802246, 0.009600043296813965, -0.25, -0.07972598075866699, -0.6994619369506836, 2.112546443939209, -1.1812219619750977, 0.07520794868469238, -0.25, 0.07980990409851074, -0.6995458602905273, 2.112546443939209, -1.1796040534973145, -0.07512402534484863, -1.5692400932312012, 0.004559993743896484, 0.7792301177978516, 1.0861139297485352, -0.1365680694580078, 0.009600043296813965]
POSITION_ARMS_LEFT_FORWARD_RIGHT_DOWN = [-0.009245872497558594, 0.14415407180786133, 0.06592011451721191, 0.01683211326599121, -0.7701098918914795, -1.0568840503692627, 0.13801813125610352, 0.9663999676704407, -0.24846601486206055, -0.07512402534484863, -0.704064130783081, 2.112276077270508, -1.1894419193267822, 0.07520794868469238, -0.24846601486206055, 0.07980990409851074, -0.6980118751525879, 2.112546443939209, -1.186300277709961, -0.07665801048278809, 1.4818859100341797, 0.009161949157714844, 0.7822980880737305, 1.0953178405761719, -0.13810205459594727, 0.040400028228759766]
POSITION_ARMS_RIGHT_FORWARD_LEFT_DOWN = [-0.009245872497558594, 0.14568805694580078, 1.483336091041565, -4.1961669921875e-05, -0.8007900714874268, -1.0921659469604492, 0.13801813125610352, 0.9663999676704407, -0.24846601486206055, -0.07512402534484863, -0.704064130783081, 2.112546443939209, -1.1894419193267822, 0.07520794868469238, -0.24846601486206055, 0.07980990409851074, -0.6980118751525879, 2.112546443939209, -1.186300277709961, -0.07512402534484863, 0.07213997840881348, 0.009161949157714844, 0.7562201023101807, 1.0600361824035645, -0.13810205459594727, 0.040400028228759766]
POSITION_ARMS_RIGHT_DOWN_LEFT_BACK = [-0.009245872497558594, 0.14415407180786133, 2.035576105117798, -0.0031099319458007812, -0.7793140411376953, -0.047512054443359375, 0.13648414611816406, 0.04200005531311035, -0.24846601486206055, -0.07359004020690918, -0.7132680416107178, 2.112546443939209, -1.1894419193267822, 0.07520794868469238, -0.24846601486206055, 0.07827591896057129, -0.7041480541229248, 2.112546443939209, -1.1857401132583618, -0.07665801048278809, 1.586197853088379, -0.12889790534973145, 0.7792301177978516, 0.04606199264526367, -0.13810205459594727, 0.04159998893737793]
POSITION_ARMS_LEFT_DOWN_RIGHT_BACK = [-0.009245872497558594, 0.14415407180786133, 1.6321340799331665, 0.08739614486694336, -0.7701098918914795, -0.04597806930541992, 0.1349501609802246, 0.04200005531311035, -0.24846601486206055, -0.07359004020690918, -0.7132680416107178, 2.112546443939209, -1.1894419193267822, 0.07520794868469238, -0.24846601486206055, 0.07827591896057129, -0.7041480541229248, 2.112546443939209, -1.1857401132583618, -0.07512402534484863, 2.0387282371520996, -0.0031099319458007812, 0.7776961326599121, 0.05373191833496094, -0.13810205459594727, 0.04159998893737793]

# hands
POSITION_HANDS_CLOSE = [-0.0031099319458007812, 0.13341593742370605, 1.4357820749282837, 0.13801813125610352, -0.0061779022216796875, -0.03984212875366211, 0.15949392318725586, 0.009600043296813965, -0.23466014862060547, -0.06745409965515137, -0.7163360118865967, 2.112546443939209, -1.1894419193267822, 0.07520794868469238, -0.23466014862060547, 0.07980990409851074, -0.7056820392608643, 2.112546443939209, -1.1857401132583618, -0.07665801048278809, 1.5677900314331055, -0.10281991958618164, 0.0060939788818359375, 0.04606199264526367, 0.42947816848754883, 0.009600043296813965]
POSITION_HANDS_OPEN = [-0.0031099319458007812, 0.13341593742370605, 1.4342480897903442, 0.13801813125610352, -0.0061779022216796875, -0.03984212875366211, 0.15949392318725586, 0.9739999771118164, -0.23466014862060547, -0.06745409965515137, -0.7163360118865967, 2.112546443939209, -1.1894419193267822, 0.07520794868469238, -0.23466014862060547, 0.07980990409851074, -0.7056820392608643, 2.112546443939209, -1.1857401132583618, -0.07665801048278809, 1.5677900314331055, -0.10128592699766159, 0.0060939788818359375, 0.04606199264526367, 0.42947816848754883, 0.9771999716758728]
POSITION_HANDS_RIGHT_OPEN_LEFT_CLOSE = [-0.0031099319458007812, 0.13341593742370605, 1.4357820749282837, 0.13801813125610352, -0.0061779022216796875, -0.03984212875366211, 0.15949392318725586, 0.009999990463256836, -0.23466014862060547, -0.06745409965515137, -0.7163360118865967, 2.112546443939209, -1.1894419193267822, 0.07520794868469238, -0.23466014862060547, 0.07980990409851074, -0.7056820392608643, 2.112546443939209, -1.1857401132583618, -0.07665801048278809, 1.5677900314331055, -0.10128592699766159, 0.0060939788818359375, 0.04606199264526367, 0.4279439449310303, 0.9771999716758728]
POSITION_HANDS_LEFT_OPEN_RIGHT_CLOSE = [-0.0031099319458007812, 0.13341593742370605, 1.4342480897903442, 0.13648414611816406, -0.0061779022216796875, -0.03984212875366211, 0.15949392318725586, 0.9739999771118164, -0.23466014862060547, -0.06745409965515137, -0.7163360118865967, 2.112546443939209, -1.1894419193267822, 0.07520794868469238, -0.23466014862060547, 0.07980990409851074, -0.7056820392608643, 2.112546443939209, -1.186300277709961, -0.07665801048278809, 1.5677900314331055, -0.10128592699766159, 0.007627964019775391, 0.04606199264526367, 0.42947816848754883, 0.011199951171875]

# elbows
POSITION_ELBOWS_STRAIGHT_TURN_IN = [-0.02611994743347168, 0.17330002784729004, 0.08125996589660645, 0.007627964019775391, -0.010779857635498047, -0.0367741584777832, -1.5708580017089844, 0.885200023651123, -0.49390602111816406, 0.5139319896697998, -1.6075900793075562, 1.4710640907287598, 0.8405900001525879, -0.056715965270996094, -0.49390602111816406, -0.19170808792114258, -1.563188076019287, 1.3438258171081543, 0.8836259841918945, -0.03217196464538574, 0.0844118595123291, 0.009161949157714844, 0.010695934295654297, 0.04606199264526367, 1.1964781284332275, 0.026399970054626465]
POSITION_ELBOWS_BENT_TURN_UP = [-0.02611994743347168, 0.17176604270935059, 0.052114009857177734, -4.1961669921875e-05, -1.5570521354675293, -1.5446163415908813, -1.5708580017089844, 0.8847999572753906, -0.4570901393890381, 0.5139319896697998, -1.6167941093444824, 1.4618600606918335, 0.8421239852905273, -0.05518198013305664, -0.4570901393890381, -0.19170808792114258, -1.5723919868469238, 1.3376898765563965, 0.8897619247436523, -0.022968053817749023, 0.05373191833496094, -0.023051977157592773, 1.556968092918396, 1.5187020301818848, 1.3774900436401367, 0.972000002861023]
POSITION_ELBOWS_STRAIGHT_TURN_DOWN = [-0.0061779022216796875, 0.2039799690246582, 0.05364799499511719, 0.018366098403930664, 1.5707966089248657, -0.03490659222006798, 0.027570009231567383, 0.04079997539520264, 0.027653932571411133, -0.013764142990112305, 0.08901405334472656, -0.01691603660583496, -0.0031099319458007812, 0.0061779022216796875, 0.027653932571411133, 4.1961669921875e-05, 0.1088719367980957, -0.02143406867980957, -0.0060939788818359375, -0.007627964019775391, -0.024502038955688477, 0.004559993743896484, -1.5707966089248657, 0.03490658476948738, 0.03063797950744629, 0.02240002155303955]

# wrists
POSITION_WRISTS_CENTER = [-0.009245872497558594, 0.13801813125610352, 0.14108610153198242, 0.019900083541870117, -0.009245872497558594, -0.042910099029541016, -0.024585962295532227, 0.9711999893188477, -0.28067994117736816, -0.06745409965515137, -0.7531521320343018, 2.112546443939209, -1.1894419193267822, 0.07520794868469238, -0.28067994117736816, 0.0813438892364502, -0.7501680850982666, 2.112546443939209, -1.186300277709961, -0.07512402534484863, 0.08901405334472656, -0.01691603660583496, 0.010695934295654297, 0.0614018440246582, 0.024502038955688477, 0.9739999771118164]
POSITION_WRISTS_TURN_IN = [-0.007711887359619141, 0.13801813125610352, 0.14108610153198242, 0.019900083541870117, -0.009245872497558594, -0.042910099029541016, -1.540177822113037, 0.9711999893188477, -0.28067994117736816, -0.06745409965515137, -0.7531521320343018, 2.112276077270508, -1.1894419193267822, 0.07520794868469238, -0.28067994117736816, 0.0813438892364502, -0.7501680850982666, 2.112546443939209, -1.186300277709961, -0.07665801048278809, 0.08901405334472656, -0.01691603660583496, 0.010695934295654297, 0.0614018440246582, 1.5278220176696777, 0.9739999771118164]
POSITION_WRISTS_TURN_OUT = [-0.007711887359619141, 0.13801813125610352, 0.14108610153198242, 0.019900083541870117, -0.009245872497558594, -0.042910099029541016, 1.552366018295288, 0.9711999893188477, -0.28067994117736816, -0.06745409965515137, -0.7531521320343018, 2.112546443939209, -1.1894419193267822, 0.07520794868469238, -0.28067994117736816, 0.0813438892364502, -0.7501680850982666, 2.112546443939209, -1.186300277709961, -0.07512402534484863, 0.09054803848266602, -0.01691603660583496, 0.010695934295654297, 0.0614018440246582, -1.5371098518371582, 0.9739999771118164]
POSITION_WRISTS_RIGHT_CENTER_LEFT_TURN_OUT = [-0.007711887359619141, 0.13801813125610352, 1.4143060445785522, 0.13801813125610352, 0.019900083541870117, -0.0367741584777832, 1.5477640628814697, 0.97079998254776, -0.2868161201477051, -0.06285214424133301, -0.7117340564727783, 2.112546443939209, -1.1894419193267822, 0.07520794868469238, -0.2868161201477051, 0.0813438892364502, -0.6980118751525879, 2.112546443939209, -1.186300277709961, -0.07512402534484863, 1.4650120735168457, -0.12429594993591309, -0.047595977783203125, 0.0583338737487793, 0.022968053817749023, 0.9739999771118164]
POSITION_WRISTS_RIGHT_TURN_IN_LEFT_CENTER = [-0.007711887359619141, 0.13801813125610352, 1.4143060445785522, 0.13801813125610352, 0.019900083541870117, -0.038308143615722656, -0.018450021743774414, 0.97079998254776, -0.2868161201477051, -0.06285214424133301, -0.7117340564727783, 2.112546443939209, -1.1894419193267822, 0.07520794868469238, -0.2868161201477051, 0.0813438892364502, -0.6980118751525879, 2.112546443939209, -1.186300277709961, -0.07512402534484863, 1.4650120735168457, -0.12429594993591309, -0.04912996292114258, 0.0583338737487793, 1.5308901071548462, 0.9739999771118164]

# head
POSITION_HEAD_DOWN_HEAD_FORWARD = [-0.009245872497558594, 0.4524879455566406, 0.9065520763397217, 0.2039799690246582, -0.4418339729309082, -1.2072160243988037, 0.01683211326599121, 0.3068000078201294, -0.5951499938964844, 0.27616190910339355, -1.5738420486450195, 1.3928301334381104, 0.8682019710540771, -0.01222991943359375, -0.5951499938964844, -0.26840806007385254, -1.5739259719848633, 1.4036521911621094, 0.8514120578765869, 0.01691603660583496, 0.9710640907287598, -0.26389002799987793, 0.48163414001464844, 1.2533202171325684, -0.04452800750732422, 0.30080002546310425]
POSITION_HEAD_UP_HEAD_RIGHT = [-1.5355758666992188, -0.3835420608520508, 0.9065520763397217, 0.2039799690246582, -0.4418339729309082, -1.2056820392608643, 0.01683211326599121, 0.3068000078201294, -0.5951499938964844, 0.27616190910339355, -1.5738420486450195, 1.3928301334381104, 0.8682019710540771, -0.01222991943359375, -0.5951499938964844, -0.26840806007385254, -1.5739259719848633, 1.4036521911621094, 0.8514120578765869, 0.01691603660583496, 0.9710640907287598, -0.2654240131378174, 0.48163414001464844, 1.251786231994629, -0.04452800750732422, 0.30080002546310425]
POSITION_HEAD_CENTER_HEAD_LEFT = [1.552366018295288, 0.038308143615722656, 0.9065520763397217, 0.2039799690246582, -0.4418339729309082, -1.2056820392608643, 0.01683211326599121, 0.3068000078201294, -0.5951499938964844, 0.27616190910339355, -1.5738420486450195, 1.3928301334381104, 0.8682019710540771, -0.01222991943359375, -0.5951499938964844, -0.26840806007385254, -1.5739259719848633, 1.4036521911621094, 0.8514120578765869, 0.01691603660583496, 0.9710640907287598, -0.26389002799987793, 0.48163414001464844, 1.2502517700195312, -0.04452800750732422, 0.30080002546310425]

# feet
POSITION_FEET_POINT_TOES = [-0.0031099319458007812, 0.21165013313293457, 1.9266620874404907, 0.027570009231567383, -1.251786231994629, -1.2762460708618164, -1.7794818878173828, 0.9711999893188477, 0.04912996292114258, -0.27761197090148926, 0.21020007133483887, -0.09232791513204575, 0.9218921661376953, 4.1961669921875e-05, 0.04912996292114258, -0.3451080322265625, 0.25, -0.09232791513204575, 0.9219760894775391, -0.05058002471923828, 1.9727659225463867, -0.02151799201965332, 1.1704000234603882, 1.4880218505859375, 0.22238802909851074, 0.3059999942779541]
POSITION_FEET_RAISE_TOES = [-0.0031099319458007812, 0.21011614799499512, 1.9251281023025513, 0.027570009231567383, -1.2502517700195312, -1.274712085723877, -1.7794818878173828, 0.9711999893188477, 0.04912996292114258, -0.2760779857635498, 0.21020007133483887, -0.09208202362060547, -1.1894419193267822, -0.010695934295654297, 0.04912996292114258, -0.3451080322265625, 0.25, -0.09232791513204575, -1.186300277709961, -0.07665801048278809, 1.9727659225463867, -0.02151799201965332, 1.1704000234603882, 1.4880218505859375, 0.22238802909851074, 0.3059999942779541]
POSITION_FEET_TURN_OUT = [-0.0031099319458007812, 0.21011614799499512, 1.9251281023025513, 0.027570009231567383, -1.251786231994629, -1.2762460708618164, -1.7794818878173828, 0.9711999893188477, 0.04912996292114258, -0.27761197090148926, 0.21020007133483887, -0.09208202362060547, -0.13963603973388672, 0.3835420608520508, 0.04912996292114258, -0.3451080322265625, 0.25, -0.09232791513204575, -0.13955211639404297, -0.38345813751220703, 1.9727659225463867, -0.02151799201965332, 1.1704000234603882, 1.4880218505859375, 0.22238802909851074, 0.3059999942779541]
POSITION_FEET_TURN_IN = [-0.0031099319458007812, 0.21165013313293457, 1.9266620874404907, 0.027570009231567383, -1.251786231994629, -1.2762460708618164, -1.7794818878173828, 0.9711999893188477, 0.04912996292114258, -0.27761197090148926, 0.21020007133483887, -0.09208202362060547, -0.13963603973388672, -0.3972640037536621, 0.04912996292114258, -0.3451080322265625, 0.25, -0.09232791513204575, -0.13955211639404297, 0.38814401626586914, 1.9727659225463867, -0.02151799201965332, 1.1704000234603882, 1.4880218505859375, 0.22238802909851074, 0.3059999942779541]
POSITION_FEET_CENTER = [-0.0031099319458007812, 0.21011614799499512, 1.9251281023025513, 0.027570009231567383, -1.2502517700195312, -1.274712085723877, -1.7794818878173828, 0.9711999893188477, 0.04912996292114258, -0.27761197090148926, 0.21020007133483887, -0.09208202362060547, -4.1961669921875e-05, 4.1961669921875e-05, 0.04912996292114258, -0.3451080322265625, 0.25, -0.09232791513204575, 4.1961669921875e-05, 4.1961669921875e-05, 1.9727659225463867, -0.02151799201965332, 1.1704000234603882, 1.4880218505859375, 0.22238802909851074, 0.3059999942779541]

# legs
POSITION_LEGS_LEFT_FORWARD_RIGHT_IN = [-0.02611994743347168, 0.18710613250732422, 1.9021180868148804, 0.17943596839904785, -1.3714380264282227, -0.3573801517486572, -1.6153440475463867, 0.9711999893188477, -0.1088719367980957, 0.004643917083740234, -0.8728041648864746, -0.09208202362060547, -0.052197933197021484, 0.042994022369384766, -0.1088719367980957, 0.018450021743774414, 0.2561359405517578, -0.09232791513204575, -0.0030260086059570312, -0.1058039665222168, 1.8976001739501953, -0.07213997840881348, 1.6750860214233398, 0.3007059097290039, 1.579978108406067, 0.30720001459121704]
POSITION_LEGS_RIGHT_FORWARD_LEFT_IN = [-0.02611994743347168, 0.18710613250732422, 1.9021180868148804, 0.17943596839904785, -1.3714380264282227, -0.3589141368865967, -1.6153440475463867, 0.9715999960899353, -0.08893013000488281, 0.0061779022216796875, 0.16264605522155762, 0.0060939788818359375, -0.052197933197021484, 0.042994022369384766, -0.08893013000488281, 0.018450021743774414, -0.8728880882263184, -0.09232791513204575, -0.0030260086059570312, -0.1058039665222168, 1.8991341590881348, -0.07367396354675293, 1.6750860214233398, 0.3007059097290039, 1.579978108406067, 0.30720001459121704]
POSITION_LEGS_LEFT_OUT_RIGHT_IN = [-0.007711887359619141, 0.18710613250732422, 1.6750860214233398, 0.04597806930541992, -0.8437418937683105, -1.5232200622558594, -1.5033621788024902, 0.97079998254776, -0.06131792068481445, 0.6121079921722412, 0.0031099319458007812, 0.013764142990112305, -0.052197933197021484, 0.042994022369384766, -0.06131792068481445, 4.1961669921875e-05, 0.2239220142364502, -0.09232791513204575, -0.010695934295654297, -0.1058039665222168, 1.8976001739501953, -0.07827591896057129, 1.6428720951080322, 0.3068418502807617, 1.579978108406067, 0.30720001459121704]
POSITION_LEGS_RIGHT_OUT_LEFT_IN = [-0.024585962295532227, 0.18864011764526367, 1.9036520719528198, 0.18250393867492676, -1.3714380264282227, -0.36044812202453613, -1.6153440475463867, 0.9715999960899353, -0.06898808479309082, 0.0061779022216796875, 0.1365680694580078, 0.022968053817749023, -0.052197933197021484, 0.042994022369384766, -0.06898808479309082, -0.610490083694458, 0.0014920234680175781, -0.09232791513204575, -0.0014920234680175781, -0.1058039665222168, 1.850046157836914, -0.06600403785705566, 0.9740481376647949, 1.5417118072509766, 1.5815120935440063, 0.30720001459121704]

def make_joint_dict(angles):
    result = {}
    for n, v in zip(JOINT_NAMES, angles):
        result[n] = v
    return result

def make_random_joints():
    result = {}
    for n in JOINT_NAMES:
        result[n] = random.random()
    return result
