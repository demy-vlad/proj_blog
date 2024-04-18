from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from proxy_list import ProxyList
from datetime import datetime



def get_random_user_agent() -> str:
    '''Возвращает рандомный юзер агент'''
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    return user_agent_rotator.get_random_user_agent()


def get_random_random_proxy() -> str:
    '''Возвращает рандомный IP'''
    proxies = ProxyList()
    proxies.get_random_proxy()
    return proxies.get_random_proxy()


def get_current_date():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d")
    return formatted_date


def get_formatted_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    return current_time