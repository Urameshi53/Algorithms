# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:05:44 2023

@author: User
"""


# The interface of a remote service.
# class ThirdPartYouTubeLib:
#     def listVideos(self):
#         pass 
    
#     def getVideoInfo(self, id):
#         pass 
    
#     def downloadVideo(self, id):
#         pass 
    
    
# '''
# The concrete implementation of a service connector. Methods of this class can
# request information from YouTube. The speed of the request depends on a user's 
# internet connection as well as YouTube's. The application will slow down if a
# lot of requests are fired at the same time, even if they all request the same
# information.
# '''

# class ThirdPartyYouTubeClass(ThirdPartYouTubeLib):
#     def listVideos(self):
#         # Send an API request to YouTube. 
#         pass
        
#     def getVideoInfo(self, id):
#         # Get metadata about some video.
#         pass
        
#     def downloadVideo(self, id):
#         # Download a video file form YouTube.
#         pass
        
    
# '''
# To save some bandwith, we can cache request results and keep them for some 
# time.But it may be impossible to put such code directly into the service class. 
# For example, it could have been provided as part of a third party library 
# and/or defined as `final`. That's why we put the cahing code into a new proxy 
# class which implements the same interface as the service class. 
# It delegates to the service object only when the real requests have to be sent.
# '''
# class CachedYouTubeClass(ThirdPartYouTubeLib):
#     service: ThirdPartYouTubeLib
#     listCache, videoCache = None, None 
#     needReset: None 
    
#     def __init__(self, service: ThirdPartYouTubeLib):
#         self.service = service
        
#     def listVideos(self):
#         if listCache == None or needReset:
#             listCache = self.service.listVideos()
#         return listCache 
    
#     def getVideoInfo(self, id):
#         if videoCache == None or neeReset:
#             videoCache = service.getVideoInfo(id)
#         return videoCache 
    
#     def downloadVideo(self, id):
#         if not downloadExists(id) or needReset:
#             service.downloadVideo(id)
            

# '''
# The GUI class, which used to work directly with a service object, stays 
# unchanged as long as it works with the service object through an interface.
# We can safely pass a proxy object instead of a real service object since 
# they both implement the same interface.
# '''
# class YouTubeManager:
#     service: ThirdPartYouTubeLib
    
#     def __init__(self, service: ThirdPartYouTubeLib):
#         self.service = service 
        
#     def renderVideoPage(self, id):
#         info = self.service.getVideoInfo(id)
#         # Render the video page.
        
#     def renderLIstPanel(self):
#         list = self.service.listVideos()
#         # Render the list of video thumbnails.
        
#     def reactOnUserInput(self):
#         self.renderVideoPage()
#         self.renderListPanel()
            
    
# '''
# The application can configure proxies on the fly.
# '''
# class Application:
#     def init(self):
#         aYouTubeService = ThirdPartyYouTubeClass()
#         aYouTubeProxy = CachedYouTubeClass(aYouTubeService)
#         manager = YouTubeManager(aYouTubeProxy)
#         manager.reactOnUserInput()
        

from abc import ABC, abstractmethod 


class Subject(ABC):
    '''
    The Subject interface declares common operations for both RealSubject and 
    the proxy. As long as the client works with RealSubject using this 
    interface, you'll be able to pass it a proxy instead of a real subject.
    '''
    
    @abstractmethod 
    def request(self) -> None:
        pass
    
    
class RealSubject(Subject):
    '''
    The RealSubject contains some core business logic. Usually, RealSubjects are
    capable of doing some useful work which may also be very slow or sensitive -
    e.g. correcting input data. A proxy can solve these issues without any 
    changes to the RealSubject's code.
    '''
    
    def request(self) -> None:
        print('RealSubject: Handling request.')
        

class Proxy(Subject):
    '''
    The Proxy has an interface identical to the RealSubject.
    '''
    
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject 
        
    def request(self) -> None:
        '''
        The most common applications of the Proxy pattern are lazy loading, 
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending of the result, pass the execution 
        to the same method in a linked RealSubject object.
        '''
        
        if self.check_access():
            self._real_subject.request()
            self.log_access()
            
    def check_access(self) -> bool: 
        print('Proxy: Checking access prior to firing a real request.')
        return True 
    
    def log_access(self) -> None:
        print('Proxy: Logging the time of request.', end='')
        

def client_code(subject: Subject) -> None:
    '''
    The client code is supposed to work with all objects (bot subjects and 
    proxies) via the Subject interface in order to support both real 
    subjects and proxies. In real life, however, clients mostly work with 
    their real subjects directly. In this case, to implement the patter 
    more easily, you can extend your proxy from the real subject's class.
    '''
    
    # ...
    subject.request()
    # ....
    
    
if __name__ == '__main__':
    print('Client: Executing the client code with a real subject:')
    real_subject = RealSubject()
    client_code(real_subject)
    
    print('')
    
    print('Client: Executing the same client code with a Proxy.')
    proxy = Proxy(real_subject)
    client_code(proxy)

    



