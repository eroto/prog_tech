import unittest
from functools import reduce
from itertools import chain
from fp import MyMonad, get_PushEvent_msgs, filter_PushEvents, tokenize

data = [{'id': '47206940108', 'type': 'PushEvent', 'actor': {'id': 41898282, 'login': 'github-actions[bot]', 'display_login': 'github-actions', 'gravatar_id': '', 'url': 'https://api.github.com/users/github-actions[bot]', 'avatar_url': 'https://avatars.githubusercontent.com/u/41898282?'}, 'repo': {'id': 862690200, 'name': 'zezotalos/Flicker', 'url': 'https://api.github.com/repos/zezotalos/Flicker'}, 'payload': {'repository_id': 862690200, 'push_id': 22988595271, 'size': 1, 'distinct_size': 1, 'ref': 'refs/heads/main', 'head': '08a1f4e2117243b259ffdbd68d0acaa9ff87c8d9', 'before': '149a8bab99320e5170d6cb19f144882dded007f4', 'commits': [{'sha': '08a1f4e2117243b259ffdbd68d0acaa9ff87c8d9', 'author': {'email': 'actions@github.com', 'name': 'Github Actions'}, 'message': 'Updated via Appwrite ⚡️', 'distinct': True, 'url': 'https://api.github.com/repos/zezotalos/Flicker/commits/08a1f4e2117243b259ffdbd68d0acaa9ff87c8d9'}]}, 'public': True, 'created_at': '2025-03-05T03:30:22Z'},
        {'id': '47206940115', 'type': 'CreateEvent', 'actor': {'id': 120878932, 'login': 'Forcryw', 'display_login': 'Forcryw', 'gravatar_id': '', 'url': 'https://api.github.com/users/Forcryw', 'avatar_url': 'https://avatars.githubusercontent.com/u/120878932?'}, 'repo': {'id': 912495310, 'name': 'Forcryw/Proyecto-Laboratorio-Clinico-HPAO', 'url': 'https://api.github.com/repos/Forcryw/Proyecto-Laboratorio-Clinico-HPAO'}, 'payload': {'ref': 'main', 'ref_type': 'branch', 'master_branch': 'main', 'description': None, 'pusher_type': 'user'}, 'public': True, 'created_at': '2025-03-05T03:30:22Z'},
        {'id': '47206940098', 'type': 'PushEvent', 'actor': {'id': 182483123, 'login': 'freefastconnect', 'display_login': 'freefastconnect', 'gravatar_id': '', 'url': 'https://api.github.com/users/freefastconnect', 'avatar_url': 'https://avatars.githubusercontent.com/u/182483123?'}, 'repo': {'id': 861597434, 'name': 'freefastconnect/fastconnect', 'url': 'https://api.github.com/repos/freefastconnect/fastconnect'}, 'payload': {'repository_id': 861597434, 'push_id': 22988595265, 'size': 1, 'distinct_size': 1, 'ref': 'refs/heads/main', 'head': 'bcbc4d577b40e88e18dbbc05f89b821b8765124a', 'before': 'e085b696d8031a995f8ddee42ec6ddc8b345b6fa', 'commits': [{'sha': 'bcbc4d577b40e88e18dbbc05f89b821b8765124a', 'author': {'email': 'freefastconnect@gmail.com', 'name': 'freefastconnect'}, 'message': 'super', 'distinct': True, 'url': 'https://api.github.com/repos/freefastconnect/fastconnect/commits/bcbc4d577b40e88e18dbbc05f89b821b8765124a'}]}, 'public': True, 'created_at': '2025-03-05T03:30:22Z'},
        {'id': '47206940086', 'type': 'PushEvent', 'actor': {'id': 174512503, 'login': 'Naviary3', 'display_login': 'Naviary3', 'gravatar_id': '', 'url': 'https://api.github.com/users/Naviary3', 'avatar_url': 'https://avatars.githubusercontent.com/u/174512503?'}, 'repo': {'id': 828276109, 'name': 'Naviary3/infinitechess.org', 'url': 'https://api.github.com/repos/Naviary3/infinitechess.org'}, 'payload': {'repository_id': 828276109, 'push_id': 22988595273, 'size': 1, 'distinct_size': 1, 'ref': 'refs/heads/checkdetection-ts', 'head': '871e2ed3d492033d7987e326856887f42cdeda15', 'before': 'e2aa15b1f4e5bb9ba3feb24d9ed4bdde1865667e', 'commits': [{'sha': '871e2ed3d492033d7987e326856887f42cdeda15', 'author': {'email': 'tr.bomb20@gmail.com', 'name': 'Naviary Alt'}, 'message': 'Finished checkresolver.ts', 'distinct': True, 'url': 'https://api.github.com/repos/Naviary3/infinitechess.org/commits/871e2ed3d492033d7987e326856887f42cdeda15'}]}, 'public': True, 'created_at': '2025-03-05T03:30:22Z'},
        {'id': '47206940089', 'type': 'PushEvent', 'actor': {'id': 41898282, 'login': 'github-actions[bot]', 'display_login': 'github-actions', 'gravatar_id': '', 'url': 'https://api.github.com/users/github-actions[bot]', 'avatar_url': 'https://avatars.githubusercontent.com/u/41898282?'}, 'repo': {'id': 818631597, 'name': 'Zigistry/Zigistry', 'url': 'https://api.github.com/repos/Zigistry/Zigistry'}, 'payload': {'repository_id': 818631597, 'push_id': 22988595290, 'size': 1, 'distinct_size': 1, 'ref': 'refs/heads/main', 'head': '38c786e6afb25ca360991dddc2c103d050008e2d', 'before': '9e41eec91be909ac0d4189520d43e58ea400d392', 'commits': [{'sha': '38c786e6afb25ca360991dddc2c103d050008e2d', 'author': {'email': 'github-actions@users.noreply.github.com', 'name': 'Github Actions'}, 'message': 'Updated database', 'distinct': True, 'url': 'https://api.github.com/repos/Zigistry/Zigistry/commits/38c786e6afb25ca360991dddc2c103d050008e2d'}]}, 'public': True, 'created_at': '2025-03-05T03:30:22Z', 'org': {'id': 180864418, 'login': 'Zigistry', 'gravatar_id': '', 'url': 'https://api.github.com/orgs/Zigistry', 'avatar_url': 'https://avatars.githubusercontent.com/u/180864418?'}}, {'id': '47206940097', 'type': 'WatchEvent', 'actor': {'id': 10584935, 'login': 'bing-des', 'display_login': 'bing-des', 'gravatar_id': '', 'url': 'https://api.github.com/users/bing-des', 'avatar_url': 'https://avatars.githubusercontent.com/u/10584935?'}, 'repo': {'id': 928427049, 'name': 'om-ai-lab/VLM-R1', 'url': 'https://api.github.com/repos/om-ai-lab/VLM-R1'}, 'payload': {'action': 'started'}, 'public': True, 'created_at': '2025-03-05T03:30:22Z', 'org': {'id': 96569904, 'login': 'om-ai-lab', 'gravatar_id': '', 'url': 'https://api.github.com/orgs/om-ai-lab', 'avatar_url': 'https://avatars.githubusercontent.com/u/96569904?'}},
        {'id': '47206939715', 'type': 'PushEvent', 'actor': {'id': 30538765, 'login': 'signcla-test-unsigned', 'display_login': 'signcla-test-unsigned', 'gravatar_id': '', 'url': 'https://api.github.com/users/signcla-test-unsigned', 'avatar_url': 'https://avatars.githubusercontent.com/u/30538765?'}, 'repo': {'id': 409344435, 'name': 'google-test2/signclav2-probe-repo', 'url': 'https://api.github.com/repos/google-test2/signclav2-probe-repo'}, 'payload': {'repository_id': 409344435, 'push_id': 22988594817, 'size': 1, 'distinct_size': 1, 'ref': 'refs/heads/integration-test-3f5df4f6-fa4e-4906-a1e5-4e76e1cb4c24-fork', 'head': 'de5b130f32b1055038998df9789a9e902d041877', 'before': 'e1ab2ff80b87f6b70d2c2adb56f1d9775d1ebb8f', 'commits': [{'sha': 'de5b130f32b1055038998df9789a9e902d041877', 'author': {'email': 'adam@example.com', 'name': 'Test Author'}, 'message': 'New PR to test SignCLA at 2025-03-04 19:30:17.116982932 -0800 PST m=+1.521725391', 'distinct': True, 'url': 'https://api.github.com/repos/google-test2/signclav2-probe-repo/commits/de5b130f32b1055038998df9789a9e902d041877'}]}, 'public': True, 'created_at': '2025-03-05T03:30:21Z', 'org': {'id': 9579519, 'login': 'google-test2', 'gravatar_id': '', 'url': 'https://api.github.com/orgs/google-test2', 'avatar_url': 'https://avatars.githubusercontent.com/u/9579519?'}},
        {'id': '47206940058', 'type': 'PushEvent', 'actor': {'id': 189940028, 'login': 'CelestiaNFT', 'display_login': 'CelestiaNFT', 'gravatar_id': '', 'url': 'https://api.github.com/users/CelestiaNFT', 'avatar_url': 'https://avatars.githubusercontent.com/u/189940028?'}, 'repo': {'id': 895347228, 'name': 'CelestiaNFT/Welcome-NFT', 'url': 'https://api.github.com/repos/CelestiaNFT/Welcome-NFT'}, 'payload': {'repository_id': 895347228, 'push_id': 22988595241, 'size': 1, 'distinct_size': 1, 'ref': 'refs/heads/main', 'head': '4bf077ce46a0bb4ebce55b43cdfc2e1860a398ce', 'before': '03100c8724e2a2d56630a62090e9c9a6a5ebe2d9', 'commits': [{'sha': '4bf077ce46a0bb4ebce55b43cdfc2e1860a398ce', 'author': {'email': 'root@server1.bizinsure.team', 'name': 'root'}, 'message': 'Update date to 2025-03-04T23:31:03.068Z by CelestiaNFT', 'distinct': True, 'url': 'https://api.github.com/repos/CelestiaNFT/Welcome-NFT/commits/4bf077ce46a0bb4ebce55b43cdfc2e1860a398ce'}]}, 'public': True, 'created_at': '2025-03-05T03:30:22Z'},
        {'id': '47206940064', 'type': 'PushEvent', 'actor': {'id': 41898282, 'login': 'github-actions[bot]', 'display_login': 'github-actions', 'gravatar_id': '', 'url': 'https://api.github.com/users/github-actions[bot]', 'avatar_url': 'https://avatars.githubusercontent.com/u/41898282?'}, 'repo': {'id': 936204276, 'name': 'ReNchi-Z/proxy', 'url': 'https://api.github.com/repos/ReNchi-Z/proxy'}, 'payload': {'repository_id': 936204276, 'push_id': 22988595257, 'size': 1, 'distinct_size': 1, 'ref': 'refs/heads/main', 'head': '9e6dcb3493ffec53aedfcf8265c2194cdf777fb3', 'before': '3598e71e1b130c41e4c4c15d3716a6c2ed0aaa97', 'commits': [{'sha': '9e6dcb3493ffec53aedfcf8265c2194cdf777fb3', 'author': {'email': 'actions@github.com', 'name': 'GitHub Actions'}, 'message': 'Update proxy lists', 'distinct': True, 'url': 'https://api.github.com/repos/ReNchi-Z/proxy/commits/9e6dcb3493ffec53aedfcf8265c2194cdf777fb3'}]}, 'public': True, 'created_at': '2025-03-05T03:30:22Z'},
        {'id': '47206940067', 'type': 'PushEvent', 'actor': {'id': 114463850, 'login': 'vpQtA', 'display_login': 'vpQtA', 'gravatar_id': '', 'url': 'https://api.github.com/users/vpQtA', 'avatar_url': 'https://avatars.githubusercontent.com/u/114463850?'}, 'repo': {'id': 890517106, 'name': 'vpQtA/OvQbKWgY', 'url': 'https://api.github.com/repos/vpQtA/OvQbKWgY'}, 'payload': {'repository_id': 890517106, 'push_id': 22988595262, 'size': 1, 'distinct_size': 1, 'ref': 'refs/heads/main', 'head': '37cb2fb21102e588a863d840645ca6fb2c26d0b4', 'before': 'f3fa31d8e1eafa7b6e62bbe8ab2a5dc25ffc7b6d', 'commits': [{'sha': '37cb2fb21102e588a863d840645ca6fb2c26d0b4', 'author': {'email': '114463850+vpQtA@users.noreply.github.com', 'name': 'vpQtA'}, 'message': '增加了 test_login 单元测试', 'distinct': True, 'url': 'https://api.github.com/repos/vpQtA/OvQbKWgY/commits/37cb2fb21102e588a863d840645ca6fb2c26d0b4'}]}, 'public': True, 'created_at': '2025-03-05T03:30:22Z'}]


