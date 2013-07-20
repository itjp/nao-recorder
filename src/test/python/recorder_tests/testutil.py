'''
Created on 8 Jul 2013

@author: davesnowdon
'''


import random

from recorder.core import JOINT_NAMES


POSITION_ZERO = [ -0.004643917083740234, 0.35584592819213867, 0.10120201110839844, 0.009161949157714844,
                  - 0.21326804161071777, -0.03984212875366211, -0.009245872497558594, 0.974399983882904,
                  - 0.516916036605835, 0.27922987937927246, -1.5876480340957642, 1.236362099647522,
                  0.9225810170173645, 4.1961669921875e-05, -0.516916036605835, -0.31136012077331543,
                  - 1.5923337936401367, 1.2502517700195312, 0.9235100746154785, 4.1961669921875e-05,
                  0.07213997840881348, -0.013848066329956055, 0.45555615425109863, 0.04912996292114258,
                  0.22545599937438965, 0.9771999716758728]

POSITION_ARMS_UP = [0.11040592193603516, 0.3481760025024414, -1.5954017639160156, 0.029103994369506836,
                    - 0.598301887512207, -0.04597806930541992, 0.047512054443359375, 0.3004000186920166, -0.3251659870147705,
                    0.2654240131378174, -1.575376033782959, 1.3759560585021973, 0.8743381500244141, -0.033705949783325195,
                    - 0.3251659870147705, -0.2607381343841553, -1.5509161949157715, 1.3821759223937988, 0.8575479984283447,
                    0.04606199264526367, -1.595318078994751, 0.0060939788818359375, 0.5215179920196533, 0.0583338737487793,
                    0.8129780292510986, 0.9739999771118164]

POSITION_ARMS_OUT = [-0.018450021743774414, -0.009245872497558594, 0.05824995040893555, 1.2532360553741455, -0.42649388313293457,
                      - 1.1888080835342407, 0.047512054443359375, 0.30479997396469116, -0.6089560985565186, 0.27309393882751465, -1.579978108406067,
                      1.3820921182632446, 0.8651340007781982, -0.015298128128051758, -0.6089560985565186, -0.26534008979797363, -1.5877318382263184,
                      1.3990497589111328, 0.8560140132904053, 0.01691603660583496, 0.05526590347290039, -1.245649814605713, 0.47856616973876953,
                      1.2303099632263184, -0.0031099319458007812, 0.30720001459121704]

POSITION_ARMS_LEFT_UP_RIGHT_OUT = [-0.1043538972735405, 0.21625208854675293, -1.5969362258911133, 0.1748340129852295,
                                    - 0.11816000938415527, -1.084496021270752, -1.4082541465759277, 0.9711999893188477, -0.5000419616699219,
                                    0.29610395431518555, -1.5907161235809326, 1.4035680294036865, 0.8589980602264404, -0.04444408416748047,
                                    - 0.5000419616699219, -0.3941960334777832, -1.6000041961669922, 1.4512062072753906, 0.8314700126647949,
                                    0.06293606758117676, 0.05373191833496094, -1.2471837997436523, 0.19170808792114258, 1.1934938430786133,
                                    0.5123140811920166, 0.9735999703407288]

POSITION_ARMS_RIGHT_OUT_LEFT_FORWARD = [-0.04452800750732422, -0.013848066329956055, 0.08739614486694336, 0.022968053817749023, -0.42649388313293457, -1.1949440240859985, 0.01222991943359375, 0.30799996852874756, -0.610490083694458, 0.27616190910339355, -1.5861140489578247, 1.4035680294036865, 0.857464075088501, -0.013764142990112305, -0.610490083694458, -0.27147603034973145, -1.5846638679504395, 1.4067201614379883, 0.8468098640441895, 0.01691603660583496, 0.05373191833496094, -1.245649814605713, 0.46169209480285645, 1.2563881874084473, 0.007627964019775391, 0.30720001459121704]

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