pushEvent_msg=['Updated via Appwrite ⚡️ ', #4 
               'super ', #1
               'Finished checkresolver.ts ', #2
               'Updated database ', #2
               'New PR to test SignCLA at 2025-03-04 19:30:17.116982932 -0800 PST m=+1.521725391 ',#11
               'Update date to 2025-03-04T23:31:03.068Z by CelestiaNFT ',#6
               'Update proxy lists ',#3
               '增加了 test_login 单元测试 '] #3

ctrl_msgs = ['Hola y adios',
             ' No molestar',
             '2025-03-04 19:30:17.116982932 -0800 PST m=+1.521725391 ']

class TestMyFunction(unittest.TestCase):
    def test_case_1(self):
        result = MyMonad(["HOLA","adios","No"])
        self.assertIs(type(result),MyMonad,"test_case_1.1")

        result = MyMonad([78,75,21,47])
        self.assertIs(type(result),MyMonad,"test_case_1.2")

    def test_case_2(self):
        monad = MyMonad([78,"dd",21,47])
        with self.assertRaises(TypeError):
            result = monad.flat_filter(filter_PushEvents)
    
    def test_case_3(self):
        monad = MyMonad([78,5,21,47])
        with self.assertRaises(TypeError):
            result = monad.flat_filter(get_PushEvent_msgs)
    
    def test_case_4(self):
        monad = MyMonad(data)
        self.assertIs(type(monad),MyMonad,"test_case_4.1")

        result = monad.flat_filter(filter_PushEvents)
        self.assertEqual(len(result.get()),8,"test_case_4.2")

        
        result2 = result.flat_map(get_PushEvent_msgs)
        self.assertEqual(result2.get(),pushEvent_msg,"test_case_4.3")
        self.assertEqual(len(result2.get()),8,"test_case_4.4")

        tokens = result2.flat_map(tokenize)
        self.assertEqual(reduce(lambda total, sublist: total + len(sublist),tokens.value,0),32,"test_case_4.5")

        tokens2 = MyMonad(ctrl_msgs)

        result3 = tokens2.flat_map(tokenize)
        self.assertEqual(reduce(lambda total, sublist: total + len(sublist),result3.value,0),10, "test_case_4.6")


        
if __name__ == "__main__":
    unittest.main()
